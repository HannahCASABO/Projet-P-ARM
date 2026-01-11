from parser import parse_file,parse_file_list
from encodeur import encode_line, list_4x4_insertion

def encode_program_bin(program: list[dict]) -> list[int]:
    """
    Encode tout le programme mais cette fois avec un affichage en 4x4 bits
    
    => Renvois une liste contenant le nombre binaire en séquence de 4x4bits
    """
    out= []
    for entry in program:
        if entry["type"] == "instruction":
            tokens = [entry["mnemonic"]] + entry["operands"]
            sequence = encode_line(tokens)
            out.append(sequence)

            print(f"{str(tokens)} -> {' '.join(list_4x4_insertion(sequence))}")

    print("\nAffichage de la liste d'encodage du fichier :")
    print(out)
    return out



#Affichage :
program = parse_file("branch.txt")
print_parseur = parse_file_list("branch.txt")

print("Retour du parseur :")
for inst in print_parseur:
    print(inst)

print("\nEncodage:")
encode_program_bin(program)