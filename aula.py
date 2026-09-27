preco = float(input("Digite o preço do produto: R$"))
porcentagem = int(input("Digite a porcentagem do desconto (Ex: 5, 20:):"))
desconto = preco * (porcentagem / 100)
preco_final = preco - desconto
print("Com desconto, o valor fica: R$", str(preco_final))
