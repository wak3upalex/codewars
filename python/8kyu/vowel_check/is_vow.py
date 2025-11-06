def LEXA_is_vow(LEXA_input):
    for LEXA_index in range(len(LEXA_input)):
        if LEXA_input[LEXA_index] == 97 or LEXA_input[LEXA_index] == 101 or LEXA_input[LEXA_index] == 105 or LEXA_input[LEXA_index] == 111 or LEXA_input[LEXA_index] == 117:
            LEXA_input[LEXA_index] = chr(LEXA_input[LEXA_index])
    return LEXA_input
