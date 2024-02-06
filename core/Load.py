from psutil import process_iter

class Load:
    @staticmethod
    def get_pid(nome_executavel):
        try:
            for processo in process_iter(['pid', 'name']):
                if processo.info['name'] == nome_executavel:
                    return processo.info['pid']
            return None
        except Exception as e:
            return None
    
    