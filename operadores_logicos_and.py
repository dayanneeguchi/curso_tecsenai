#operador lógico and
idade = int(input("Digite sua idade: "))
cnh = input("Tem CNH? (SIM/NÃO): ")

if idade >= 18 and cnh == "sim":
    print("Você pode dirigir: ")
else:
    print("Não pode dirigir! ")
