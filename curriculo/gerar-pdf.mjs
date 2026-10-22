// Converte curriculo/ti.html e curriculo/educacao.html em PDF (Playwright + Chromium).
import { chromium } from "playwright";
import { fileURLToPath, pathToFileURL } from "node:url";
import path from "node:path";

const aqui = path.dirname(fileURLToPath(import.meta.url));
const browser = await chromium.launch();
const page = await browser.newPage();
for (const nome of ["ti", "educacao"]) {
  await page.goto(pathToFileURL(path.join(aqui, `${nome}.html`)).href, { waitUntil: "networkidle" });
  await page.pdf({ path: path.join(aqui, `jeferson-pereira-curriculo-${nome}.pdf`), format: "A4", printBackground: true, preferCSSPageSize: true });
  console.log("pdf", nome);
}
await browser.close();
