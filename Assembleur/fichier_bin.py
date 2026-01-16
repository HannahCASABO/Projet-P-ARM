import sys
from pathlib import Path

from assemble import assemble_file


def write_bin_file(hex_words: list[str], output_filename: str):
    """
    Écrit un fichier .bin au format Logisim (v2.0 raw)
    """
    with open(output_filename, "w", encoding="ascii") as f:
        f.write("v2.0 raw\n")
        f.write(" ".join(hex_words))
        f.write("\n")


# =======================
# Point d'entrée
# =======================

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fichier_bin.py <fichier.asm>")
        sys.exit(1)

    asm_file = Path(sys.argv[1])

    if not asm_file.exists():
        print(f"Erreur : fichier introuvable : {asm_file}")
        sys.exit(1)

    # Appel de l'assembleur
    hex_words = assemble_file(str(asm_file))

    # Génération du fichier .bin
    output_bin = asm_file.with_suffix(".bin")
    write_bin_file(hex_words, output_bin)

    print(f"\nFichier généré : {output_bin}")
