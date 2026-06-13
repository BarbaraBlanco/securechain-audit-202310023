import json
import hashlib
from datetime import datetime

ARQUIVO = "chain.json"

def calcular_hash(dados):
    return hashlib.sha256(dados.encode()).hexdigest()

def carregar_chain():
    with open(ARQUIVO, "r") as arquivo:
        return json.load(arquivo)

def salvar_chain(chain):
    with open(ARQUIVO, "w") as arquivo:
        json.dump(chain, arquivo, indent=4)

def criar_bloco():
    chain = carregar_chain()

    dados = input("Digite os dados do bloco: ")

    if len(chain) == 0:
        hash_anterior = "0"
    else:
        hash_anterior = chain[-1]["hash"]

    conteudo = dados + hash_anterior

    bloco = {
        "indice": len(chain) + 1,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "dados": dados,
        "hash_anterior": hash_anterior,
        "hash": calcular_hash(conteudo)
    }

    chain.append(bloco)

    salvar_chain(chain)

    print("Bloco criado com sucesso.")

def validar_chain():
    chain = carregar_chain()

    for i in range(1, len(chain)):
        bloco_atual = chain[i]
        bloco_anterior = chain[i - 1]

        if bloco_atual["hash_anterior"] != bloco_anterior["hash"]:
            print("Blockchain invalida!")
            return

    print("Blockchain valida!")

print("1 - Criar bloco")
print("2 - Validar blockchain")

opcao = input("Escolha uma opcao: ")

if opcao == "1":
    criar_bloco()

elif opcao == "2":
    validar_chain()
