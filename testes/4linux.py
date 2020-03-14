#1o
#print("1+1=",1+1)

#2o
#print("Digite uma mensagem")
#msg = input()
#print("Você digitou: %s" % msg)

#3o
#a = 5
#b = 4
#resultado = a * b
#print(resultado)

#4o

#a = int((input("Digite um valor para a: ")))
#b = int((input("Digite um valor para b: ")))

#if a > b:
#    print(a)
#    print("é maior que")
#    print(b)
#else:
#    print(a)
#    print("é menor que")
#    print(b)

#5o
#altura = float((input("Digite sua altura: ")))
#peso = float((input("Digite seu peso ")))
#imc = peso / (altura * altura)

#print(imc)

#if imc < 18.5:
#  print('Baixo peso')
#elif imc > 18.5 and imc < 24.9:
#  print('Peso ideal')
#elif imc > 25 and imc < 29.9:
#  print('Sobrepeso')
#elif imc > 30 and imc < 34.9:
#  print('Obesidade 1o')
#elif imc > 35 and imc < 39.9:
#  print('Obesidade 2o')
#elif imc > 35:
#  print('Obesidade grave')

#While
print("Usando WHILE")
a = 0

while a <= 5:
  print(a)
  a = a + 1

#for
print("Usando FOR")
a = 1

for a in range(1, 11, 2):
  print(a)

#teste aula 5
def vogais():
  print("a")
  print("e")
  print("i")
  print("o")
  print("u")

print("Professora: Existem cinco letras que são vogais:")
vogais()
print(
  "Aluno: Professora, poderia repetir por favor?\
  \nProfessora: Claro, as vogais são:"
  )
vogais()

def somar(a, b):
    return(a + b)

primeiro = 5
segundo = 4

print(somar(primeiro, segundo))


def epar(x):
  return(x%2==0)

x = int((input("Digite um numero: ")))

print(epar(x))

def imc(a, b):
  resultado = (a / (b * b))
  print("Seu IMC é %f" % resultado)
  if resultado < 18.5:
    return('E você esta com baixo peso')
  elif resultado >= 18.5 and resultado <= 24.9:
    return('E você esta com o peso ideal')
  elif resultado >= 25 and resultado <= 29.9:
    return('E você esta com sobrepeso')
  elif resultado >= 30 and resultado <= 34.9:
    return('E você esta com obesidade 1o')
  elif resultado >= 35 and resultado <= 39.9:
    return('E você esta com obesidade 2o')
  elif resultado >= 40:
    return('E você esta com obesidade grave')

altura = float((input("Digite sua altura: ")))
peso = float((input("Digite seu peso ")))

print(imc(peso, altura))