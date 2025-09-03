# 🔥 Integración de API de n8n con python.

## ✍️ Descripción

Repositorio demostrativo sobre como utilizar la API de n8n con python scripts. n8n tiene una API que permite a los desarrolladores interactuar con el sistema de automatización de procesos. Permite realizar diversas operaciones, como crear, actualizar y eliminar flujos de trabajo (workflows), así como gestionar credenciales y ejecutar flujos de trabajo de manera programática.

## ✨Características

- Código 100% en Python 🐍.
- Fácil de usar y configurar ⚙️.
- Soporte para múltiples plataformas 🌐.
- Documentación completa 📖.
- PostgresSQL como base de datos para n8n 🐘.
- Python Script que:
  - Se conecta a la api de n8n.
  - Crea un workflow que obtiene datos de una api y los envía vía correo electrónico.
  - Lista todos los workflows existentes.

## 📝 Requisitos Previos

- Asegúrate de tener n8n en funcionamiento y accesible. Puedes utilizar como referencia la siguiente [guía](https://github.com/potlitel/n8n_ELK). 
- Crear una Cuenta de Usuario
  - #### Completar el formulario de configuración inicial:
      ##### 1. Nombre de usuario (administrador)
      ##### 2. Contraseña segura (mínimo 8 caracteres, incluyendo al menos un número y una letra mayúscula)
      ##### 3. Correo electrónico válido para recuperación
- Necesitarás un token de la API de n8n para autenticarte.
  - #### Crear una clave API

    ##### 1. Inicia sesión en n8n.
    ##### 2. Ve a **Configuración > API de n8n**.
    ##### 3. Selecciona **Crear una clave API**.
    ##### 4. Elige una **Etiqueta** y establece un **Tiempo de expiración** para la clave.
    ##### 5. Si estás en un plan empresarial, elige los **Ámbitos** para otorgar a la clave.
    ##### 6. Copia **Mi clave API** y utiliza esta clave para autenticar tus llamadas.


## 📝 Requisitos de Software

### 1. Python
- **Versión**: Python 3.7 o superior

#### Instalación de Python en Windows

##### 1. Descargar el instalador de Python

Visita el sitio web oficial de Python: python.org.
Descarga la última versión de Python 3.x para Windows (asegúrate de elegir entre la versión de 32 bits o 64 bits según tu sistema).

##### 2. Ejecutar el instalador

Abre el archivo descargado (por ejemplo, python-3.x.x-amd64.exe).
Asegúrate de marcar la opción "Add Python to PATH" antes de hacer clic en "Install Now".

##### 3. Personalizar la instalación (opcional)

Si deseas personalizar la instalación, selecciona "Customize installation" y elige las características que deseas incluir, como pip, documentación, etc.

##### 4. Verificar la instalación

Abre el símbolo del sistema (cmd) y ejecuta el siguiente comando para verificar que Python se haya instalado correctamente:

  ```bash
  python --version
  ```

#### Instalación de Python en linux

##### 1: Usar el gestor de paquetes

Abre la terminal y ejecuta el siguiente comando según tu distribución:

  * Ubuntu/Debian:

      ```bash
      sudo apt-get install python3
      ```

  * Fedora:

      ```bash
      sudo dnf install python3
      ```

##### 2: Verificar la instalación

Ejecuta el siguiente comando en la terminal:

   ```bash
  python3 --version
  ```

#### Instalación de Python en Mac

##### 1. Descargar el instalador de Python

Ve a python.org y descarga la versión más reciente de Python para macOS.

##### 2. Ejecutar el instalador

Localiza el archivo descargado en tu carpeta de Descargas y haz doble clic en él para iniciar la instalación.
Sigue las instrucciones en pantalla para completar la instalación.

##### 3. Verificar la instalación

Abre la Terminal y ejecuta:

  ```bash
  python3 --version
  ```

#### Instalación de pip 

##### 1. Verificar si pip está instalado

Después de instalar Python, pip generalmente se instala automáticamente. Verifica su instalación ejecutando:

  ```bash
  pip --version
  ```

##### 2. Instalar pip (si no está instalado)

Si pip no está instalado, puedes instalarlo usando el script get-pip.py. Sigue estos pasos:

###### 1. Descarga el script

  ```bash
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  ```

###### 2. Ejecuta el script

  ```bash
  python get-pip.py
  ```

## 🛠️ Para instalar el proyecto, sigue estos pasos:

1. Clona el repositorio:
   
   ```bash
   git clone https://github.com/potlitel/n8n_ELK.git
   ```

2. Navega al directorio del proyecto:
   
   ```bash
   cd tu_repositorio
   ```

3. Crear un Entorno Virtual (**opcional pero recomendado**): Esto ayuda a manejar las dependencias sin afectar tu instalación global de Python.

   ```bash
   python -m venv venv
   ```

4. Activar el Entorno Virtual:

    * En Windows:

        ```bash
        venv\Scripts\activate
        ```

    * En Linux/Mac

        ```bash
        source venv/bin/activate
        ```
5. Instalar las Dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## 📥 Uso del proyecto

### Configuración de Credenciales SMTP en n8n para Gmail, puede usar también Mailtrap u otro de su preferencia.

Para crear credenciales SMTP en n8n y enviar correos con Gmail, sigue estos pasos clave basados en la documentación oficial de n8n:

### Requisitos Previos

- Debes tener habilitada la verificación en dos pasos en tu cuenta de Gmail.
- Genera una contraseña de aplicación (app password) para usar con n8n (esto es más seguro que usar tu contraseña principal).

### Pasos para Crear la Credencial SMTP en n8n

1. Entra a tu cuenta de Google y habilita la verificación en dos pasos si no lo has hecho ya.
2. Ve a la sección de [**Contraseñas de aplicaciones**](https://myaccount.google.com/apppasswords) de Google.
3. Genera una nueva contraseña para la aplicación, asignándole un nombre identificativo como `n8n credential`.
4. Guarda esta contraseña, pues la necesitarás para la configuración en n8n.

### Configuración en n8n (UI)

1. Ve a la sección de **Credenciales** en n8n.
2. Crea una nueva credencial de tipo **Send Email**.
3. En los campos SMTP pon:
   - **User**: tu dirección de correo Gmail completa (p.ej. `tunombre@gmail.com`)
   - **Password**: la contraseña de aplicación generada en Google.
   - **Host**: `smtp.gmail.com`
   - **Port**: `465` (SSL) o `587` (TLS)
4. Activa el toggle de **SSL/TLS** para el puerto `465` o asegúrate que **STARTTLS** esté activo si usas el puerto `587`.
5. Guarda la credencial.

Esta configuración garantiza que n8n utilice SMTP Gmail de forma segura y autorizada para enviar emails desde tus workflows.

### Ejecución del script **basic_n8n.py**

1. Desde una terminal, diríjase hacia la ubicación del proyecto.

2. Desde el editor de texto de su preferencia, abra el script basic_n8n.py y localice la sección siguiente:

    ```bash
    "credentials": {
                "smtp": {
                    "id": "smtp-credential-id"  # Reemplaza con el ID real de tu credencial SMTP
                }
    ```
    reemplace el valor "id": "smtp-credential-id" por el id de la credencial creada en n8n.

3. Localice además la sección siguiente, correspondiente al nodo '**n8n-nodes-base.sendEmail**'

    ```bash
    "parameters": {
                "fromEmail": "remitente@gmail.com",
                "toEmail": "destinatario@gmail.com",
                "subject": "Mensaje desde n8n - Datos JSON recibidos",
                "text": "={{JSON.stringify($json)}}",
            },
    ```

    y modifique los campos "fromEmail" y "toEmail" según corresponda con su entorno

4. Especifique el valor del API key creado previamente en la variable **N8N_API_KEY**

5. Use el siguiente comando para ejecutar el fichero basic_n8n.py

    ```bash
    python basic_n8n.py
    ```

## Contribuciones

Pull requests are welcome! For any bug reports, please create an issue.




https://www.mdfaisal.com/blog/using-n8n-with-docker-compose
https://felo.ai/search/DQWs9zBhuQC88af9uJ2CKu
https://felo.ai/search/aB9YE9G5tUtEoZ7ZeEH5TG
https://felo.ai/search/9gXDkxfXBaUMZofhKdWqHw
https://felo.ai/search/aB9YE9G5tUtEoZ7ZeEH5TG
https://github.com/naskio/n8n-nodes-python
docker pull naskio/n8n-python

como adapto el script para que copie la image actual de bing hacia mi host local?(Contiene el script suministrado por la IA para descargar el wallpaper actual) https://felo.ai/search/aB9YE9G5tUtEoZ7ZeEH5TG

Ponme un ejemplo práctico en python de interacción con n8n usando la api https://felo.ai/search/9gXDkxfXBaUMZofhKdWqHw

Me gustaría un script en python que interactue con n8n, cree un nuevo workflow que ejecute un sript de python todos los días https://felo.ai/search/9gXDkxfXBaUMZofhKdWqHw

https://www.perplexity.ai/search/pudieras-suministrarme-un-scri-ZOwvRIs5TBS6hSXLGsFy5A

https://www.perplexity.ai/search/tengo-la-siguiente-declaracion-EYr1w5LuRHqXwhNTuX53YA