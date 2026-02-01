import requests
import os

def subir_a_filelu(ruta_archivo, api_key):
    # La URL del endpoint de la API de FileLu (basado en su documentación estándar)
    url = "https://filelu.com/api/upload/server"
    
    # Verificamos si el archivo existe localmente
    if not os.path.exists(ruta_archivo):
        print("Error: El archivo no existe.")
        return

    # Parámetros necesarios para la API
    # Nota: Usamos la API Key para autenticarnos de forma segura
    params = {
        'api_key': api_key
    }

    try:
        with open(ruta_archivo, 'rb') as f:
            files = {'file': f}
            print(f"Subiendo {ruta_archivo}...")
            response = requests.post(url, params=params, files=files)
            
            if response.status_code == 200:
                print("¡Éxito! El archivo ha sido subido.")
                print("Respuesta del servidor:", response.json())
            else:
                print(f"Error en la subida. Código: {response.status_code}")
                
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Ejemplo de uso (esto es lo que el usuario ejecutaría)
if __name__ == "__main__":
    MI_API_KEY = "TU_API_KEY_AQUI"  # Aquí va la clave que te da FileLu
    ARCHIVO = "mi_foto.jpg"          # El archivo que quieras probar
    subir_a_filelu(ARCHIVO, MI_API_KEY)