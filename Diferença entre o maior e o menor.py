print("Cálculo da diferença entre o maior e o menor número, inteiros:")
print("Digite o primeiro número:")
n1 = int(input())

print("Digite o segundo número:")
n2 = int(input())

if n1 > n2:
    diferença = n1 - n2
    print("A diferença entre o maior e o menor número, sabendo que" , n1 , "é o maior número, resulta em:" ,diferença)
else:
    diferença = n2 - n1
    print("A diferença entre o maior e o menor número, sabendo que" , n2 , "é o maior número, resulta em:" ,diferença)
