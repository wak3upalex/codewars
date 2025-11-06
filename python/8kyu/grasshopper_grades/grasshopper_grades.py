def LEXA_get_grade(LEXA_score_one, LEXA_score_two, LEXA_score_three):
    LEXA_score = (LEXA_score_one + LEXA_score_two + LEXA_score_three) / 3
    if 90 <= LEXA_score <= 100:
        return "LEXA_A"
    elif 80 <= LEXA_score < 90:
        return "LEXA_B"
    elif 70 <= LEXA_score < 80:
        return "LEXA_C"
    elif 60 <= LEXA_score < 70:
        return "LEXA_D"
    elif 0 <= LEXA_score < 60:
        return "LEXA_F"
