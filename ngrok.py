import subprocess
import os
import time

# Função para listar todos os arquivos e pastas do diretório atual
def list_files_and_directories():
    current_dir = os.getcwd()
    print(f"Listando arquivos e pastas no diretório: {current_dir}")
    with os.scandir(current_dir) as entries:
        for entry in entries:
            if entry.is_file():
                print(f"Arquivo: {entry.name}")
            elif entry.is_dir():
                print(f"Pasta: {entry.name}")

# Listar arquivos e pastas no diretório atual
list_files_and_directories()

# Configura seu token de autenticação do ngrok
#NGROK_AUTH_TOKEN = os.environ.get("NGROK_AUTH_TOKEN")

# Autentica no ngrok
#subprocess.run(["ngrok.exe", "authtoken", NGROK_AUTH_TOKEN], check=True)

# Inicia o ngrok em segundo plano com um túnel TCP para a porta 3389
ngrok_process = subprocess.Popen(["ngrok.exe", "tcp", "3389"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print("ngrok iniciado e em execução em segundo plano.")
print("Você pode verificar os túneis em http://localhost:4040/status")

# Espera um pouco para garantir que o ngrok inicie corretamente
time.sleep(5)
