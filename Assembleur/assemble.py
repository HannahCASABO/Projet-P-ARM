from parser import parse_file, parse_file_list
from encodeur import encode_line, list_4x4_insertion
import enum_opcode as opc



import enum_opcode as opc

def resolve_labels(program: list[dict]) -> list[list[str]]:
    """
    2 passes:
    - pass 1: label -> adresse (index d'instruction 16-bit)
    - pass 2: remplace les branches "bxx label" par "bxx #offset"
              offset = target_index - (current_index + 1)
    Retourne une liste de tokens (instructions uniquement).
    """
    label_addr: dict[str, int] = {}
    inst_entries: list[dict] = []

    pc = 0
    for entry in program:
        if entry["type"] == "label":
            # Normalisation: casse insensible
            label_addr[entry["name"].lower()] = pc
        elif entry["type"] == "instruction":
            inst_entries.append(entry)
            pc += 1

    resolved: list[list[str]] = []
    for i, entry in enumerate(inst_entries):
        tokens = [entry["mnemonic"]] + entry["operands"]
        mnem = tokens[0].lower()

        # Branch conditionnels: beq/bne/... label -> #offset
        if mnem in getattr(opc, "COND_BRANCH_OP", {}) and len(tokens) == 2 and not tokens[1].startswith("#"):
            target = tokens[1].lower()
            if target in label_addr:
                off = label_addr[target] - (i + 3)
                tokens = [mnem, f"#{off}"]

            else:
        # si clang: on ignore pour ne pas bloquer
                if tokens[1].startswith(".LBB"):
                    tokens = ["b", "#0"]

        # Branch inconditionnel: b label -> #offset
        if mnem == "b" and len(tokens) == 2 and not tokens[1].startswith("#"):
            target = tokens[1].lower()
            if target in label_addr:
                off = label_addr[target] - (i + 3)
                tokens = [mnem, f"#{off}"]
            else:
                # si clang .LBB... pas trouvé, on ignore
                if tokens[1].startswith(".LBB"):
                    tokens = ["b", "#0"]

        resolved.append(tokens)

    return resolved







def encode_program_bin(program: list[dict]) -> list[int]:
    """
    Encode tout le programme avec un affichage en 4x4 bits
    => Renvoie une liste d'entiers 16 bits
    """
    out = []

    # 2 passes : labels -> offsets
    resolved_tokens = resolve_labels(program)

    for tokens in resolved_tokens:
        sequence = encode_line(tokens)
        if sequence == -1:
            continue
        out.append(sequence)
        print(f"{tokens} -> {' '.join(list_4x4_insertion(sequence))}")

    print("\nAffichage de la liste d'encodage du fichier :")
    print(out)
    return out



def convert_hexadecimal(binary: list[int]) -> list[str]:
    """
    Convertit une liste d'entiers 16 bits en hexadécimal
    """
    hex_out = [f"{word:04x}" for word in binary]
    print(hex_out)
    return hex_out


def assemble_file(filename: str) -> list[str]:
    """
    Pipeline complet assembleur :
    asm -> binaire -> hexadécimal
    """
    program = parse_file(filename)

    print("\nRetour du parseur :")
    for inst in parse_file_list(filename):
        print(inst)

    print("\nEncodage:")
    binary = encode_program_bin(program)

    print("\nConversion hexadécimale:")
    hexadecimal = convert_hexadecimal(binary)

    print("\nRésultat final :")
    print(" ".join(hexadecimal))

    return hexadecimal
