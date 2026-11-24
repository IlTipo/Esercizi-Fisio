"""Genera index.html (pagina completa da aprire nel browser) a partire da src/body.html."""
from pathlib import Path

root = Path(__file__).parent
body = (root / "src" / "body.html").read_text(encoding="utf-8")
head = (
    '<!doctype html>\n<html lang="it">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
    "</head>\n<body>\n"
)
(root / "index.html").write_text(head + body + "\n</body>\n</html>\n", encoding="utf-8")
print("index.html generato")
