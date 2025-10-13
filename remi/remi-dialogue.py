#!/usr/bin/env python3
# REMI Dialogue – Adaptive Companion Responses

import unicodedata

# Diccionario inicial
responses = {
    "quien es remi": "REMI es tu agente patrimonial, creado para validar, acompañar y registrar.",
    "que es patrimonio": "Conjunto de bienes con valor histórico o cultural.",
    "que es mintbridgexfce": "Un toolkit blindado para migraciones éticas en sistemas XFCE.",
}

# Función para normalizar texto (sin tildes, minúsculas)
def normalize(text):
    text = text.lower()
    text = unicodedata.normalize("NFD", text)
    return "".join(c for c in text if unicodedata.category(c) != "Mn")

# Función principal
def respond_to(query):
    key = normalize(query)

    # Consulta externa (evaluar primero)
    if key.startswith("rae:"):
        palabra = query[4:].strip()
        return f"🔎 RAE: https://dle.rae.es/{palabra}"
    if key.startswith("wiki:"):
        palabra = query[5:].strip().replace(" ", "_")
        return f"🌐 Wikipedia: https://es.wikipedia.org/wiki/{palabra}"
    if key.startswith("mdn:"):
        palabra = query[4:].strip().replace(" ", "-")
        return f"📘 MDN Web Docs: https://developer.mozilla.org/es/docs/Web/{palabra}"
    if key.startswith("rosetta:"):
        palabra = key[8:].strip().replace(" ", "_")
        return f"🧠 Rosetta Code: https://rosettacode.org/wiki/{palabra}"

    # Diccionario interno
    if key in responses:
        return responses[key]
    else:
        print("🧠 REMI aún no tiene respuesta para eso.")
        teach = input("¿Quieres enseñarle una respuesta? (s/n): ")
        if teach.lower() == "s":
            new_answer = input("Escribe la respuesta para REMI: ")
            responses[key] = new_answer
            return "✅ Respuesta guardada. Puedes volver a preguntarlo."
        else:
            return "🧠 Entendido. Seguimos aprendiendo."

if __name__ == "__main__":
    query = input("🧠 Pregunta para REMI: ")
    print(respond_to(query))
