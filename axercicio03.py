sexo =  input("Digite F para femenino e M para masculino:")
if sexo=="f" or sexo =="F":
    print("femenino")
elif sexo== "m" or sexo == "M" :
    print ("Masculino")

else:
    print("Sexo invalido")   
    # comando lower()converte as letras para minusculas
    # comando upper() converte as letras para maiusculas

    sexo = sexo.lower
    if sexo == "f":
        print("Femenino")
    elif sexo =="n" :
        print("Masculino")
    else:
        print("Sexo invalido")        