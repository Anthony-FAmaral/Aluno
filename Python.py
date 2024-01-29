# Exercício 4: 
# Faça um script que recebe o nome e as 4 notas de um aluno. Retorne a média
# e seu status, de acordo com as condições a seguir.
# nota >= 7: Aprovado
# nota <= 5: Reprovado
# nota > 5 e <7: Recuperação

nome = str(input("nome do aluno "))
nota1 = float(input("digite a primeira nota "))
nota2 = float(input("digite a segunda nota "))
nota3 = float(input("digite a terceira nota "))
nota4 = float(input("digite a quarta nota "))

media = (nota1 + nota2 + nota3 + nota4)/4

if media >= 7 : 
  x = "Reprovado"
elif media > 5 and media < 7 :
   x = "recuperação"

else : "Aprovado"

print (f"o aluno {nome} tirou media {media:.2f},sua situação {x}.")