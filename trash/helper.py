import psutil

def find_process_by_name(process_name):
    for process in psutil.process_iter(['pid', 'name', 'username', 'status', 'cpu_percent', 'memory_info']):
        if process.info['name'] == process_name:
            return process.info

process_name = 'ravendawn_dx-1706708469.exe'
process_info = find_process_by_name(process_name)

if process_info:
    print(f"Processo encontrado - PID: {process_info['pid']}")
    print(f"Nome: {process_info['name']}")
    print(f"Usuário: {process_info['username']}")
    print(f"Status: {process_info['status']}")
    print(f"Uso de CPU: {process_info['cpu_percent']}%")
    print(f"Uso de Memória: {process_info['memory_info'].rss / (1024 * 1024):.2f} MB")
else:
    print(f"O processo {process_name} não está em execução.")
