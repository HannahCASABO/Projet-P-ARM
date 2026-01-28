# Opcodes Thumb ALU "data-processing register" (010000 op Rm Rd)
ALU_OP = {
    "ands": 0b0000,
    "eors": 0b0001,
    "lsls": 0b0010,
    "lsrs": 0b0011,
    "asrs": 0b0100,
    "adcs": 0b0101,
    "sbcs": 0b0110,
    "rors": 0b0111,
    "tst": 0b1000,
    "rsbs": 0b1001,
    "cmp": 0b1010,
    "cmn": 0b1011,
    "orrs": 0b1100,
    "muls": 0b1101,
    "bics": 0b1110,
    "mvns": 0b1111,
}

#Format Imm8 pour le ADD_SUB_MOV_OP:
ADD_SUB_MOV_OP = {
    "movs": 0b00,
    "cmps": 0b01,
    "adds": 0b10,
    "subs": 0b11,
}

#Format Imm5 pour les Shit:
SHIFT_OP = {
    "lsls": 0b00,
    "lsrs": 0b01,
    "asrs": 0b10,
}

#Opcodes Thumb ALU "Load/Store register" (1001 op Rt SP/offset)
LOAD_STORE_OP = {
    "str": 0b0,
    "ldr": 0b1,
}

#Opcodes Thumb ALU "Miscellaneous 16-bit instructions" (1011 op SP offset)
MISCELLANEOUS_OP = {
    "add": 0b00000,
    "sub": 0b00001,
}

# Branch conditionnel Thumb (1101 cond imm8)
COND_BRANCH_OP = {
    "beq": 0b0000,
    "bne": 0b0001,
    "bcs": 0b0010,
    "bcc": 0b0011,
    "bmi": 0b0100,
    "bpl": 0b0101,
    "bvs": 0b0110,
    "bvc": 0b0111,
    "bhi": 0b1000,
    "bls": 0b1001,
    "bge": 0b1010,
    "blt": 0b1011,
    "bgt": 0b1100,
    "ble": 0b1101,
    "bal": 0b1110,
}
