#Definir esto dentro de otra function
import requests

def ListExistingWorkflows(N8N_API_URL, headers)-> None:
    try:
    # Realiza una solicitud GET a la API de n8n para obtener workflows
        response = requests.get(f'{N8N_API_URL}/api/v1/workflows', headers=headers)
    # Imprime el contenido de la respuesta
        print("Contenido de la respuesta:", response.text)
    
    # Verifica la respuesta
        response.raise_for_status()  # Lanza un error si la respuesta no es 200

        workflows = response.json()
    
        if workflows:
            print("Workflows obtenidos exitosamente:")
            print(workflows)
        else:
            print("No se encontraron workflows.")

    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error en la solicitud: {req_err}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")