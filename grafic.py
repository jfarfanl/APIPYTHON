from flask import Flask, render_template
import matplotlib.pyplot as plt
import mysql.connector

app = Flask(__name__)

# Conexión a la base de datos MySQL
conn = mysql.connector.connect(
    host='https://databases-auth.000webhost.com',
    user='id20857986_root',
    password='ddmnhn_4768252I',
    database='id20857986_medidor1'
)


@app.route('/')
def index():
    cursor = conn.cursor()
    cursor.execute("SELECT id, RMSv1 FROM rms ORDER BY id DESC LIMIT 10")
    data = cursor.fetchall()

    # Procesamiento de los datos para graficar
    x = [row[0] for row in data]
    y = [row[1] for row in data]

    # Crear el gráfico de barras con Matplotlib
    plt.figure(figsize=(10, 6))
    plt.bar(x, y, color='blue')
    plt.title('Últimos datos en Gráfico de Barras')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Guardar la imagen del gráfico en un archivo
    nombre_archivo = 'static/grafico_barras.png'  # Ruta donde se guardará la imagen
    plt.savefig(nombre_archivo)

    cursor.close()
    return render_template('index.html', grafico=nombre_archivo)

if __name__ == '__main__':
    app.run(debug=True)
