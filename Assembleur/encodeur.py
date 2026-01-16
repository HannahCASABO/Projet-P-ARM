from __future__ import annotations
from typing import List
import enum_opcode as opc


def check_unsigned_fit(value: int, bits: int) -> int:
    """
    Vérifie que value peut être codée sur 'bits' bits non signés
    Exemple :
        bits = 3  → valeurs autorisées : 0..7
    """
    if value < 0 or value >= (1 << bits):
        raise ValueError(f"Valeur {value} hors plage sur {bits} bits")
    return value

def is_register(tok: str) -> bool:
    t = tok.strip().lower()
    return t.startswith("r") and t[1:].isdigit()


def is_immediate(tok: str) -> bool:
    t = tok.strip().lower()
    if not t.startswith("#"):
        return False
    try:
        int(t[1:], 0)  # accepte #12, #0x10, #-4
        return True
    except ValueError:
        return False


def parse_register(token: str) -> int:
    """
    Transforme 'r3' → 3
    """
    t = token.strip().lower()

    if not is_register(t):
        raise ValueError(f"Registre invalide: {token}")

    return int(t[1:])


def parse_immediate(token: str) -> int:
    """
    Transforme '#12' → 12
    Accepte décimal et hexadécimal (#0x10)
    """
    t = token.strip().lower()

    if not is_immediate(t):
        raise ValueError(f"Immédiat invalide: {token}")

    return int(t[1:], 0)


#Pour insérer dans une liste lisible pour les tests
def list_4x4_insertion(binary: int) -> List[str]:
    """
    Transforme un entier 16 bits en 4 groupes de 4 bits
    Exemple :
        0b1011000010000011
        → ['1011','0000','1000','0011']
    """
    return [
        format((binary >> shift) & 0xF, "04b")
        for shift in (12, 8, 4, 0)
    ]


def encode_line(parsed: List[str]) -> int:
    """
    Retourne un entier représentant l'instruction 16 bits (int binaire)
    """

    if not parsed:
        raise ValueError("Ligne vide")

    mnem = parsed[0].lower()
    length_parsed = len(parsed)

    #------------- Catégorie : Shift, add, sub, mov -------------
    # --- Shift format: shift rd, rn, imm5 ---
    if (mnem in opc.SHIFT_OP) and length_parsed == 4:
        rd = check_unsigned_fit(parse_register(parsed[1]), 3)
        rn = check_unsigned_fit(parse_register(parsed[2]), 3)
        imm5 = check_unsigned_fit(parse_immediate(parsed[3]), 5)
        
        op = opc.SHIFT_OP[mnem]
        return (0b00011 << 13) | (op << 11) | (imm5 << 6) | (rn << 3) | rd
    
    # --- Add_sub_mov_cmp format: adds rd, rn, rm/imm3 ---
    elif(mnem in opc.ADD_SUB_MOV_OP):
        # --- format: adds subs rd, rn, rm/imm3 ---
        if length_parsed == 4:
            rd = check_unsigned_fit(parse_register(parsed[1]), 3)
            rn = check_unsigned_fit(parse_register(parsed[2]), 3)

            #Register format: adds rd, rn, rm
            if is_register(parsed[3]):
                rm_imm3 = check_unsigned_fit(parse_register(parsed[3]), 3)
                is_imm = False
            
            #Immediate format: adds rd, rn, #imm3
            elif is_immediate(parsed[3]):
                rm_imm3 = check_unsigned_fit(parse_immediate(parsed[3]), 3)
                is_imm = True
            else:
                raise ValueError(f"{mnem}: opérande 3 invalide")

            if mnem == "adds":
                op = 0b00 if not is_imm else 0b10
            elif mnem == "subs":
                op = 0b01 if not is_imm else 0b11
            else:
                raise ValueError(f"{mnem}: format rd,rn non supporté")

            return (0b00011 << 11) | (op << 9) | (rm_imm3 << 6) | (rn << 3) | rd

        #Add/Subs-8-bit | Movs | Cmps format: inst rd #imm8
        elif length_parsed == 3:
            rd = check_unsigned_fit(parse_register(parsed[1]), 3)
            imm8 = check_unsigned_fit(parse_immediate(parsed[2]), 8)
            op = opc.ADD_SUB_MOV_OP[mnem]

            # 001 op Rd imm8
            return (0b001 << 13) | (op << 11) | (rd << 8) | imm8

        else:
            raise ValueError(f"Add_sub_mov_cmp: format non supporté: {parsed}")
 
    #-------------  Catégporie : Data processing -------------
    # Syntaxe Thumb: "inst rd, rm" (2 opérandes).
    elif mnem in opc.ALU_OP:
        if len(parsed) < 2:
            raise ValueError(f"{mnem}: il faut au moins Rd")

        rd = check_unsigned_fit(parse_register(parsed[1]), 3)

        #Par défaut rm, sauf lorsqu'il y a 3 opérandes, cela veut dire que Rm = 0 (A revoir)
        rm = parse_register(parsed[2]) if length_parsed <= 3 else 0

        op = opc.ALU_OP[mnem]
        return (0b010000 << 10) | (op << 6) | (rm << 3) | rd
    

    #-------------  Catégporie : Load/Store -------------
    # Syntaxe Thumb: "inst rt, #offset/SP" (2 opérandes).
    elif mnem in opc.LOAD_STORE_OP:
    rt = check_unsigned_fit(parse_register(parsed[1]), 3)
    offset = check_unsigned_fit(parse_immediate(parsed[2]), 8)
    op = opc.LOAD_STORE_OP[mnem]

    return (0b1001 << 12) | (op << 11) | (rt << 8) | offset
    

    #-------------  Catégporie : Miscellaneous 16-bit instructions -------------
    # Syntaxe Thumb: "inst sp, #offset" (2 opérandes).
    elif mnem in opc.MISC_OP:
    offset = check_unsigned_fit(parse_immediate(parsed[2]), 7)
    op = opc.MISC_OP[mnem]

    return (0b1011 << 12) | (op << 7) | offset

    raise NotImplementedError(f"Instruction non supportée (pour l'instant): {parsed}")


#Main test: pour exécuter sur l'ensemble de la liste attendu d'un parseurs 
def encode_program(parsed_lines: List[List[str]]) -> List[List[str]]:
    list_lines = list()
    for line in parsed_lines :
        list_lines.append(list_4x4_insertion(encode_line(line)))
    return list_lines
