# 🛡️ Desafio de Cibersegurança DIO — Simulação de Malware em Python

## 🚀 Visão Geral do Projeto
Este projeto é a implementação prática e documentada do desafio proposto pela **Digital Innovation One (DIO)**, com o objetivo de entender, simular e mitigar ameaças cibernéticas comuns — como **Ransomware** e **Keylogger** — em um ambiente **100% controlado e educacional (sandboxed)**.

O foco principal é o aprendizado e a reflexão sobre estratégias de defesa, demonstrando como essas ameaças operam e, mais importante, como podemos nos proteger delas no mundo real.

---

## ⚠️ Aviso de Segurança
**TODO O CÓDIGO NESTE REPOSITÓRIO É ESTRITAMENTE PARA FINS EDUCACIONAIS E DE ESTUDO DE CIBERSEGURANÇA.**  
Ele **nunca** deve ser executado em sistemas de produção, máquinas pessoais ou fora de um ambiente virtual isolado (VM / Sandbox).

---

# 🛠️ Ransomware Simulado em Python
A simulação de **Ransomware** demonstra o processo de sequestro de dados usando criptografia forte.

## 🎯 Funcionamento
- **Geração da Chave (`key.py`)**  
  Utiliza a biblioteca `cryptography` (módulo `Fernet`) para gerar uma chave simétrica AES-128. Essa chave é o "segredo" do atacante.

- **Criptografia (`encrypter.py`)**  
  O script percorre o diretório de teste (`target_files/`), lê os arquivos e os criptografa utilizando a chave gerada. Após a criptografia, renomeia os arquivos adicionando a extensão `.cripto` e gera a mensagem de resgate.

- **Mensagem de Resgate (`README_RESCUE.txt`)**  
  Arquivo deixado para a vítima com instruções e a suposta "demanda".

- **Descriptografia (`decrypter.py`)**  
  O script de recuperação que, em posse da chave correta, reverte o processo, restaurando os arquivos originais.

## 📚 Códigos e Estrutura

| Arquivo | Função |
|---|---|
| `ransomware/key.py` | Gera a chave de criptografia Fernet. |
| `ransomware/encrypter.py` | Executa a criptografia dos arquivos de teste. |
| `ransomware/decrypter.py` | Descriptografa os arquivos utilizando a chave. |
| `ransomware/target_files/` | Pasta contendo os arquivos de teste seguros. |

---

# ⌨️ Keylogger Simulado em Python
A simulação de **Keylogger** foca na captura furtiva de dados e na exfiltração (envio) desses dados para um atacante.

## 🎯 Funcionamento
- **Captura de Teclas**  
  Utiliza a biblioteca `pynput` para escutar e registrar todas as teclas pressionadas no sistema.

- **Registro em Log**  
  As teclas são formatadas e salvas em um arquivo de log temporário (`keylogger/log.txt`).

- **Exfiltração (Envio Furtivo)**  
  - Um *thread* em segundo plano é iniciado para gerenciar o envio.  
  - O script utiliza o módulo `smtplib` para enviar o arquivo `log.txt` periodicamente para um e-mail de controle (do "atacante").  
  - Após o envio bem-sucedido, o arquivo de log é limpo para evitar logs repetidos e melhorar o *stealth*.

## 📚 Códigos e Estrutura

| Arquivo | Função |
|---|---|
| `keylogger/keylogger.py` | Script principal que inicia a escuta e o thread de envio. |
| `keylogger/log.txt` | Arquivo que armazena as teclas capturadas. |

---

# 🛡️ Defesa e Mitigação: A Verdadeira Lição
A parte mais importante deste desafio é a reflexão sobre como detectar, prevenir e responder a esses tipos de ataques.

## 1. Prevenção Ativa (Tecnológica)
- **Antivírus / EDR**  
  Soluções de Endpoint Detection and Response detectam o comportamento do malware (ex.: ransomware acessando muitos arquivos rapidamente ou keylogger monitorando APIs de teclado) e bloqueiam a execução antes que o dano ocorra.

- **Firewall de Saída**  
  Pode ser configurado para bloquear tráfego SMTP (portas `25`, `465`, `587`) ou outros protocolos de exfiltração de dados para destinos não autorizados.

- **Princípio do Menor Privilégio (PoLP)**  
  Limitar o que um usuário ou processo pode fazer. Se o ransomware não tiver permissão para modificar arquivos críticos, o dano é contido.

## 2. Contenção e Recuperação
- **Backups Seguros**  
  O método mais eficaz contra ransomware. Ter backups *offline*, imutáveis e testados permite restaurar dados sem pagar resgate.

- **Segmentação de Rede**  
  Isolar sistemas e dados críticos do restante da rede para limitar propagação lateral em caso de infecção.

- **Sandboxing**  
  Ambientes virtuais e isolados (como a VM utilizada neste projeto) protegem o host da execução de código malicioso.

## 3. Fator Humano (Conscientização)
- **Treinamento**  
  A principal vulnerabilidade é o usuário. Treinamento contínuo ajuda a identificar phishing e outros vetores de ataque (links suspeitos, anexos maliciosos).

- **Autenticação Multifator (MFA)**  
  Mesmo que um keylogger capture uma senha, o MFA impede que o atacante finalize a exploração.

---

# ⚙️ Como Executar a Simulação (Ambiente de Teste)

**Pré-requisitos**
- Python 3.x instalado.  
- Um ambiente virtual (VM, Docker ou Sandbox) **obrigatório**.

**1. Clonar o Repositório**
```bash
git clone https://[URL-DO-SEU-REPOSITÓRIO]
cd [NOME-DO-SEU-REPOSITÓRIO]
```

> Nota: substitua `https://[URL-DO-SEU-REPOSITÓRIO]` pela URL correta do repositório.

**2. Instalar as Dependências**  
É recomendado criar e ativar um ambiente virtual antes da instalação.
```bash
pip install -r requirements.txt
```
*(Crie um `requirements.txt` listando `pynput` e `cryptography`.)*

**3. Rodar o Ransomware (no ambiente isolado!)**
```bash
cd ransomware/
# Gera a chave
python key.py
# Executa o "ataque" (somente em ambiente controlado)
python encrypter.py
# Para recuperar (com a chave correta)
python decrypter.py
```

**4. Rodar o Keylogger (no ambiente isolado!)**
```bash
cd keylogger/
# Configure credenciais de e-mail no script keylogger.py (use e-mail de teste / App Password)
python keylogger.py
```
Digite algumas teclas e verifique `keylogger/log.txt` e, após o intervalo definido, a caixa de entrada configurada para exfiltração.

---

## 🎓 Conclusão e Próximos Passos
Este projeto reforça a importância da **Defesa em Profundidade**. Ao entender o mecanismo de um ataque, tornamo-nos mais eficazes em construir barreiras contra ele.

