import sys
from pathlib import Path


def remove_comment(line: str) -> str:
    return line.split('@', 1)[0]


def is_directive(line: str) -> bool:
    s = line.lstrip()
    return s.startswith('.') and ':' not in s


def parse_line(line: str, lineno: int) -> dict:
    original = line.rstrip("\n")
    line = remove_comment(line).strip()
    if not line or is_directive(line):
        return None

    if ':' in line:
        label = line.split(':', 1)[0].strip()
        return {
            "type": "label", 
            "name": label, 
            "lineno": lineno, 
            "text": original
        }

    tokens = line.replace(',', ' ').split()
    if not tokens:
        return None

    return {
        "type": "instruction",
        "mnemonic": tokens[0].lower(),
        "operands": [op.lower() for op in tokens[1:]],
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
