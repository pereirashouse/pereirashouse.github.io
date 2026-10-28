"""Gera ti.html e educacao.html a partir do mesmo conteúdo.
Depois: python3 curriculo/renderizar-pdf.py, ou use o gerador Playwright Node."""
from pathlib import Path

AQUI = Path(__file__).parent

CSS = """
@page{size:A4;margin:12mm 14mm 10mm}
*{box-sizing:border-box}
body{margin:0;color:#15211F;font:10.5pt/1.28 "Public Sans",Arial,sans-serif;background:#fff}
.pg{max-width:780px;margin:0 auto;padding:20px 12px}
@media print{.pg{padding:0;max-width:none}}
h1{font:700 20pt/1.05 "Familjen Grotesk",Arial,sans-serif;margin:0}
.cargo{margin:2px 0 4px;font-weight:600;color:var(--c)}
.contato{font-size:8.8pt;line-height:1.25;color:#56655F;display:flex;flex-wrap:wrap;gap:1px 10px}
.contato a{color:inherit;text-decoration:none}
h2{font:700 10.8pt/1.1 "Familjen Grotesk",Arial,sans-serif;text-transform:uppercase;letter-spacing:.05em;color:var(--c);
   border-bottom:1.5px solid var(--c);padding-bottom:2px;margin:10px 0 5px}
p{margin:0 0 4px}
ul{margin:0;padding-left:15px}
li{margin-bottom:1px}
.item{margin-bottom:5px;break-inside:avoid}
.item .t{display:flex;justify-content:space-between;gap:8px;font-weight:600;line-height:1.2}
.item .t span{font-weight:400;color:#56655F;font-size:8.8pt;white-space:nowrap}
.item .l{font-size:8.8pt;color:#56655F}
.sk{display:grid;grid-template-columns:138px 1fr;gap:2px 9px;font-size:9.3pt;line-height:1.2}
.sk b{font-weight:600}
.extra{font-size:9.5pt;margin-top:4px}
.nota{font-size:8.2pt;line-height:1.1;color:#56655F;margin-top:2px}
"""

CONTATO = """<p class="contato"><span>Paraná, Brasil</span><a href="tel:+5542999601085">(42) 99960-1085</a>
<a href="https://www.linkedin.com/in/jefersonluizpereira">linkedin.com/in/jefersonluizpereira</a>
<a href="https://pereirashouse.github.io/">pereirashouse.github.io</a>
<a href="https://github.com/pereirashouse">github.com/pereirashouse</a></p>"""

EXPERIENCIA = """
<div class="item"><p class="t">Analista de Infraestrutura Sênior <span>mai. 2026 – atual</span></p><p class="l">Indústria · Paraná</p>
<ul><li>PoC de substituição da plataforma de virtualização, com alternativa open source e critérios de rollback definidos antes da implantação e acionados quando o risco se confirmou.</li>
<li>802.1X por conta de máquina (NPS, Active Directory, GPO) em dezenas de APs.</li>
<li>Análise de Wi-Fi com Python/API UniFi; automação PowerShell/GPO; backup Veeam e Dell PowerProtect.</li></ul></div>
<div class="item"><p class="t">Analista de TI Pleno <span>set. 2022 – mai. 2026</span></p><p class="l">Indústria · Paraná</p>
<ul><li>Infraestrutura de TI em ambiente industrial com várias unidades: switches Aruba e TP-Link, Wi-Fi Ubiquiti, firewall, VMware/KVM, Zabbix/Grafana e Dell PowerProtect.</li></ul></div>
<div class="item"><p class="t">Analista de TI Júnior <span>ago. 2021 – set. 2022</span></p><p class="l">Indústria · Paraná</p>
<ul><li>Suporte de infraestrutura e usuários no AD; antivírus, Wi-Fi Ubiquiti, VMware vSphere, KVM Oracle, Zabbix e Grafana.</li></ul></div>
<div class="item"><p class="t">Analista Financeiro <span>mar. 2014 – set. 2019</span></p><p class="l">Multinacional de embalagens · Paraná</p></div>
<div class="item"><p class="t">Assistente de TI <span>jan. 2012 – abr. 2014</span></p><p class="l">Empresa de fundição · Paraná · Help Desk N1/N2 e rede local</p></div>
"""

FORMACAO = """
<div class="item"><p class="t">Licenciatura em Computação (cursando) <span>UTFPR · desde fev. 2024</span></p></div>
<div class="item"><p class="t">Técnico em Administração</p></div>
"""

COMPETENCIAS = """<div class="sk">
<b>Virtualização</b><span>VMware vSphere · Sangfor HCI · KVM Oracle · Proxmox VE · Hyper-V</span>
<b>Sistemas e identidade</b><span>Windows Server · Linux · Active Directory · Microsoft Entra ID (Azure AD)</span>
<b>Redes e segurança</b><span>Aruba / TP-Link · Wi-Fi Ubiquiti · FortiGate · 802.1X / RADIUS · VLAN</span>
<b>Backup e monitoramento</b><span>Veeam · Dell PowerProtect · Zabbix · Grafana</span>
<b>Automação</b><span>Python · PowerShell · GPO</span>
</div>"""

PROJ_TI = """<ul>
<li><b>Wi-Fi corporativo com 802.1X:</b> política de conta de máquina, NPS/AD/GPO, piloto com rollback e bloqueio de dispositivos pessoais.</li>
<li><b>Modernização de rede de filial industrial:</b> levantamento sem documentação, parser de configurações em Python, drift, VLANs e roteiro por risco.</li>
<li><b>Monitor de quedas Wi-Fi de coletores WMS:</b> agente Python open source com testes automatizados, CI multiversão e TLS seguro por padrão.</li>
<li><b>Alarme falso de robôs industriais:</b> causa raiz em canal 2,4 GHz saturado; RSSI mínimo resolveu sem afetar os robôs.</li>
</ul>"""

PROJ_EDU = """<ul>
<li><b>Rede da Escola</b> (protótipo publicado, offline): simulador para 8º/9º ano; hipótese, verificação e ping; relatório e rubrica de endereçamento, diagnóstico, segurança e comunicação; EF07CO06, EF07CO07, EF08CO06 e EF08CO10.</li>
<li><b>A Rede Parou</b> (protótipo publicado): laboratório com logs fictícios para 9º ano/Ensino Médio; método científico, papéis, três pistas graduais e versão impressa; EF07CO06, EF07CO07 e EF08CO06.</li>
<li><b>Operação Anzol</b> (publicado): jogo de perícia de 60 min para 9º ano; Três Momentos Pedagógicos, papéis alternados, protocolo P.A.R.E. e avaliação formativa com laudo, rubrica e ticket de saída; EF09CO04 e EF09CO10.</li>
<li><b>Do Planejamento à Prática</b> (artigo publicado): pipeline em quatro etapas — captura, seleção/sanitização com revisão humana, transposição BNCC e publicação versionada de planos de aula e rubricas.</li>
</ul><p class="extra"><b>Outros materiais:</b> simulador de roteador, IIR “A invisibilidade do Wi-Fi”, oficina desplugada e 802.1X didático.</p>"""

PONTE = "<p>Mentoria, runbooks e incidentes sanitizados viram materiais didáticos alinhados à BNCC.</p>"

VARIANTES = {
    "ti": dict(
        titulo="Currículo · Infraestrutura de TI", cor="#1D5BB8",
        cargo="Analista de Infraestrutura de TI Sênior · Licenciando em Computação (UTFPR)",
        corpo=f"""<h2>Resumo</h2>
<p>Analista de infraestrutura com mais de cinco anos em TI industrial, em ambiente com várias unidades, com foco em redes e Wi-Fi, identidade/802.1X, virtualização, backup, monitoramento e automação Python/PowerShell. Atua com hipóteses, evidências e rollback definido antes da mudança.</p>
{PONTE}
<h2>Experiência</h2>{EXPERIENCIA}
<h2>Projetos selecionados</h2>{PROJ_TI}
<h2>Competências técnicas</h2>{COMPETENCIAS}
<h2>Formação</h2>{FORMACAO}"""),
    "educacao": dict(
        titulo="Currículo · Computação e Educação", cor="#23774A",
        cargo="Licenciando em Computação (UTFPR) · Professor de tecnologia · Analista de Infraestrutura de TI Sênior",
        corpo=f"""<h2>Resumo</h2>
<p>Professor de tecnologia em cursos livres desde 2008 (redes, hardware, BNCC Computação, Excel) e analista sênior de infraestrutura. Parte de casos reais antes da teoria, usa IA só como copilota com dados sanitizados e cria materiais alinhados à BNCC, revisados e adaptados ao contexto local, com versões offline e avaliação formativa.</p>
<h2>Materiais e método</h2>{PROJ_EDU}
<h2>Formação</h2>{FORMACAO}
<h2>Experiência profissional</h2>{EXPERIENCIA}
<h2>Competências técnicas</h2>{COMPETENCIAS}"""),
}

for nome, v in VARIANTES.items():
    html = f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Jeferson Luiz Pereira · {v['titulo']}</title>
<meta name="robots" content="noindex">
<link rel="stylesheet" href="../assets/fonts.css">
<style>:root{{--c:{v['cor']}}}{CSS}</style></head>
<body><div class="pg">
<h1>Jeferson Luiz Pereira</h1>
<p class="cargo">{v['cargo']}</p>
{CONTATO}
{v['corpo']}
<p class="nota">Confidencialidade: endereços, nomes de servidores, domínios e empresas omitidos. Estudos completos: pereirashouse.github.io.</p>
</div></body></html>
"""
    (AQUI / f"{nome}.html").write_text(html, encoding="utf-8")
    print("gerado", nome)
