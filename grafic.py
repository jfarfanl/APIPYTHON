from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def mostrar_archivo():
    # URL del archivo de texto en el servidor web
    url_archivo = 'https://unlike-travel.000webhostapp.com/medidor/freqss.txt'  # Reemplaza esta URL por la dirección del archivo que desees leer

    # Intentar obtener el contenido del archivo de texto desde la URL
    try:
        response = requests.get(url_archivo)
        if response.status_code == 200:
            contenido = response.text
            return render_template('https://unlike-travel.000webhostapp.com/medidor/lala.html', contenido=contenido)
        else:
            return "Error al obtener el archivo: Código de estado " + str(response.status_code)
    except requests.RequestException as e:
        return "Error de conexión: " + str(e)

if __name__ == '__main__':
    app.run(debug=True)
