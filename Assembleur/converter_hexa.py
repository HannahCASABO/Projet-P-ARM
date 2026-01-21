def bintohexa(bin_list):
    hexa = [''] * 4

    # Découper en groupes de 4 bits
    bindiv = [
        bin_list[0:4],
        bin_list[4:8],
        bin_list[8:12],
        bin_list[12:16]
    ]

    for i in range(4):
        hexatmp = 0
        for j in range(4):
            if bindiv[i][j] == 1:
                hexatmp += 1 << (3 - j)

        if hexatmp < 10:
            hexa[i] = chr(ord('0') + hexatmp)
        else:
            hexa[i] = chr(ord('A') + (hexatmp - 10))

    return ''.join(hexa)


# Exemple d'utilisation
bin_list = [
    1, 1, 1, 1,
    1, 1, 0, 0,
    0, 1, 1, 1,
    1, 0, 0, 1
]

hex_value = bintohexa(bin_list)
print("Hex:", hex_value)
