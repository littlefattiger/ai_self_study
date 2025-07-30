import platform
import psutil
import subprocess
import json


def get_host_info():
    info = {
        "system":platform.system(),
        "release":platform.release(),
        "machine":platform.machine(),
        "processor":platform.processor(),
        "memory_gb":str(round(psutil.virtual_memory().total))
    }
    cpu_count = psutil.cpu_count(logical=1)
    if cpu_count is None:
        info["cpu_count"] = "-1"
    else:
        info["cpu_count"] = str(cpu_count)
    try:
        cpu_model = subprocess.check_output(
    ["wmic", "cpu", "get", "Name"], shell=True).decode().strip().split('\n')[1].strip()

        info["cpu_model"] = cpu_model
    except Exception:
        info["cpu_model"] = "unknown"

    return json.dumps(info, indent=4)



if __name__ == '__main__':
    print(get_host_info())