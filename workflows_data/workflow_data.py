WORKFLOW_NAME = "Flujo JSON a Email con Trigger"

workflow_data = {
    "name": WORKFLOW_NAME,
    "nodes": [
        {
            "parameters": {},
            "name": "Manual Trigger",
            "type": "n8n-nodes-base.manualTrigger",
            "typeVersion": 1,
            "position": [100, 300]
        },
        {
            "parameters": {
                "url": "https://api.chucknorris.io/jokes/random",
                "responseFormat": "json"
            },
            "name": "HTTP Request",
            "type": "n8n-nodes-base.httpRequest",
            "typeVersion": 1,
            "position": [300, 300],
            "credentials": {
                "smtp": {
                    "id": "lAk5vJR1VeN4pQTS"
                }
            }
        },
        {
            "parameters": {
                "fromEmail": "n8nname@gmail.com",
                "toEmail": "potlitel@gmail.com",
                "subject": "Mensaje desde n8n - Datos JSON recibidos",
                "text": "={{JSON.stringify($json)}}",
            },
            "name": "Send Email",
            "type": "n8n-nodes-base.emailSend",
            "typeVersion": 1,
            "position": [500, 300]
        },
    ],
    "connections": {
        "Manual Trigger": {
            "main": [
                [
                    {
                        "node": "HTTP Request",
                        "type": "main",
                        "index": 0
                    }
                ]
            ]
        },
        "HTTP Request": {
            "main": [
                [
                    {
                        "node": "Send Email",
                        "type": "main",
                        "index": 0
                    }
                ]
            ]
        }
    },
    "settings": {}
}
