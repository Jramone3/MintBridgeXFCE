#!/usr/bin/env python3
# REMI Dialogue – Adaptive Companion Responses

import unicodedata
from langdetect import detect

# Función para normalizar texto (sin tildes, minúsculas)
def normalize(text):
    text = text.lower()
    text = unicodedata.normalize("NFD", text)
    return "".join(c for c in text if unicodedata.category(c) != "Mn")

# Función para detectar idioma
import langid

def detectar_idioma(texto):
    try:
        idioma, _ = langid.classify(texto)
        return idioma
    except:
        return "es"

# Diccionario inicial
responses = {
    "quien es remi": "REMI es tu agente patrimonial, creado para validar, acompañar y documentar cada fase técnica con respeto.",
    "que es patrimonio": "Conjunto de bienes con valor histórico o cultural que merecen ser protegidos y documentados.",
    "que es mintbridgexfce": "Un toolkit blindado para migraciones éticas en Linux Mint con enfoque patrimonial y reproducible.",
    "saludo": "saludo",
    "hello": "saludo",
    "bonjour": "saludo"
}

# Función principal de respuesta
def respond_to(query):
    idioma = detectar_idioma(query)
    key = normalize(query)

    if any(palabra in key for palabra in [
        "saludo", "saludar", "saludarme", "saludos",
        "hello", "hi", "greet", "greeting", "greetings",
        "bonjour", "salut", "saluer", "salutation"
    ]):
        if idioma == "en":
            return "🧠 REMI says hello!"
        elif idioma == "fr":
            return "🧠 REMI vous salue !"
        else:
            return "🧠 REMI te saluda."

    return "REMI no reconoce esa consulta aún."

# Interfaz interactiva
if __name__ == "__main__":
    print("🧠 REMI activo. Escribe tu consulta (Ctrl+C para salir):")
    while True:
        try:
            entrada = input("> ")
            respuesta = respond_to(entrada)
            print(respuesta)
        except KeyboardInterrupt:
            print("\n🔚 Sesión finalizada.")
            break
