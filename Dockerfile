# Usamos una imagen base de Python oficial
FROM python:3.9

# Establece un directorio de trabajo para contener los archivos de la aplicación
WORKDIR /app

# Copia el archivo de dependencias en el contenedor
COPY requirements.txt /app/

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código fuente del proyecto en el contenedor
COPY . /app/

# Expone el puerto que usa la aplicación
EXPOSE 8000

# Define el comando que ejecuta la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
