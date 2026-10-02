class Reserva:
    # 1. Método para criar a reserva
    @staticmethod
    def realizar_reserva(banco, id_cliente, id_quarto, data, horario, num_pessoas):
        # ... (seu código de INSERT e UPDATE) ...
        pass

    # 2. Método para o Check-out
    @staticmethod
    def realizar_checkout(banco, num_quarto):
        # ... (seu código de liberação) ...
        pass

    # 3. O MÉTODO DE CONSULTA DETALHADA (Coloque aqui)
    @staticmethod
    def consultar_reserva_detalhada(banco, cpf):
        resultados = banco.buscar_reserva_detalhada(cpf)

        if resultados:
            res = resultados[0]
            print(f"\n📋 --- RESERVA ENCONTRADA ---")
            print(f"Hóspede: {res[0]} | Quarto: {res[1]} ({res[2]})")
            print(f"Data: {res[3]} às {res[4]}h | Pessoas: {res[5]}")
        else:
            print("\n❌ Nenhuma reserva encontrada.")