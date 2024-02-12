import os
import shutil

# Crear la carpeta Proyecto111
proyecto_folder = "Proyecto111"
os.makedirs(proyecto_folder, exist_ok=True)

# Abrir Visual Studio Code en la carpeta Proyecto111
os.system("code " + proyecto_folder)

# Definir las rutas de origen y destino
from_dir = os.path.join(os.path.expanduser("~"), "Descargas")
to_dir = os.path.join(os.path.expanduser("~"), "Documentos_Archivos")

# Obtener la lista de archivos en la carpeta de origen
list_of_files = os.listdir(from_dir)
print("Archivos en la carpeta de origen:")
print(list_of_files)

# Recorrer la lista de archivos
for filename in list_of_files:
    # Obtener el nombre y la extensión del archivo
    name, extension = os.path.splitext(filename)
    
    # Comprobar si la extensión está en blanco
    if not extension.strip():
        continue  # Saltar al siguiente archivo si la extensión está en blanco
    
    # Lista de extensiones permitidas
    allowed_extensions = ['.txt', '.doc', '.docx', '.pdf']
    
    # Comprobar si la extensión está en la lista permitida
    if extension in allowed_extensions:
        # Crear las rutas de directorio
        path1 = os.path.join(from_dir, filename)
        path2 = os.path.join(to_dir, "Document_Files")
        path3 = os.path.join(path2, filename)
        
        # Comprobar si la ruta de destino existe
        if os.path.exists(path2):
            print(f"Moviendo {filename} a {path3}")
            shutil.move(path1, path3)
        else:
            # Crear la carpeta de destino y luego mover el archivo
            os.makedirs(path2, exist_ok=True)
            print(f"Creada carpeta {path2}, moviendo {filename} a {path3}")
            shutil.move(path1, path3)

# Imprimir mensaje de finalización
print("Proceso de mover archivos completado.")
