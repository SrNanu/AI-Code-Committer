import json
import os

def validar_json(ruta_archivo):
    """
    Lee un archivo JSON desde una ruta y verifica si su contenido es un JSON válido.
    
    Args:
        ruta_archivo (str): La ruta del archivo JSON a leer.
    
    Returns:
        bool: True si el archivo es un JSON válido, False en caso contrario.
    
    Raises:
        FileNotFoundError: Si el archivo no existe.
        json.JSONDecodeError: Si el contenido del archivo no es un JSON válido.
    """
    
    # Verifica si el archivo existe
    if not os.path.isfile(ruta_archivo):
        raise FileNotFoundError(f"El archivo no existe: {ruta_archivo}")
    
    try:
        # Intenta abrir y cargar el contenido del archivo JSON
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            json.loads(archivo.read())
        return True  # Si se carga sin errores, el JSON es válido
    except json.JSONDecodeError as e:
        return False  # Si hay un error de decodificación, el JSON no es válido