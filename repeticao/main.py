# Quando usar o for:
# O for deve ser utilizado quando sabemos
# quantas vezes queremos repetir uma ação
# ou quando queremos percorrer uma sequência de valores

# Exemplos:

# Repetir algo 10 vezes:

for num2 in range(1,10):
    print(num2 + 1)

# Percorrer uma lista com nomes:
nomes = ['Victor','Arthur','Bryan','Isaias']
print(nomes)

# Mostrar os números de 1 a 100:

for numero in range(1,100):
    print(numero + 1)

# Calcular a tabuada de um número
numero = 5

for num_atual in range(1,11):
    resultado = numero * num_atual
    print(numero, 'x',  num_atual, '=', resultado)
