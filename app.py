import speedtest


def run_speed_test():
    st = speedtest.Speedtest(secure=True)
    st.get_servers([68701])

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
    run_speed_test()
