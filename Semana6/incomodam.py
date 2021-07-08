def elefantes(n):
    if n < 2:
        return ''
    elif n == 2:
        return 'Um elefante incomoda muita gente\n' + str(n) + ' elefantes ' + incomodam(n) + 'muito mais\n'
    else:
        return elefantes(n-1) + str(n-1) + ' elefantes incomodam muita gente\n' + str(n) + ' elefantes ' + incomodam(n) + 'muito mais\n'
    for n in range(1, 5):
        return 'Para n = ', n
        return elefantes(n)

def incomodam(n):
    if n <= 0:
        return ""
    if n == 1:
        return "incomodam "
    else:
        return "incomodam " + incomodam(n-1)
