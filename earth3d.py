from pathlib import Path
import webview

html_file = Path(__file__).with_name("earth.html")

webview.create_window(
    "Earth 3D Hackathon",
    html_file.resolve().as_uri(),
    width=1280,
    height=800
)

webview.start()