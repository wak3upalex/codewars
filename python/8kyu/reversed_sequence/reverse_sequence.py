def LEXA_reverse_seq(LEXA_number):
    LEXA_answer = []
    while LEXA_number > 0:
        LEXA_answer.append(LEXA_number)
        LEXA_number -= 1
    return LEXA_answer
