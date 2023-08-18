def recebe_string(palavra):
    indice = 0
    palavra_compactada = ''
    tamanho_palavra = len(palavra)

    while indice != tamanho_palavra:
        contador = 1
        while (indice < tamanho_palavra - 1) and (palavra[indice] == palavra[indice+1]):
            contador += 1
            indice += 1

        if contador == 1:
            palavra_compactada += str(palavra[indice])
        else:
            palavra_compactada += str(palavra[indice]) + str(contador)
        indice += 1
    return palavra_compactada

print(recebe_string('jjjjooaoo'))
