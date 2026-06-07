import hashlib

def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

senha = "teste123"

print("Senha original:", senha)
print("Hash:", gerar_hash(senha))
