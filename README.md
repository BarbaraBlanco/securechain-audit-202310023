# securechain-audit-202310023

# SecureChain Audit

Projeto desenvolvido para a disciplina de Seguranca de sistemas computacionais, com o objetivo de implementar mecanismos de controle de acesso, auditoria, blockchain e backup automatizado em ambiente Debian.

## Objetivo

O sistema SecureChain Audit foi criado para simular uma solução de segurança voltada ao monitoramento de eventos, autenticação de usuários e armazenamento seguro de registros utilizando conceitos de blockchain.

## Estrutura do Projeto

securechain-audit-202310023/

├── auditoria/
│   ├── auditor.py
│   └── relatorios/
│       └── eventos.log
│
├── backup/
│   └── backup.sh
│
├── blockchain/
│   ├── blockchain.py
│   └── chain.json
│
├── usuarios/
│   ├── auth.py
│   └── usuarios.json
│
└── README.md

# Funcionalidades Implementadas

## RF01 - Gerenciamento de Usuários Linux

* Criação de usuários do sistema.
* Criação de grupos.
* Associação de usuários aos grupos.
* Verificação de permissões.

## RF02 - Autenticação de Usuários

* Cadastro de usuários.
* Login no sistema.
* Armazenamento de senhas utilizando SHA-256.
* Persistência dos dados em arquivo JSON.

## RF03 - Blockchain

* Criação de blocos.
* Registro de data e hora.
* Encadeamento por hash.
* Validação da integridade da cadeia.
* Armazenamento em arquivo JSON.

## RF04 - Auditoria

* Registro de eventos.
* Armazenamento em arquivo de log.
* Consulta dos eventos registrados.
* Contagem de eventos.

## RF05 - Backup Automatizado

* Script Bash para backup.
* Compactação dos módulos do projeto.
* Geração automática de arquivos .tar.gz.

## Tecnologias Utilizadas

* Debian Linux
* Python 3
* Bash Script
* Git
* GitHub
* JSON
* SHA-256

## Como Executar

## Módulo de Autenticação

cd usuarios
python3 auth.py

## Módulo Blockchain

cd blockchain
python3 blockchain.py

## Módulo de Auditoria

cd auditoria
python3 auditor.py

## Módulo de Backup

cd backup
./backup.sh

## Resultados Obtidos

O projeto permitiu aplicar conceitos de administração de sistemas Linux, segurança da informação, controle de acesso, integridade de dados e automação de tarefas administrativas.
