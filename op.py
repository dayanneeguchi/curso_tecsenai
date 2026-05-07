#operador lógico or/ou
idade = int(input("Qual sua idade? "))
condicao_fisica = input("Possui teste físico aprovado? (sim ou não) ")
atestado_medico = input("Possui atestado médico aprovado? (sim ou não) ")

if idade >= 18 and (condicao_fisica or atestado_medico);
    print("Parabéns! ")
else:
    print("Não foi dessa vez! ")