def output (v):
    total=0
    a=v
    for i in range (25):
        v+=0.1
        total+=v

    suma=total+a #para calcular con ambos limites incluidos
    print ("Suma: ")
    print (round (suma,2))
    print ("Promedio: ")
    print (round (suma/25,2))
        
        


v1=0 #inferior
v2=1 #superior
rpta=0

#no sale del bucle hasta que cumpla los requerimientos:
while rpta !=2.5 or v1>v2 or (v1<1 and v2>5000):
    print("Ingresa valores ")
    v1= float(input("ingresa primer valor: "))
    v2= float(input("ingresa segundo valor: ")) 
    rpta=v2-v1

output(v1) #solo es necesario el nro inferior, ya esta validado que haya 25 nros.
