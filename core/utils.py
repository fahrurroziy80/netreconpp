import subprocess

def run_cmd(cmd):
    try:
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL)
        return result.decode()
    except subprocess.CalledProcessError:
        return "[ERROR] Command failed"

def print_banner():
    banner = """
 _   _      _                      
| \ | | ___| | ___  _ __ ___   ___ 
|  \| |/ _ \ |/ _ \| '_ ` _ \ / _ \
| |\  |  __/ | (_) | | | | | |  __/
|_| \_|\___|_|\___/|_| |_| |_|\___|

Advanced Network Recon Framework
"""
    print(banner)
