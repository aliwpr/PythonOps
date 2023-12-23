# process and system util
import psutil

def system_info():
    cpu_information = f"cpu: {psutil.cpu_percent(interval=1)}% usage"
    memory_information = psutil.virtual_memory()
    memory_usage = f"memory: {memory_information.percent} % used ({round(memory_information.used / (1024**3), 2)} GB)"
    # each location put in the dis_usage 
    disk_information = psutil.disk_usage("/")
    disk_usage = f"Disk: {disk_information.percent}% used ({round(disk_information.used / (1024**3), 2)} GB)"
    print(cpu_information)
    print(memory_usage)
    print(disk_usage)
system_info()