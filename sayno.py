meses = 12
dias = 30

tempo = int(input('Tempo como fumante (em anos).....: '))
valor_maco = float(input('Valor do maço....................: ').replace(",", "."))
qtd_macos_dia = float(input("Quantidade de maços por dia............: ").replace(",", "."))

qtd_macos_ano = qtd_macos_dia * dias * meses * tempo
gasto = qtd_macos_ano * valor_maco

if gasto < 20000:
    print("Com o valor R$ {:.2f}, você poderia ter dado entrada em um carro.".format(gasto))
elif gasto >= 20000 and gasto < 50000:
    print("Com o valor R$ {:.2f}, você poderia ter comprado um carro popular usado.".format(gasto))
else:
    print("Com o valor R$ {:.2f}, você poderia ter comprado um carro zero.".format(gasto))