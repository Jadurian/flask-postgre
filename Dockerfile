# Imagen base
FROM python:3.9

# Directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY . .

# Instalar dependencias
RUN pip install -r requirements.txt

# Exponer el puerto de Flask
EXPOSE 5000

# Comando de inicio
CMD ["python", "run.py"]
