# Speedtest

Programa personal para ejecutar en línea de comandos para generar un informe de velocidad de conexión a Internet.

## Requisitos
- Python 3.6 o superior
- Módulos de Python: `speedtest-cli`

## Instalación
1. Clona el repositorio:
    ```bash
    git clone https://github.com/davibern/speedtest.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd speedtest
    ```
3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
4. Ejecuta el script:
    ```bash
    python app.py
    ```

## Uso
El script ejecutará una prueba de velocidad de conexión a Internet y generará un informe por salida estándar del terminal.

```bash
py app.py
Obteniendo lista de servidores...
Advertencia: No se encontró el servidor con ID 68701. Usando el servidor más cercano por defecto.
Comprobando velocidad de descarga...
Comprobando velocidad de subida...

--- Resultados de la comprobaciónd de velocidad ---
Servidor: HTELECOM (Mérida)
Host: h1speedtest.htelecom.es:8080
Ping: 24.20 ms
Descarga: 656.84 Mbps
Subida: 212.15 Mbps
URL: None
-------------------------------------------------
```