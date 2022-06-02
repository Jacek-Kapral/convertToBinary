def intoBinary(number):
    binarynumber=""
    if (number!=0):
        while (number>=1):
            if (number %2==0):
                binarynumber=binarynumber+"0"
                number=number//2
            else:
                binarynumber=binarynumber+"1"
                number=(number-1)//2

    else:
        binarynumber="0"

    return "".join(reversed(binarynumber))


print('Konwersja liczby dziesietnej na binarna od 0 do 255')
print('Wprowadz liczbe dziesietna i nacisnij enter:')
dec = int(input())
if dec <= 255:

    binarka = intoBinary(dec)
    binz = ''

    while len(binarka) != 8:
        binarka = '0' + str(binarka)

    print(binarka)
else:
    print('Wprowadziles za duza liczbe')