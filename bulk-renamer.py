import os
import sys

def rename_txt_files(directory):
    """Renombra todos los archivos .txt en el directorio especificado agregando el prefijo 'archivado-'."""
    
    # Verificamos si el directorio existe
    if not os.path.isdir(directory):
        print(f"Error: El directorio '{directory}' no existe.")
        return
    
    # Iteramos sobre todos los archivos en el directorio
    for filename in os.listdir(directory):
        # Comprobamos si el archivo tiene extensión .txt
        if filename.endswith('.txt'):
            # Construimos el nuevo nombre de archivo
            new_name = f'archivado-{filename}'
            # Construimos la ruta completa para el archivo original y el nuevo archivo
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_name)
            # Renombramos el archivo
            os.rename(old_file, new_file)
            print(f'Renombrado: {old_file} -> {new_file}')

if __name__ == '__main__':
    # Verificamos que se ha proporcionado un argumento
    if len(sys.argv) != 2:
        print("Uso: python rename_txt_files.py <directorio>")
        sys.exit(1)
    
    # Obtenemos el directorio del argumento
    directory = sys.argv[1]
    
    # Llamamos a la función para renombrar los archivos
    rename_txt_files(directory)