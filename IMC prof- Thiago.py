print("calcular o imc?")
nome=input("Digite seu nome :")
idade=input("Digite sua idade :")
altura=float(input("Digite seu altura :"))
peso=float(input("Digite sua peso :"))
imc= peso/altura**2
print (imc)
if imc<18.5:
    print('magreza')
elif imc<24.9:
    print("peso normal")
elif imc <29.9:
    print ( "sobre peso" )
elif imc < 34.9:
    print ( "Obesidade grau 1" )
elif imc < 39.9:
    print ( "Obesidade grau 2" )
elif imc >40:
    print ( "obsidade grau 3 ou Mórbida" )




