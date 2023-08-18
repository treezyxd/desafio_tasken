caminho_arquivo = 'C:\\Users\\treezy\\PycharmProjects\\desafio_tasken\\questao4\\'
caminho_arquivo += 'texto.txt'
vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
soma_vogal = 0
soma_consoante = 0

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('hello my world\n')
    arquivo.write('ola meu mundo')

    arquivo.seek(0, 0)

    linha1 = arquivo.readline()
    linha2 = arquivo.readline()

    for letra in linha1:
        if letra in vogais:
            soma_vogal += 1

        if letra in consoantes:
            soma_consoante += 1

    if soma_vogal >= soma_consoante:
        print('A linha 1 possui mais vogais')
    else:
        print('A linha 1 possui mais consoantes')

    for letra in linha2:
        soma_vogal = 0
        soma_consoante = 0
        if letra in vogais:
            soma_vogal += 1

        if letra in consoantes:
            soma_consoante += 1

    if soma_vogal >= soma_consoante:
        print('A linha 2 possui mais vogais')
    else:
        print('A linha 2 possui mais consoantes')