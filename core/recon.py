from .utils import run_cmd, print_banner

def run_recon(args):
    print_banner()
    print(f"[*] Starting scan on target: {args.target} with mode: {args.mode}")

    result = {}
    # Basic Nmap Scan
    nmap_cmd = f"nmap -sV -T4 {args.target}"
    result['nmap'] = run_cmd(nmap_cmd)

    if args.enum_web:
        from . import enum_web
        result['web'] = enum_web.enumerate(args.target)

    if args.enum_smb:
        from . import enum_smb
        result['smb'] = enum_smb.enumerate(args.target)

    return result
