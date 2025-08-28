"""
script.py — Restart Hidup Versi MVP

Tujuan:
- Membangun kebiasaan kecil yang bisa dieksekusi harian
- Mengurangi loop overthinking & penundaan
- Memvisualisasikan progres seperti sebuah project AI

Kebutuhan:
- Python 3.8+
- `rich` untuk tampilan terminal yang inspiratif (pip install rich)

"""

import time
import random
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

# 1. Inisialisasi mindset sebagai 'startup boot'
def initialize_mindset():
    console.rule("[bold green]🚀 SYSTEM REBOOT: MINDSET INIT")
    console.print(Panel("💡 [bold yellow]Versi baru dari dirimu sedang di-booting...\n\n🎯 Fokus pada 1 hal saja hari ini.\n🔁 Lakukan berulang selama 7 hari.\n🧠 Gagal? Ulangi. Kamu bukan robot."))

# 2. Pilih satu habit/goal harian (kecil saja)
def define_daily_focus():
    goal = Prompt.ask("\n📌 Fokusmu hari ini (1 kalimat aksi, bukan niat)?", default="Baca 10 menit topik AI")
    console.print(f"✅ Fokus hari ini: [bold cyan]{goal}[/bold cyan]")
    return goal

# 3. Eksekusi dengan timer sederhana
def start_focus_session(goal):
    duration = 25  # menit kerja (Pomodoro)
    console.rule("[bold blue]⏱️ MULAI FOKUS")
    console.print(f"🎯 Fokus selama {duration} menit untuk:\n[italic green]{goal}[/italic green]\n\nJangan multitasking. Tutup tab lain.")

    for i in range(duration, 0, -1):
        time.sleep(1)  # bisa ganti ke sleep(60) di real use
        if i % 5 == 0 or i <= 3:
            console.print(f"[grey58]...{i} menit tersisa[/grey58]")

    console.print(Panel(f"⏳ Waktu habis. [bold green]Selesai![/bold green]"))

# 4. Logging hasil
def log_result(goal):
    hasil = Prompt.ask("\n🧾 Apa yang kamu pelajari/rasakan?", default="Lebih tenang dari sebelumnya.")
    with open("daily_focus_log.txt", "a") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] Fokus: {goal}\n→ Refleksi: {hasil}\n\n")
    console.print("📝 Log tersimpan ke [bold]daily_focus_log.txt[/bold]")

# 5. Fungsi utama
def main():
    initialize_mindset()
    goal = define_daily_focus()
    start_focus_session(goal)
    log_result(goal)
    console.rule("[bold magenta]📦 SELESAI — Script Hidup Hari Ini")

if __name__ == "__main__":
    main()
