def calcular_media(valores):
    tamanho = len(valores)
    soma = sum(valores)
    media = soma / tamanho if tamanho > 0 else 0
    return media

continuar = True
valores = []

while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor: ')

    if valor.lower() == 'ok':
        continuar = False
    else:
        valores.append(float(valor))

media = calcular_media(valores)

print(f"A média calculada para os valores {valores} foi de {media}.")



