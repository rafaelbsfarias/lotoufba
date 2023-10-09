import psutil
import time
import logging

# Configurar o logger para salvar informações em um arquivo
logging.basicConfig(filename='monitoring.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Função para coletar e registrar as informações do sistema
def monitor_system():
    while True:
        # Obter o uso atual da CPU e da memória
        cpu_percent = psutil.cpu_percent()
        memory_percent = psutil.virtual_memory().percent

        # Registrar as informações no log
        logging.info(f'CPU Usage: {cpu_percent}% - Memory Usage: {memory_percent}%')

        # Esperar por um intervalo (por exemplo, 60 segundos)
        time.sleep(60)

if __name__ == '__main__':
    try:
        # Iniciar a monitorização
        monitor_system()
    except KeyboardInterrupt:
        # Encerrar o script quando o usuário pressionar Ctrl+C
        pass
