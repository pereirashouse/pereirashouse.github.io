"""Converte os dois currículos HTML em PDF A4 usando Playwright Python.

Requisitos: pip install playwright e playwright install chromium,
ou Chromium instalado no sistema. CHROMIUM_PATH permite indicar o executável.
Execute gerar.py antes, se tiver atualizado o conteúdo dos currículos.
"""
from pathlib import Path
import os
import shutil

from playwright.sync_api import sync_playwright

AQUI = Path(__file__).resolve().parent


def main():
    with sync_playwright() as p:
        executavel = os.environ.get("CHROMIUM_PATH")
        if not executavel and not Path(p.chromium.executable_path).exists():
            executavel = next(
                (shutil.which(nome) for nome in ("chromium", "chromium-browser", "google-chrome") if shutil.which(nome)),
                None,
            )
        opcoes = {"headless": True}
        if executavel:
            opcoes["executable_path"] = executavel
        with p.chromium.launch(**opcoes) as browser:
            page = browser.new_page()
            for nome in ("ti", "educacao"):
                html = AQUI / f"{nome}.html"
                page.goto(html.as_uri(), wait_until="networkidle")
                page.evaluate("document.fonts.ready")
                destino = AQUI / f"jeferson-pereira-curriculo-{nome}.pdf"
                page.pdf(
                    path=str(destino),
                    format="A4",
                    print_background=True,
                    prefer_css_page_size=True,
                    display_header_footer=False,
                )
                print(f"PDF gerado: {destino.name}")


if __name__ == "__main__":
    main()
