def classificar_consumo():
    print("=== SISTEMA DE CONSCIENTIZAÇÃO AMBIENTAL - SANEAMENTO ===")

    tipo_imovel = input("Digite o tipo de imóvel (comercial, casa ou apartamento): ").strip().lower()

    while tipo_imovel not in ["comercial", "casa", "apartamento"]:
        print("Tipo inválido. Por favor, digite 'comercial', 'casa' ou 'apartamento'.")
        tipo_imovel = input("Digite o tipo de imóvel (comercial, casa ou apartamento): ").strip().lower()

    try:
        consumo = float(input("Digite o consumo mensal de água em metros cúbicos (m³): "))
    except ValueError:
        print("Valor de consumo inválido. Por favor, insira um número decimal.")
        return

    if tipo_imovel == "comercial":
        print("\nTarifa comercial aplicada – consulte o plano corporativo.")
    elif tipo_imovel == "apartamento" and consumo < 10:
        print("\nConsumo econômico – excelente controle de água!")
    elif tipo_imovel == "apartamento" or (tipo_imovel == "casa" and consumo <= 25):
        print("\nConsumo moderado – dentro do padrão residencial.")
    else:
        print("\nConsumo excessivo – adote medidas de economia e verifique vazamentos.")

if __name__ == "__main__":
    classificar_consumo()