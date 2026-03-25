identificationName = input("Qual o seu nome? ")
identificationClass = input("Qual disciplina você cursa? ")
identificationProfessor = input("Qual o nome do seu professor? ")

print(f"Olá, {identificationName}, você está cursando {identificationClass} e o nome do seu professor é {identificationProfessor}.")


firstgrade = float(input("Adicione sua primeira nota: "))
secondgrade = float(input("Adicione sua segunda nota: "))
thirdgrade = float(input("Adicione sua terceira nota: "))
fourthgrade = float(input("Adicione sua quarta nota: "))

addgrades = firstgrade + secondgrade + thirdgrade + fourthgrade

media = addgrades / 4

print(f"Sua média de notas é: {media}")