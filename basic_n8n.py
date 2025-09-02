from workflows_utils.CreateBasicWorkflow import CreateBasicWorkflow
from workflows_utils.ListExistingsWorkflows import ListExistingWorkflows

# Configura la URL de tu instancia de n8n
N8N_API_URL = 'http://localhost:5678'  # Cambia esto si tu n8n está en otra dirección
N8N_API_KEY  = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiYjQ1YTIzOC02YjYxLTRlZDAtYjhlNi02NzIwMWM5ZWIyZDIiLCJpc3MiOiJuOG4iLCJhdWQiOiJwdWJsaWMtYXBpIiwiaWF0IjoxNzU2ODQ3MjI1LCJleHAiOjE3NTkzNzc2MDB9.JbkdNn8X-UaqnFQkHzQEv-zicGX5zv78JYDHDokUu7o'  # Reemplaza con tu token de API

# Configura los headers para la autenticación básica
headers = {
    'X-N8N-API-KEY': N8N_API_KEY,
    'Content-Type': 'application/json'
}


CreateBasicWorkflow(N8N_API_URL, headers)

ListExistingWorkflows(N8N_API_URL, headers)
