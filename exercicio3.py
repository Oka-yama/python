#Peça a idade e classifique

#0 a 12 criança;
#13 a 17 adolescente;
#18 a 59 adulto;
#60 ou mais idoso

idade = int(input("Digite sua idade: "))

if idade < 13:
    print("É uma criança")
elif idade < 18:
    print("É um adolescente")
elif idade < 60:
    print("É um adulto")
else:
    print("É um idoso")