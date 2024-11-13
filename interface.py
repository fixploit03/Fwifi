import subprocess

# Menjalankan perintah 'iwconfig' untuk mendapatkan daftar interface Wi-Fi
result = subprocess.run(['iwconfig'], capture_output=True, text=True)

if result.returncode != 0:
    print("Gagal mendapatkan daftar interface Wi-Fi.")
else:
    interfaces = []
    for line in result.stdout.splitlines():
        # Mencari baris yang mengandung informasi interface Wi-Fi
        if 'IEEE 802.11' in line:
            interface = line.split()[0]  # Nama interface ada di awal baris
            interfaces.append(interface)

    if interfaces:
        print("Interface jaringan Wi-Fi yang tersedia:")
        for interface in interfaces:
            print(f"- {interface}")
    else:
        print("Tidak ada interface Wi-Fi yang ditemukan.")
