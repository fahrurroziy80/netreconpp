import argparse
from core import recon
from reports import generator

def main():
    parser = argparse.ArgumentParser(description="NetRecon++: Advanced Network Recon Tool")
    parser.add_argument('--target', required=True, help='Target IP, CIDR, or domain')
    parser.add_argument('--mode', choices=['fast', 'full', 'stealth'], default='fast')
    parser.add_argument('--enum-web', action='store_true', help='Enable web service enumeration')
    parser.add_argument('--enum-smb', action='store_true', help='Enable SMB enumeration')
    parser.add_argument('--output', default='report.json', help='Output file name')
    args = parser.parse_args()

    results = recon.run_recon(args)
    generator.generate_report(results, args.output)

if __name__ == '__main__':
    main()
