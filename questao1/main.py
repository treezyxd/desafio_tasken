while True:
    try:
        inteiro = int(input('Digite um numero inteiro: '))
        break
    except ValueError:
        print('Nao eh um numero inteiro...')
        print()


def recebe_valor_inteiro(x):
    qtd_valor = x
    valor = x

    arr_aux = []

    while qtd_valor > 0:

        while valor > 0:
            arr_aux.append(valor**2)

            valor -= 1

        print(*arr_aux)

        if valor == 0:
            arr_aux.clear()

        qtd_valor -= 1
        valor = qtd_valor


recebe_valor_inteiro(inteiro)
