# Enviar solicitud para crear el flujo
from workflows_data.workflow_data import workflow_data
import requests
import json

# Configura la URL de tu instancia de n8n
N8N_API_URL = 'http://localhost:5678'  # Cambia esto si tu n8n está en otra dirección
N8N_API_KEY  = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiYjQ1YTIzOC02YjYxLTRlZDAtYjhlNi02NzIwMWM5ZWIyZDIiLCJpc3MiOiJuOG4iLCJhdWQiOiJwdWJsaWMtYXBpIiwiaWF0IjoxNzU2ODQ3MjI1LCJleHAiOjE3NTkzNzc2MDB9.JbkdNn8X-UaqnFQkHzQEv-zicGX5zv78JYDHDokUu7o'  # Reemplaza con tu token de API

def CreateBasicWorkflow(N8N_API_URL, headers)-> None:
    # Enviar solicitud para crear el flujo
    response = requests.post(f'{N8N_API_URL}/api/v1/workflows', headers=headers, data=json.dumps(workflow_data))

    if response.status_code == 200:
        workflow_id = response.json()['id']
        print(f'Flujo creado con ID: {workflow_id}')
        
        # Paso 2: Activar workflow
        activate_response = requests.post(f"{N8N_API_URL}/api/v1/workflows/{workflow_id}/activate", headers=headers)
        if activate_response.status_code != 204:
            print(f"Error al activar workflow: {activate_response.text}")
            exit(1)
        print("Workflow activado")

        # Paso 3: Ejecutar el flujo
        execute_response = requests.post(f'{N8N_API_URL}/api/v1/workflows/{workflow_id}/execute', headers=headers)

        if execute_response.status_code == 200:
            print('Flujo ejecutado correctamente.')
        else:
            print('Error al ejecutar el flujo:', execute_response.text)
    else:
        print('Error al crear el flujo:', response.text)