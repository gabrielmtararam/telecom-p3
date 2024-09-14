def decode(signal):
    estado = 0
    resultado = list()
    dado_anterior = 0
    lista_bits = []
    posicao_atual = 1
    atual = signal[0]
    ocioso = False
    indice = 1

    while indice < len(signal) and not ocioso:
        amostra = signal[indice]
        if amostra == atual:
            posicao_atual += 1
        else:
            if posicao_atual >= 19:
                ocioso = True
            elif posicao_atual >= 5:
                posicao_atual = 0

                if estado == 0:
                    if dado_anterior == amostra and amostra == 1:
                        estado = 1
                    dado_anterior = amostra
                elif estado == 1:
                    lista_bits.append(amostra)
                    if len(lista_bits) == 8:
                        valor_byte = sum(lista_bits[i] * (2 ** i) for i in range(8))
                        resultado.append(valor_byte)
                        lista_bits = []

            atual = amostra
        indice += 1

    return bytes(resultado)

