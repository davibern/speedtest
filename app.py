import speedtest
import datetime
import json


def run_speed_test(server_id=None, export_to_json=True):
    st = speedtest.Speedtest(secure=True)

    print("Obteniendo lista de servidores...")
    st.get_servers()

    if server_id:
        selected_server = None
        for server_type, servers in st.servers.items():
            for s in servers:
                if str(s['id']) == str(server_id):
                    selected_server = s
                    break
                if selected_server:
                    break

        if selected_server:
            st.closest = [selected_server]
            print(f"Servidor seleccionado manualmente: {selected_server['sponsor']} ({selected_server['name']})")
        else:
            print(f"Advertencia: No se encontró el servidor con ID {server_id}. Usando el servidor más cercano por defecto.")
            st.get_best_server()
    else:
        print("Seleccionando el mejor servidor...")
        st.get_best_server()

    print("Comprobando velocidad de descarga...")
    st.download()

    print("Comprobando velocidad de subida...")
    st.upload()

    result = st.results.dict()

    print("\n--- Resultados de la comprobaciónd de velocidad ---")
    print(f"Servidor: {result['server']['sponsor']} ({result['server']['name']})")
    print(f"Host: {result['server']['host']}")
    print(f"Ping: {result['ping']:.2f} ms")
    print(f"Descarga: {result['download'] / 1_000_000:.2f} Mbps")
    print(f"Subida: {result['upload'] / 1_000_000:.2f} Mbps")
    print(f"URL: {result['share']}")
    print("-------------------------------------------------")

    if export_to_json:
        export_results_to_json(result)


def export_results_to_json(data):
    """
    Exporta los resultados de la prueba de velocidad a un archivo JSON.

    Args:
        data (dict): Los resultados de la prueba de velocidad.
    """

    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"speedtest_results_{timestamp}.json"

        with open(filename, 'w') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print(f"Resultados exportados a {filename}")
    except Exception as e:
        print(f"Error al exportar los resultados a JSON: {e}")


if __name__ == "__main__":
    digi_id: int = 69648
    run_speed_test(digi_id, False)
