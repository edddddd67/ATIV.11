# Crie um programa que receba a idade de uma pessoa e classifique-a de acordo com as seguintes faixas etárias:
# Criança (0-12 anos)
# Adolescente (13-17 anos)
# Adulto (18-59 anos)
# Idoso (60 anos ou mais)

id = int(input("idade da pessoa: "))
if(id <= 12):
    print("criança")


elif (id <=17) and (id >=13):
    print("adolescente")

elif (id <=59) and (id >=18):
    print('adulto')

elif (id >= 60):
    print('idoso')
