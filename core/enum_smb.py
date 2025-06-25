from .utils import run_cmd

def enumerate(target):
    print(f"[*] Enumerating SMB services on {target}")
    return run_cmd(f"smbclient -L {target} -N")
