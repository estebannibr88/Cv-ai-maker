import openai

# Configura la API de OpenAI
openai.api_key = "
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"  # Reemplaza con tu clave de OpenAI

def obtener_trabajos_anteriores():
    print("Por favor, ingresa tus puestos de trabajo anteriores.")
    print("Nota: Describe tus roles sin mencionar años trabajados.")
    trabajos = []
    while True:
        trabajo = input("Ingresa un puesto de trabajo anterior (o escribe 'fin' para terminar): ")
        if trabajo.lower() == 'fin':
            break
        descripcion = input("Describe brevemente tus habilidades o responsabilidades en ese puesto: ")
        trabajos.append({"puesto": trabajo, "descripcion": descripcion})
    return trabajos

def obtener_descripcion_puesto():
    print("\nAhora, ingresa la descripción del puesto al que quieres postularte:")
    descripcion_puesto = input("Descripción del puesto: ")
    return descripcion_puesto

def generar_cv(trabajos_anteriores, descripcion_puesto):
    prompt = f"""Genera un currículum vitae adaptado a la siguiente descripción de puesto:
    '{descripcion_puesto}'
    
    Utiliza la experiencia previa proporcionada a continuación para amoldar el CV de manera sutil y profesional, evitando frases obvias y centrando el contenido en lo que el reclutador busca, sin detalles innecesarios:

    Experiencia anterior:
    """
    for trabajo in trabajos_anteriores:
        prompt += f"- {trabajo['puesto']}: {trabajo['descripcion']}\n"

    prompt += "\nEl CV debe ser breve, conciso y centrado en las habilidades y logros relacionados con el puesto solicitado."

    # Llamada a la IA para generar el CV
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=250,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )

    cv_generado = response.choices[0].text.strip()
    return cv_generado

def main():
    print("Generador de CV Adaptado")
    trabajos_anteriores = obtener_trabajos_anteriores()
    descripcion_puesto = obtener_descripcion_puesto()
    cv = generar_cv(trabajos_anteriores, descripcion_puesto)
    
    print("\n--- CV Generado ---\n")
    print(cv)

# Ejecuta el programa
if __name__ == "__main__":
    main()
