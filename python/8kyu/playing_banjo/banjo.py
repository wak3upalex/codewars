def are_you_playing_banjo(name):
    return name + " plays banjo" if name.startswith('R') == True or name.startswith(
        'r') == True else name + " does not play banjo"
