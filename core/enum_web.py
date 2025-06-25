from .utils import run_cmd

def enumerate(target):
    print(f"[*] Enumerating web services on {target}")
    return run_cmd(f"whatweb {target}")
