import speedtest


def run_speed_test(server_id=None):
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


if __name__ == "__main__":
    digi_id: int = 68701
    run_speed_test(digi_id)
