#esse codigo mostra se o numero escolhido pelo usuario é par ou impar
numero =int(input("digite um numero:"))
print("o numero escolhido foi:", numero)
if numero % 2 == 0:
    print("o numero e par")
else:
    print("o numero e impar")