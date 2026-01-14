# 1. Usar una imagen base ligera de Python
FROM python:3.9-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Instalar la dependencia necesaria
RUN pip install flask

# 4. Copiar nuestro código al contenedor
COPY app.py .

# 5. Exponer el puerto donde corre Flask
EXPOSE 5000

# 6. Comando para ejecutar la aplicación
CMD ["python", "app.py"]