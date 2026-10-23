# -*- coding: utf-8 -*-
"""اجرای هم‌زمان چهار ربات بله در Pydroid 3."""
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BOTS = [
    ("گرشا", ROOT / "gersha.py"),
    ("دستیار هوش مصنوعی GPT-5", ROOT / "GPT5_Bale_Neon_Premium_groq_fixed_config.py"),
    ("دانلودر ویدیو", ROOT / "bot.py"),
    ("ربات خبر", ROOT / "botkhabar.py"),
]

def start_bot(name, script):
    if not script.is_file():
        print(f"❌ فایل {script.name} پیدا نشد؛ {name} اجرا نشد.")
        return None
    print(f"🚀 در حال روشن کردن {name}...")
    try:
        return subprocess.Popen(
            [sys.executable, "-u", str(script)],
            cwd=str(ROOT),
        )
    except Exception as exc:
        print(f"❌ اجرای {name} ناموفق بود: {exc}")
        return None

def main():
    processes = {}
    try:
        for name, script in BOTS:
            proc = start_bot(name, script)
            if proc is not None:
                processes[name] = (script, proc)
            time.sleep(1)

        if not processes:
            print("هیچ رباتی اجرا نشد.")
            return

        print("\n✅ تلاش برای اجرای هر چهار ربات انجام شد.")
        print("اگر توکن/کلید یا کتابخانه‌ای اشتباه باشد، خطای همان ربات در همین پنجره دیده می‌شود.")
        print("این پنجره را باز نگه دار. برای خاموش کردن همه، Stop را بزن.\\n")

        while True:
            for name, (script, proc) in list(processes.items()):
                code = proc.poll()
                if code is not None:
                    print(f"⚠️ {name} متوقف شد (کد {code}). تلاش مجدد تا 5 ثانیه دیگر...")
                    time.sleep(5)
                    new_proc = start_bot(name, script)
                    if new_proc is not None:
                        processes[name] = (script, new_proc)
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nدر حال خاموش کردن ربات‌ها...")
    finally:
        for _, proc in processes.values():
            if proc.poll() is None:
                proc.terminate()
        for _, proc in processes.values():
            try:
                proc.wait(timeout=5)
            except Exception:
                try:
                    proc.kill()
                except Exception:
                    pass
        print("فرایندهای اجراکننده متوقف شدند.")

if __name__ == "__main__":
    main()
