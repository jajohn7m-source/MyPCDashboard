# Deb: pip install psutil gputil requests pysensors py3nvml

# Imports
import sensors
import psutil
import py3nvml
import GPUtil
import subprocess
import time
import requests
import webbrowser


def get_ram_temperature():
    sensors.init()

    try:
        # Iterate over available chipspysensors
        for chip in sensors.iter_detected_chips():
            # Check if the chip is related to RAM
            if b"ram" in chip.prefix.lower():
                # Iterate over available features of the chip
                for feature in chip:
                    # Check if the feature is temperature-related
                    if b"temp" in feature.name.lower():
                        # Retrieve the temperature reading
                        temp = feature.get_value()
                        return temp

    finally:
        sensors.cleanup()

    return None

# main function that will run after Setup is complete.
def main():
    # anything that needs init
    py3nvml.py3nvml.nvmlInit()
    global isRunning
    isRunning = True
    while isRunning:
        # get the cpu usage (as %)
        cpu_usage = psutil.cpu_percent()
        cpu_temp = psutil.sensors_temperatures()['k10temp'][0].current

        # get nvme temp
        nvme_temp = psutil.sensors_temperatures()['nvme'][0].current


        # Get RAM usuage (as %)
        ram_usage = psutil.virtual_memory().percent

        # Get Ram Temp
        ram_temp = get_ram_temperature()
        if ram_temp is not None:
            continue
        else:
            ram_temp = "RAM temperature reading not available."

        # Get GPU usuagepy3nvml
        gpus = GPUtil.getGPUs()
        gpu_usage = 0
        if gpus:
            gpu_usage = gpus[0].load
        handle = py3nvml.py3nvml.nvmlDeviceGetHandleByIndex(0)
        gpu_temp = py3nvml.py3nvml.nvmlDeviceGetTemperature(handle, py3nvml.py3nvml.NVML_TEMPERATURE_GPU)


        # create a data structure
        data = {
            'cpu': cpu_usage,
            'cpu_temp': cpu_temp,
            'ram': ram_usage,
            'ram_temp': ram_temp,
            'gpu': gpu_usage,
            'gpu_temp': gpu_temp,
            'nvme_temp': nvme_temp
        }

        # Send the data to  your server (node server)
        requests.post('http://localhost:3000/', json=data)

        # Sleep for a while before collecting data again
        time.sleep(1)

        if cpu_usage > 90:
            isRunning = False
    # cleanup
    py3nvml.py3nvml.nvmlShutdown()


# Perform Setup
if __name__ == '__main__':
    # Setup is performed here
    # Start node server:
    # Start the Node.js server
    server_process = subprocess.Popen(["nodejs", "../server/index.js"], stdout=subprocess.PIPE)
    webbrowser.open('http://localhost:3000/')
    time.sleep(2)
    main()
    server_process.terminate()
