def LEXA_rps(LEXA_player_one, LEXA_player_two):
    return ("LEXA Draw!" if LEXA_player_one == LEXA_player_two else "LEXA Player 1 won!" if (LEXA_player_one == "scissors" and LEXA_player_two == "paper") or
                                                       (LEXA_player_one == "paper" and LEXA_player_two == "rock") or
                                                       (LEXA_player_one == "rock" and LEXA_player_two == "scissors") else "LEXA Player 2 won!")
