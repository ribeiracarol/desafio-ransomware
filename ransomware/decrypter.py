import os
from cryptography.fernet import Fernet

TARGET_DIR = "./target_files/"
EXTENSAO_CRIPTO = ".cripto"

# 1. Carrega a chave
try:
    with open("filekey.key", "rb") as filekey:
        key = filekey.read()
    fernet = Fernet(key)
except FileNotFoundError:
    print("Erro: Chave de descriptografia 'filekey.key' não encontrada.")
    exit()

def decrypt_file(file_path):
    # Lê os dados criptografados
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    
    # Descriptografa os dados
    decrypted_data = fernet.decrypt(encrypted_data)
    
    # Sobrescreve o arquivo com os dados descriptografados e remove a extensão
    original_path = file_path.replace(EXTENSAO_CRIPTO, "")
    with open(original_path, "wb") as file:
        file.write(decrypted_data)
        
    os.remove(file_path) # Remove o arquivo criptografado
    print(f"Descriptografado: {original_path}")

# 2. Itera sobre os arquivos criptografados
for filename in os.listdir(TARGET_DIR):
    if filename.endswith(EXTENSAO_CRIPTO):
        file_path = os.path.join(TARGET_DIR, filename)
        decrypt_file(file_path)

print("\nDescriptografia concluída. Arquivos restaurados.")