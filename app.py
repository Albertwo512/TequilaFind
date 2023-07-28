from flask import Flask, render_template, request

app = Flask(__name__)

# Lista para almacenar las respuestas del chat
respuestas_chat = []

@app.route('/', methods=['GET', 'POST'])
def home():
    global respuestas_chat
    
    if request.method == 'POST':
        user_input = request.form['askHuman']
        # Aquí puedes realizar alguna lógica específica con la entrada del usuario
        # Por ejemplo, una simple respuesta automática
        if user_input.lower() == 'hola':
            respuesta = "¡Hola! ¿Cómo estás?"
            respuestas_chat.append(("Tu", user_input))
            respuestas_chat.append(("Agavi", respuesta))
        elif user_input.lower() == 'limpiar':
            respuestas_chat = []
        else:
            respuesta = "Gracias por tu mensaje: " + user_input
            respuestas_chat.append(("Tu", user_input))
            respuestas_chat.append(("Agavi", respuesta))
        
        # Agregar la respuesta del usuario y la respuesta del chat a la lista
        
    if request.method == 'GET':
        respuestas_chat.clear()

    return render_template('index.html', respuestas_chat=respuestas_chat)

if __name__ == "__main__":
    app.run(debug=True)

