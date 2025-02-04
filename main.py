import random

longitud_contrasena = int(input("Introduce la longitud de la contraseña: "))

def gen_pass(longitud_contrasena):
    caracteres = "+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    contraseña_generada = ""
    
    for i in range(longitud_contrasena):
        contraseña_generada += random.choice(caracteres)
    
    return contraseña_generada

# Llamamos a la función y mostramos la contraseña generada
print("Tu contraseña es:", gen_pass(longitud_contrasena))
