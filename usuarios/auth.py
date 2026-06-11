import json
import hashlib

ARQUIVO = "usuarios.json"

def gerar_hash(senha):
	return hashlib.sha256(senha.encode()).hexdigest()

def carregar_usuarios():
	with open(ARQUIVO, "r") as arquivo:
		return json.load(arquivo)

def salvar_usuarios(lista):
	with open(ARQUIVO, "w") as arquivo:
		json.dump(lista, arquivo, indent=4)

def cadastrar_usuario():
	usuarios = carregar_usuarios()

	usuario = input("Usuario: ")
	senha = input("Senha: ")
	perfil = input("Perfil: ")

	novo_usuario = {
		"usuario": usuario,
		"senha": gerar_hash(senha),
		"perfil": perfil
	}

	usuarios.append(novo_usuario)

	salvar_usuarios(usuarios)

	print("Usuario cadastrado com sucesso")

def autenticar_usuario():
	usuarios = carregar_usuarios()

	usuario = input("Usuario: ")
	senha = input("Senha: ")

	hash_senha = gerar_hash(senha)

	for u in usuarios:
		if u["usuario"] == usuario and u["senha"] == hash_senha:
			print("Login realizado com sucesso")
			print("Perfil:", u["perfil"])
			return

	print("Usuario ou senha invalidos")

print("1 - Cadastrar usuario")
print("2 - Fazer login")

opcao = input("Escolha uma opcao: ")

if opcao == "1":
	cadastrar_usuario()

elif opcao == "2":
	autenticar_usuario()
