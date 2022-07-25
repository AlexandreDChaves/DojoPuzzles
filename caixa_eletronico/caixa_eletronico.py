saque = int(input("Qual o valor do saque: R$ "))
for nota in[100, 50, 20, 10]:
    quantidade = saque // nota
    saque = saque % nota
    if quantidade > 0:
        print(f"{quantidade} notas de R$: {nota}")