periodo = input("Digite M-Matutino, V-vespertno ou N-Noturno ")
periodo = periodo.lower()

if periodo == "m":
    print("Bom dia")
elif periodo == "v":
    print("Boa tarde!")
elif periodo == "n":
    print("Boa noite!")    
          
else: 
 print("Valor invalido")         