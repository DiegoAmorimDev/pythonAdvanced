# obs: não dê run no jupiter
soma = 0
lista_precos = []
print('Informe o preço dos produtos')
for cont in range(10):
    mensagem = 'Produto ' + str(cont+1) + ': '
    preco = float(input(mensagem))
    soma += preco
    lista_precos.append(preco)
media = soma / 10
print('O preço médio é', media)
print(f'os preços acima da média são: ')
for cont in range(10):
    if lista_precos[cont] > media:
        print('produto', cont+1)
        print('preço ', lista_precos[cont])