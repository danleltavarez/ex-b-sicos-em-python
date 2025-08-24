    # esse codigo mostra a categoria da idade
    # idade coleta a variavel de um numero inteiro
idade =int(input("digite a sua idade: "))
    # verifica a categoria da idade
    # se a idade for menor ou igual a 12 vc e uma criança
if idade <= 12:
    print("você é uma criança")
    # se a idade for igual ou maior que 13 e menor ou igual a 17 vc e um adolescente
elif idade >= 13 and idade <= 17:
    print("adolecente")
    # se a idade for igual ou maior que 18 e menor ou igual a 59 vc e um adulto
elif idade >=18 and idade <= 59:
    print("adulto")
    # se a idade for igual ou maior que 60 vc e um idoso
elif idade >= 60:
    print("idoso")
