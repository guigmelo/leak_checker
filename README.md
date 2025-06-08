# 🔐 Leaks Checker

Verificador de vazamento de senhas utilizando a API Have I Been Pwned (HIBP), empacotado com Docker para fácil execução local.

## 📦 Sobre o Projeto

Este projeto permite verificar se uma senha já foi exposta em vazamentos públicos de dados, utilizando a API do [Have I Been Pwned](https://haveibeenpwned.com/). A verificação é feita de forma segura e anônima, seguindo o padrão k-Anonymity da API.

Desenvolvido em Python, o Leaks Checker é distribuído como um container Docker para facilitar o uso em qualquer sistema operacional.

## 🐳 Como Executar com Docker

### 1. Clone o repositório

```bash
git clone https://github.com/kashieel/gs.git
cd gs
docker build -t check_leaks .
docker run -it check_leaks
