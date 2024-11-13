import re
 
 
 
num1 = int(input ("digite um numero: "))
 
num2 = int(input ("digite um numero: "))
 
num3 = int(input ("digite um numero: "))
 
 
 
# padrao = r"^[0-9]+$"
# numero_valido = re.match(padrao,num1,num2,num3) is not None
# if(numero_valido==False):
#     print("escrita invalida! por favor digite apenas numeros")
   
   
   
if num1 > num2:
    if num1 > num3:
        print("o primeiro numero é o maior: ", num1)
    else:
        print('o terceiro numero é o maior', num3)
       
elif num2 > num3:
    if num2 > num1:
        print("o segundo numero é o maior: ", num2)
    else:
        print('o primeiro numero é o maior', num1)
       
elif num3 > num1:
    if num3 > num2:
        print("o terceiro numero é o maior: ", num3)
    else:
        print('o segundo numero é o maior', num2)
       
else:
    print("você digitou dois ou mais numeros iguais, tente novamente")
 