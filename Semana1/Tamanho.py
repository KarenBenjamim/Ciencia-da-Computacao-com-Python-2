def dimensoes(x):
    l = 0
    c = 0

    for i in range(len(x)):
        l += 1
    
    coluna = x[i]

    for y in coluna:
        c += 1
    
    print("{}X{}".format(l, c))