import subprocess

# Menjalankan perintah 'ip link' untuk mendapatkan daftar interface jaringan
result = subprocess.run(['ip', 'link'], capture_output=True, text=True)

if result.returncode != 0:
    print("Gagal mendapatkan daftar interface.")
else:
    interfaces = []
    for line in result.stdout.splitlines():
        if line.strip() and not line.strip().startswith("lo"):  # Mengabaikan 'lo' (loopback interface)
            interface = line.split(":")[1].strip().split()[0]
            interfaces.append(interface)

    if interfaces:
        print("Interface jaringan yang tersedia:")
        for interface in interfaces:
            print(f"- {interface}")
    else:
        print("Tidak ada interface yang ditemukan.")
