import sys
from pathlib import Path


def remove_comment(line: str) -> str:
    return line.split('@', 1)[0]


def is_directive(line: str) -> bool:
    s = line.lstrip()
    return s.startswith('.') and ':' not in s


def extract_sp_immediate(op: str):
    """
    Extrait l'immédiat depuis [sp, #imm]
    Retourne '#imm' ou None si non applicable
    """
    # Transforme #imm] -> #imm
    if op.startswith("#") and op.endswith("]"):
        return op[:-1]

    return op

def parse_line(line: str, lineno: int) -> dict:
    
    original = line.rstrip("\n")
    line = remove_comment(line).strip()
    if not line or is_directive(line):
        return None

    s = line.strip()
    if s.endswith(':'):
        label = s[:-1].strip()

        # Ignorer les labels de debug clang (.LBB...)
        if label.startswith(".LBB"):
            return None

        return {
            "type": "label",
            "name": label,
            "lineno": lineno,
            "text": original
        }

    tokens = (line
              .replace(',', ' ')
              .replace('[', ' [')
              .replace(']', ' ] ')
              .split())

    if not tokens:
        return None

    mnemonic = tokens[0].lower()
    raw_operands = tokens[1:]
    operands = []

    for op in raw_operands:
        if op == ']':
            continue
        norm = extract_sp_immediate(op)
        if norm is not None:
            operands.append(norm)

    # Ignorer les branches de debug clang (b .LBB...)
    if mnemonic == "b" and operands and operands[0].startswith(".LBB"):
        return None

    # Ignorer l'épilogue si ton CPU Logisim ne fait pas de retour
    if mnemonic == "bx" and operands == ["lr"]:
        return None

    # (optionnel) ignorer aussi "add sp, #imm" d'épilogue si tu ne le supportes pas
    # if mnemonic == "add" and operands[:2] == ["sp", "#40"]:
    #     return None

    return {
        "type": "instruction",
        "mnemonic": mnemonic,
        "operands": operands,
        "lineno": lineno,
        "text": original,
    }



def parse_file(filename: str) -> list[dict]:
    """
    Retourn une liste dictionnaire pour identifier chaque élément
    """
    path = Path(filename)
    if not path.exists():
        raise FileNotFoundError(f"Fichier introuvable: {path.resolve()}")

    parsed = []
    with path.open("r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, start=1):
            item = parse_line(line, lineno)
            if item:
                parsed.append(item)
    return parsed

def parse_file_list(filename: str) -> list[list[str]]:
    """
    Retourne une liste de listes des instructions:
    """
    path = Path(filename)
    if not path.exists():
        raise FileNotFoundError(f"Fichier introuvable: {path.resolve()}")

    parsed = []
    with open(filename, "r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, start=1):
            item = parse_line(line, lineno)
            if item and item["type"] == "instruction":
                tokens = [item["mnemonic"]] + item["operands"]
                parsed.append((lineno, tokens))
    return parsed



#Test dans le terminale :
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parser.py <fichier.asm>")
        sys.exit(1)

    asm_file = sys.argv[1]
    program = parse_file(asm_file)

    for entry in program:
        if entry["type"] == "label":
            print(f"Label : {entry['name']}")
        else:
            print(f"Instr : {entry['mnemonic']}")
            for i, op in enumerate(entry["operands"]):
                print(f"  Op{i} : {op}")
