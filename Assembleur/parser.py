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

    # Support des lignes du style: "L1: L2: L3: instruction ..."
    if ':' in line:
        parts = [p.strip() for p in line.split(':')]
        rest = parts[-1].strip()
        labels = [p for p in parts[:-1] if p.strip()]

        # Cas: plusieurs labels + instruction derrière
        if labels and rest:
            return {
                "type": "labels_plus_instruction",
                "labels": labels,
                "rest": rest,
                "lineno": lineno,
                "text": original
            }

        # Cas: label seul (ligne qui finit par ':')
        if labels and not rest:
            label = labels[0]
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
            if not item:
                continue

            if item["type"] == "labels_plus_instruction":
                # Ajouter tous les labels
                for lab in item["labels"]:
                    parsed.append({
                        "type": "label",
                        "name": lab,
                        "lineno": item["lineno"],
                        "text": item["text"]
                    })
                # Reparser l'instruction restante
                inst = parse_line(item["rest"], lineno)
                if inst:
                    parsed.append(inst)
            else:
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
