import subprocess

# Configura seu token de autenticação do ngrok
#NGROK_AUTH_TOKEN = "your_ngrok_auth_token_here"

# Autentica no ngrok
#subprocess.run(["./ngrok", "authtoken", NGROK_AUTH_TOKEN])

# Inicia o ngrok em segundo plano com um túnel TCP para a porta 3389
ngrok_process = subprocess.Popen(["./ngrok", "tcp", "3389"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print("ngrok iniciado e em execução em segundo plano.")
print("Você pode verificar os túneis em http://localhost:4040/status")

# O script termina aqui, mas o processo ngrok continua em execução
