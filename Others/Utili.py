def media(*args):
    """
    Calcula a média de um conjunto de números.
    """
    if len(args) == 0:
        return 0
    else:
        return sum(args) / len(args)

print(media(10,8.33,8.33,10,8.33,8.75,5.83,10,0,5,7.5,0,7.5,0,0,10,10))