# process and system util
import psutil

def systemInfo():
    cpuInformation = f"cpu: {psutil.cpu_percent(interval=1)}% usage"
    memoryInformation = psutil.virtual_memory()
    memoryUsage = f"memory: {memoryInformation.percent} % used ({round(memoryInformation.used / (1024**3), 2)} GB)"
    # each location put in the dis_usage 
    diskInformation = psutil.disk_usage("/")
    diskUsage = f"Disk: {diskInformation.percent}% used ({round(diskInformation.used / (1024**3), 2)} GB)"
    print(cpuInformation)
    print(memoryUsage)
    print(diskUsage)
systemInfo()