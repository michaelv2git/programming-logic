variable = "a"
edad = 17
x = 1

# Condicionales o selección

if type(variable) is str:
    print("Si es")
else:
    print("No es")

if edad > 18:
    print("Si")
elif edad == 18:
    print("Exacto")
else:
    print("No")

# Iterativas o bucles

for i in range(1,11):
    print(i)

while(x<=10):
    print(x)
    x+=1

# Salida y excepción

try:
    numero1 = int(input("Ponga un número: "))
    numero2 = int(input("Ponga un segundo: "))

    resultado = numero1 * numero2
    print(resultado)
except:
    print("Son numeros pedazo de mongolico :D")
finally:
    print("Esta vaina va a funcionar siempre Ricardo :D")

# try: sirve para decirle a un bloque de codigo que intente ejecutar ese codigo, que si salta error, ejecute el except.
# Entonces, si el código funciona, la excepción finally se ejecutará siempre.