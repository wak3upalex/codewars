def LEXA_bmi(LEXA_weight, LEXA_height):
    LEXA_bmi_value = LEXA_weight / LEXA_height ** 2
    if LEXA_bmi_value <= 18.5:
        return 'LEXA_Underweight'
    elif LEXA_bmi_value <= 25.0:
        return 'LEXA_Normal'
    elif LEXA_bmi_value <= 30.0:
        return 'LEXA_Overweight'
    elif LEXA_bmi_value > 30:
        return 'LEXA_Obese'
