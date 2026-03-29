import time
import subprocess

while True:
    print("Executando bot Workana...")

    subprocess.run(["python3", "/home/darkcover/Documentos/Workana/Bot/Site/SBot.py"])

    print("Aguardando 30 minutos...")
    time.sleep(1800)  # 30 minutos = 1800 segundos