salario = float(input("Digite o seu salario"))

valor_aumento = 0
novo_salario = 0 
if salario <=200:
    valor_aumento = salario * 20/100
    novo_salario = salario = valor_aumento
    print(" O seu salario atual é " +str(salario)+ "20% de aumento. O valor do aumento é "+str(valor_aumento)+ " e o  novo salario é " +str(novo_salario))

elif salario < 700:
    valor_aumento = salario *15 /100 
    novo_salario = salario + valor_aumento
    print( "O seu salrio atual é " +str(salario)+" 15% de aumento. O valor  do aumento é "+str(valor_aumento)+" eo novo salario é "+str(novo_salario))    

    
elif salario < 1500:
    valor_aumento = salario * 10 /100 
    novo_salario = salario + valor_aumento
    print("O seu salrio atual é " +str(salario)+" 15% de aumento. O valor  do aumento é "+str(valor_aumento)+" eo novo salario é "+str(novo_salario))    


else:
    valor_aumento = salario * 5 /100 
    novo_salario = salario + valor_aumento
    print("O seu salrio atual é "+str(salario)+" 15% de aumento. O valor  do aumento é "+str(valor_aumento)+" eo novo salario é "+str(novo_salario))  
         
         