from parser import parse_file, parse_file_list
from encodeur import encode_line, list_4x4_insertion


def encode_program_bin(program: list[dict]) -> list[int]:
    """
    Encode tout le programme avec un affichage en 4x4 bits
    => Renvoie une liste d'entiers 16 bits
    """
    out = []
    for entry in program:
        if entry["type"] == "instruction":
            tokens = [entry["mnemonic"]] + entry["operands"]

            sequence = encode_line(tokens)
            if(sequence == -1):
                continue
            out.append(sequence)

            # affichage binaire
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
