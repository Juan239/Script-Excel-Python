import os
import pandas as pd
import qrcode

# Inicializar contadores
qr_creados = 0
qr_no_creados = 0

# Leer el archivo de Excel
df = pd.read_excel('nombre del excel')

# Crear la carpeta "qr" si no existe || Definir carpeta para guardar los QR
if not os.path.exists('QR'):
    os.makedirs('QR')

# Iterar sobre cada fila
for index, row in df.iterrows():

        # Extraer los datos de la fila actual || Cambiar por los del documento
        #(Ejemplo)
        nombre = row['Nombre']
        apellido_paterno = row['Apellido Paterno']
        apellido_materno = row['Apellido Materno']
        rut = row['RUT']
        establecimiento = row['Establecimiento']
        curso = row['Curso']

  
        # Crear el texto para el código QR
        texto = f"{nombre} {apellido_paterno} {apellido_materno} {rut} {establecimiento} {curso}"
        
        # Nombre de archivo para el QR
        nombre_archivo = os.path.join('QR', f"{rut}.png")  # Nombre de archivo basado en el RUT

        # Verificar si el archivo de imagen QR ya existe
        if not os.path.exists(nombre_archivo):
            # Crear un objeto QRCode
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )

            # Agregar los datos al objeto QRCode
            qr.add_data(texto)
            qr.make(fit=True)

            # Crear una imagen QR
            img = qr.make_image(fill_color="black", back_color="white")

            # Guardar la imagen QR en la carpeta "qr"
            img.save(nombre_archivo)
            
            
        else:
            # Incrementar contador de QR no creados debido a la existencia del archivo
            qr_no_creados += 1
    
    

# Mostrar resultados
print("Resumen:")
print(f"Total de códigos QR creados: {qr_creados}")
print(f"Códigos QR no creados: {qr_no_creados}")
