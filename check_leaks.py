import requests
import hashlib

def check_password_pwned(password):
    sha1pwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1pwd[:5], sha1pwd[5:]
    url = f'https://api.pwnedpasswords.com/range/{prefix}'
    response = requests.get(url)
    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)
    return 0

def main():
    print("Verificação de vazamento de senha no Have I Been Pwned (HIBP):")
    pwd = input("Digite a senha para verificar: ").strip()
    count = check_password_pwned(pwd)
    if count:
        print(f"A senha '{pwd}' foi encontrada {count} vezes em vazamentos.")
    else:
        print(f"A senha '{pwd}' NÃO foi encontrada em vazamentos.")

if __name__ == "__main__":
    main()