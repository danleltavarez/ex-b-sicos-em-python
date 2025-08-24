#esse codigo mostra se a nota do aluno foi o suficiente para aprovado
# media coleta a variavel da media das notas
nota1=int(input("digite sua nota da primeira prova: "))
nota2=int(input("digite sua nota da segunda prova: "))
nota3=int(input("digite sua nota da terceira prova:" ))
media = (nota1 + nota2 + nota3) / 3;
if media >= 7:
    print("parabens você foi aprovado! ")
else:
    print("infelizmente você foi reprovado")
