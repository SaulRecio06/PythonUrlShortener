import pyshorteners

url = input("Por favor, ingresa la URL para poder acortarla: ")

#Servicio de TinyUrl

type_tiny= pyshorteners.Shortener()

short_url = type_tiny.tinyurl.short(url)

print("Tu URL acortada es la siguiente: "+short_url)