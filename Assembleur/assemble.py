from parser import parse_file, parse_file_list
from encodeur import encode_line, list_4x4_insertion


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
            sequence = encode_line(tokens)   # int 16 bits
            out.append(sequence)

            # affichage binaire conservé
            print(f"{tokens} -> {' '.join(list_4x4_insertion(sequence))}")

    print("\nAffichage de la liste d'encodage du fichier :")
    print(out)
    return out


def convert_hexadecimal(binary: list[int]) -> list[str]:
    """
    Convertit une liste d'entiers 16 bits en hexadécimal (base 16)
    """
    hex_out = []
    for word in binary:
        hex_out.append(f"{word:04x}")

    print(hex_out)
    return hex_out


def assemble_file(filename: str) -> list[str]:
    """
    Pipeline complet assembleur :
    asm -> binaire -> hexadécimal

    Retourne la liste hexadécimale
    """
    program = parse_file(filename)
    print_parseur = parse_file_list(filename)

    print("Retour du parseur :")
    for inst in print_parseur:
        print(inst)

    print("\nEncodage:")
    binary = encode_program_bin(program)

    print("\nConversion hexadecimal:")
    hexadecimal = convert_hexadecimal(binary)

    print("\nRésultat final :")
    print(" ".join(hexadecimal))

    return hexadecimal

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
            sequence = encode_line(tokens)   # int 16 bits
            out.append(sequence)

            # affichage binaire conservé
            print(f"{tokens} -> {' '.join(list_4x4_insertion(sequence))}")

    print("\nAffichage de la liste d'encodage du fichier :")
    print(out)
    return out


def convert_hexadecimal(binary: list[int]) -> list[str]:
    """
    Convertit une liste d'entiers 16 bits en hexadécimal (base 16)
    """
    hex_out = []
    for word in binary:
        hex_out.append(f"{word:04x}")

    print(hex_out)
    return hex_out


def assemble_file(filename: str) -> list[str]:
    """
    Pipeline complet assembleur :
    asm -> binaire -> hexadécimal

    Retourne la liste hexadécimale
    """
    program = parse_file(filename)
    print_parseur = parse_file_list(filename)

    print("Retour du parseur :")
    for inst in print_parseur:
        print(inst)

    print("\nEncodage:")
    binary = encode_program_bin(program)

    print("\nConversion hexadecimal:")
    hexadecimal = convert_hexadecimal(binary)

    print("\nRésultat final :")
    print(" ".join(hexadecimal))

    return hexadecimal
