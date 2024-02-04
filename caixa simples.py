
//Gostaria de saber quais notas vou sacar no caixa??
n1 = int(input('digete o seu Saldo'))
c = n1//100
n1 = n1%100
cc =n1//50
d = n1//10
n1 = n1%10
n1 = n1%50
u = n1//1
n1=n1%1
print(f'o seu saldo podera ser sacado {c} notas de cem resta ')
print(f' {d} notas de 10')
print(f'agora com seu saldo podera sacado com {cc} com notas de 50 e resta ')
print(f'e por ultimo seu saldo podera saca {u} com notas de um e resta')
