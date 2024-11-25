def is_vow(inp):
    for i in range(len(inp)):
        if inp[i] == 97 or inp[i] == 101 or inp[i] == 105 or inp[i] == 111 or inp[i] == 117:
            inp[i] = chr(inp[i])
    return inp
