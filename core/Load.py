from psutil import process_iter

class Load:

    @staticmethod
    def get_pid(Executable):
        try:
            for processo in process_iter(['pid', 'name']):
                if processo.info['name'] == Executable:
                    return processo.info['pid']
            return None
        except Exception as e:
            return None
    
    