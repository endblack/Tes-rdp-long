import subprocess
import time
import requests

# Configura seu token de autenticação do ngrok
#NGROK_AUTH_TOKEN = "your_ngrok_auth_token_here"

# Autentica no ngrok
#subprocess.run(["./ngrok/ngrok.exe", "authtoken", NGROK_AUTH_TOKEN])

# Inicia o ngrok em segundo plano com um túnel TCP para a porta 3389
ngrok_process = subprocess.Popen(["./ngrok/ngrok.exe", "tcp", "3389"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print("Ngrok OK")
def get_ngrok_public_url():
    try:
        response = requests.get("http://localhost:4040/api/tunnels")
        response.raise_for_status()
        tunnels = response.json().get("tunnels", [])
        if tunnels:
            for tunnel in tunnels:
                public_url = tunnel['public_url']
                if public_url.startswith("tcp://"):
                    public_url = public_url.replace("tcp://", "")
                print(f"Ngrok Url: {public_url}")
                return public_url
        else:
            print("Nenhum túnel ngrok ativo encontrado.")
            return None
    except requests.RequestException as e:
        print(f"Erro ao verificar o status do ngrok: {e}")
        return None

public_url = get_ngrok_public_url()

#print("ngrok iniciado e em execução em segundo plano.")
#print("Você pode verificar os túneis em http://localhost:4040/status")

# O script termina aqui, mas o processo ngrok continua em execução
