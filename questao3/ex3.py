num_digitado = ''
arr = []
maior_valor = 0
media = 0
menor_impar = 0
qtd_vezes_numero = 0


while True:
    try:
        num_digitado = int(input('Vá digitando numeros inteiros... Digite 0 pra parar  '))

        if num_digitado == 0:
            break

        arr.append(num_digitado)

    except ValueError:
        print('Nao eh um inteiro...')
        print()


print(arr)


def qtd_numeros():
    return f'Foram Lidos {len(arr)} numeros'


def maior_numero_lido():
    global maior_valor
    for num in arr:
        if num > maior_valor:
            maior_valor = num

    return f'O maior numero eh {maior_valor}'


def calcula_menor_impar():
    global menor_impar, maior_valor
    menor_impar = maior_valor
    for num in arr:
        if num % 2 != 0 and menor_impar > num:
            menor_impar = num
            return f'O menor numero impar eh {menor_impar}'

        return 'Nao houve numeros impares'


def contador_de_numeros():
    global qtd_vezes_numero
    conjunto_resposta = set([])
    conjunto = set()
    for num in arr:
        if num in conjunto:
            qtd_vezes_numero = arr.count(num)
            conjunto_resposta.add(f'o numero {num} apareceu {qtd_vezes_numero} vez(es)')
        conjunto.add(num)

    print(*conjunto_resposta)






print(qtd_numeros())
print(maior_numero_lido())
print(calcula_menor_impar())
contador_de_numeros()
