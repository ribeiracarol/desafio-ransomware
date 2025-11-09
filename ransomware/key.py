from cryptography.fernet import Fernet

# 1. Gera uma chave de criptografia segura
key = Fernet.generate_key()

# 2. Salva a chave em um arquivo (o segredo do "atacante")
with open("filekey.key", "wb") as filekey:
    filekey.write(key)

print("Chave de criptografia gerada e salva em 'filekey.key'")