import time
import qrcode
import requests
import uuid

def gerar_codigo_pix(conta, valor):
    """
    Gera um payload PIX simplificado, incluindo um transaction_id para identificação única da transação.
    Em um cenário real, esse payload deverá seguir o padrão do Banco Central.
    """
    transaction_id = str(uuid.uuid4())
    payload = f"PIX:{conta}:{valor:.2f}:{transaction_id}"
    return payload, transaction_id

def salvar_qr_code(dado, arquivo="pix_qr.png"):
    """
    Gera e salva o QR Code contendo o payload PIX.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(dado)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(arquivo)
    print(f"QR Code gerado e salvo em: {arquivo}")

def verificar_pagamento_automatico(transaction_id):
    """
    Verifica automaticamente o status do pagamento através de uma chamada à API do sistema PIX.
    A função realiza polling, consultando periodicamente o status da transação no endpoint.
    Retorna 1 se a API confirmar que o pagamento foi contabilizado, 0 caso contrário.
    """
    tempo_maximo = 120   # tempo total máximo de verificação (em segundos)
    intervalo = 5       # intervalo entre verificações (em segundos)
    tempo_total = 0

    # Endpoint fictício da API do sistema PIX para verificação do status da transação.
    api_endpoint = "https://api.sistemapix.com/transaction/status"  

    while tempo_total < tempo_maximo:
        print("Verificando status do pagamento...")
        try:
            # Realiza uma requisição GET passando o transaction_id como parâmetro.
            response = requests.get(api_endpoint, params={"transaction_id": transaction_id})
            if response.status_code == 200:
                data = response.json()
                # Se o status retornado for "confirmado", o pagamento foi contabilizado.
                if data.get("status") == "confirmado":
                    print("Pagamento contabilizado no sistema.")
                    return 1
            else:
                print(f"Erro na requisição: HTTP {response.status_code}")
        except Exception as e:
            print(f"Erro ao acessar a API: {e}")
        time.sleep(intervalo)
        tempo_total += intervalo

    print("Tempo de verificação esgotado, pagamento não confirmado.")
    return 0

def autenticador_pix(conta, valor):
    """
    Função principal que gera o QR Code PIX, registra a transação e aguarda a confirmação automática do pagamento.
    Retorna 1 somente se a API confirmar que o pagamento foi contabilizado no sistema PIX.
    """
    payload, transaction_id = gerar_codigo_pix(conta, valor)
    salvar_qr_code(payload)
    print("Aguardando confirmação automática do pagamento...")
    status = verificar_pagamento_automatico(transaction_id)
    return status

# Exemplo de uso:
if __name__ == "__main__":
    conta = "28999659388"  # Pode ser um número de telefone ou outra chave PIX
    valor = 1.00
    resultado = autenticador_pix(conta, valor)
    if resultado:
        print("Pagamento confirmado!")
    else:
        print("Pagamento não confirmado.")
