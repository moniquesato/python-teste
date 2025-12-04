
# app.py - Programa de teste de Python

def saudacao(nome):
    return f"Olá, {nome}!"

nome = input("Digite seu nome: ")
print(saudacao(nome))

# Perguntar nome e idade
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print(f"Olá, {nome}! Você tem {idade} anos.")

# Fazer uma soma simples
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
print("A soma dos números é:", num1 + num2)

# Guardar frutas em uma lista
frutas = []
for i in range(3):
    fruta = input(f"Digite a fruta {i+1}: ")
    frutas.append(fruta)

print("As frutas que você digitou são:", frutas)
