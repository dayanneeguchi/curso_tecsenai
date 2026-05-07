#operador lógico or/ou
est = input("É estudante? (sim ou não) ")
ido = input("Tem mais de 60 anos? (sim ou não)  ")

if est == "sim" or ido == "sim":
    print("Ganhou desconto VIP! ")
else:
    print("Não possui desconto válido! ")