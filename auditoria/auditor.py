from datetime import datetime

ARQUIVO_LOG = "relatorios/eventos.log"

def registrar_evento():
    evento = input("Descreva o evento: ")

    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    linha = f"{data_hora} - {evento}\n"

    with open(ARQUIVO_LOG, "a") as arquivo:
        arquivo.write(linha)

    print("Evento registrado com sucesso.")

def listar_eventos():
    with open(ARQUIVO_LOG, "r") as arquivo:
        print("\n=== EVENTOS REGISTRADOS ===\n")
        print(arquivo.read())

def contar_eventos():
    with open(ARQUIVO_LOG, "r") as arquivo:
        linhas = arquivo.readlines()

    print("Total de eventos:", len(linhas))

print("1 - Registrar evento")
print("2 - Listar eventos")
print("3 - Contar eventos")

opcao = input("Escolha uma opcao: ")

if opcao == "1":
    registrar_evento()

elif opcao == "2":
    listar_eventos()

elif opcao == "3":
    contar_eventos()
