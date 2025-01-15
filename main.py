import random

caracteres = "+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud_contraseña = int(input("Introduce la longitud de la contraseña: "))
contraseña_generada = ""
for _ in range(longitud_contraseña):
    contraseña_generada += random.choice(caracteres)
print("Tu contraseña es", contraseña_generada)
