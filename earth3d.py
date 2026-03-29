from pathlib import Path
import webview # web_gorunumu yerine orijinal kütüphane adı

# Dosya yolunu belirle
html_dosyasi = Path(__file__).parent / "dunya.html"

# Pencereyi oluştur (Burası kritik!)
window = webview.create_window(
    "ORBIT-EYE | Discord Kronos GGrid - Milli Uydu Takip Sistemi",
    html_dosyasi.resolve().as_uri(),
    width=1400, # Biraz daha geniş, profesyonel görünür
    height=900,
    resizable=True, # Jürinin ekranına göre ayarlanabilir
    confirm_close=True # Yanlışlıkla kapanmasın
)

# Başlat
webview.start()
