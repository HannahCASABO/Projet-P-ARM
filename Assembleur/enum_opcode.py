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
    "tsts": 0b1000,
    "rsbs": 0b1001,
    "cmps": 0b1010,
    "cmns": 0b1011,
    "orrs": 0b1100,
    "muls": 0b1101,
    "bics": 0b1110,
    "mvns": 0b1111,
}

#Format Imm8 pour le ADD_SUB_MOV_OP:
ADD_SUB_MOV_OP = {
    "adds": 0b00,
    "subs": 0b01,
    "movs": 0b10,
    "cmps": 0b11,
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