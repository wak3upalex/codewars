def LEXA_count_sheeps(LEXA_sheep):
    LEXA_count = 0
    for LEXA_item in LEXA_sheep:
        if LEXA_item == True:
            LEXA_count += 1
    return LEXA_count
