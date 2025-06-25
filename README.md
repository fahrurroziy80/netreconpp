# NetRecon++

NetRecon++ adalah framework rekonstruksi jaringan otomatis berbasis CLI yang dapat melakukan recon aktif dan pasif, enumerasi layanan, dan menghasilkan laporan JSON secara langsung.

## Usage
```
python3 main.py --target 192.168.1.1 --mode full --enum-web --output result.json
```

#--target: IP, CIDR, atau domain

--mode: fast, full, atau stealth (opsi lanjutan)

--enum-web: Scan dan deteksi layanan web

--enum-smb: Enumerasi layanan SMB

--output: Nama file hasil (format JSON)

