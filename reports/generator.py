import json

def generate_report(results, filename):
    print(f"[*] Generating report to {filename}")
    with open(filename, 'w') as f:
        json.dump(results, f, indent=4)
