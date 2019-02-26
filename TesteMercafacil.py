# #Desafio de criptografia:
#
# Desenvolver um algoritmo em qualquer linguagem de programação que tome como input uma string criptografada e a imprima descriptografada.
#
# Criptografia Prime-Scramble:
# O valor ASCII de cada membro da string é somado ao número primo de mesmo índice. Exemplo:
#
# a b c d e f g h i j
# + + + + + + + + + +
# 2 3 5 7 11 13 17 19 23 29
# = = = = = = = = = =
# c e h k p s x { # *
# limite inferior: VALOR DECIMAL = 33 <=> CARACTERE = !
# limite superior: VALOR DECIMAL = 125 <=> CARACTERE = }
#
# Note que caso a soma do caractere com o número primo seja maior do que o limite superior, ele deve começar novamente a partir do limite inferior. Por exemplo:
#
# i(105) + 23 = 128. 128 > 125. criptografia = 33 + (128 - 126) = 35 = #
#
# 'cqil}##$E3.79>AuKEXMMXW_mt8{u'


def gen_prime(end):
    """
    gera uma lista de numero primo
    :param end: integer
    """
    cript=[2]
    z=0
    aux=0
    cont=3
    while z < end:
        for x in range(2, cont, 1):
            if cont % x == 0:
                aux = aux + 1
        if aux == 0:
            cript.append(cont)
        cont = cont + 1
        if aux == 0:
            z = z + 1
        aux = 0
    return cript


def index_to_prime(index):
    prime_list = gen_prime(93)
    return prime_list[index]


def get_char(index, letter):
    ascii_letter = ord(letter)
    index_prime = index_to_prime(index)
    return [index_prime, ascii_letter]


def char_limit(ascii_code):
    if ascii_code < 33:
        return 126-(33 - ascii_code)
    elif ascii_code < 125:
        return ascii_code
    return (ascii_code % 93) + 33


def char_limit2(ascii_code):
    if ascii_code > 125:
        return ascii_code - 126 + 33
    return ascii_code


def decrypt(crypt_txt):
    txt = []
    for i, c in enumerate(crypt_txt):
        temp = get_char(i, c)
        tempb = temp[1] - temp[0]
        tempb = char_limit(tempb)
        txt.append(chr(tempb))
    print(''.join(txt))


def crypt(text):
    txt = []
    for i, c in enumerate(text):
        temp = get_char(i, c)
        tempb = (temp[1]) + temp[0]
        tempb = char_limit2(tempb)
        txt.append(chr(tempb))
    print(''.join(txt))


decrypt('cqil}##$E3.79>AuKEXMMXW_mt8{u')
decrypt('ohhvy$&t.!/->13>?COV')
crypt('testecript')
