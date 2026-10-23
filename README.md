# Portfólio de Jeferson Luiz Pereira

Portfólio público que reúne experiência profissional em **infraestrutura de TI** e projetos de **Computação e Educação**.

[Visitar o portfólio](https://pereirashouse.github.io/) · [Contato pelo LinkedIn](https://www.linkedin.com/in/jefersonluizpereira)

## Trilhas

- [Infraestrutura de TI](https://pereirashouse.github.io/#infra): redes corporativas, Wi-Fi, 802.1X, Active Directory, virtualização, backup, monitoramento e automação.
- [Computação e Educação](https://pereirashouse.github.io/#edu): simuladores, oficinas e materiais para aprendizagem de redes e Computação.

## Estudos de caso

- [Wi-Fi corporativo com 802.1X](https://pereirashouse.github.io/projetos/wifi-8021x/): autenticação de máquinas com NPS, Active Directory e UniFi.
- [Diagnóstico de falha 802.1X](https://pereirashouse.github.io/projetos/incidente-8021x-windows/): investigação orientada por logs após atualização do Windows.
- [Modernização de rede industrial](https://pereirashouse.github.io/projetos/rede-filial-industrial/): levantamento, VLANs, redundância, documentação e análise de risco.
- [Quedas dos coletores Wi-Fi](https://pereirashouse.github.io/projetos/quedas-coletores-wifi/): investigação em seis frentes, correções por rodada e comparação de amostras, com validação contínua.
- [Avaliação de virtualização](https://pereirashouse.github.io/projetos/poc-virtualizacao/): PoC de VMware, Sangfor HCI e Proxmox VE.
- [Troubleshooting pós-migração de VM](https://pereirashouse.github.io/projetos/troubleshooting-pos-migracao/): migração KVM → VMware com três bloqueios em cadeia (acesso, rede e HTTP 503), resolvidos sem rollback.
- [Monitoramento Wi-Fi com Python](https://github.com/pereirashouse/monitoramentowificompython): código de coleta de eventos de queda de coletores e geração de relatórios.

### Testes do monitor

O monitor tem **177 testes automatizados** (coleta, eventos, relatórios, persistência, concorrência e TLS seguro por padrão), executados no GitHub Actions em Python 3.10, 3.11, 3.12 e 3.13 a cada push na `main`. Resultados: [execuções do workflow](https://github.com/pereirashouse/monitoramentowificompython/actions/workflows/testes.yml?query=branch%3Amain).

## Materiais educacionais

[Simulador de configuração de roteador](https://pereirashouse.github.io/educacao/simulador-roteador/): seis desafios com feedback automático sobre alcance, escolha de canal, comparação de faixas, segurança, QoS e leitura de log. Os desafios têm testes de interface com Playwright em tela de computador e de celular ([workflow de interface](https://github.com/pereirashouse/simulador-configura-o-roteador/actions/workflows/testes-interface.yml?query=branch%3Amain)). Código e orientações ao professor no [repositório do simulador](https://github.com/pereirashouse/simulador-configura-o-roteador).

[Operação Anzol](https://pereirashouse.github.io/operacao-anzol/) é um jogo de perícia de mensagens fictícias. [Rede da Escola](https://pereirashouse.github.io/rede-da-escola/) e [A Rede Parou](https://pereirashouse.github.io/a-rede-parou/) são protótipos para configurar uma rede fictícia e investigar um incidente com registros simulados. O [pipeline pedagógico](https://pereirashouse.github.io/pipeline-pedagogico/) mostra como os casos de infraestrutura viram material de Computação.

A revisão de acessibilidade dos seis desafios implementados, no commit `e54bbd7` em **23/10/2026**, reforçou contraste, foco, atalhos e mensagens. A [execução na main](https://github.com/pereirashouse/simulador-configura-o-roteador/actions/runs/39971280418) aprovou **58 execuções: 29 cenários em duas telas Chromium**, sem retentativas. A [suíte de acessibilidade](https://github.com/pereirashouse/simulador-configura-o-roteador/blob/e54bbd707a92e54072cdd336815a09ac995e59f4/tests/acessibilidade.spec.cjs) acrescenta 10 cenários por tela, incluindo análise axe-core A/AA nos estados examinados, teclado, erros associados, 320 px e movimento reduzido. Os critérios didáticos foram preservados. A avaliação com tecnologias assistivas e usuários é uma etapa manual futura; os relatórios mantêm itens inconclusivos para revisão humana.

Público, autoria e limitações de cada material estão na página do projeto.

## Visualizar localmente

O site é estático, sem etapa obrigatória de compilação. Com Git e Python 3 instalados:

```bash
git clone https://github.com/pereirashouse/pereirashouse.github.io.git
cd pereirashouse.github.io
python3 -m http.server 8000 --bind 127.0.0.1
```

Abra `http://127.0.0.1:8000/`. Para interromper o servidor, use Ctrl+C. O endereço local não publica o site na internet.

## Uso offline

Para preservar a aparência e todos os links internos, baixe ou clone **o repositório completo**, incluindo `assets/`, e execute o servidor local. As fontes do portfólio são servidas de `assets/fonts/`, sem solicitação ao Google Fonts.

Os laboratórios `operacao-anzol/`, `rede-da-escola/` e `a-rede-parou/` têm a lógica e os estilos da atividade no próprio `index.html`. É possível baixar esse arquivo e abri-lo no navegador sem conexão; se os recursos locais de fontes não estiverem junto dele, o navegador usa fontes de sistema. Links externos e materiais hospedados em outros serviços continuam exigindo internet. Uma visita ao site não garante que a URL poderá ser reaberta offline depois.

## Organização

- `index.html`: página inicial, trilhas e arquivo de projetos.
- `projetos/`: estudos de caso de infraestrutura.
- `educacao/`: apresentação de projetos educacionais.
- `operacao-anzol/`, `rede-da-escola/` e `a-rede-parou/`: atividades interativas.
- `pipeline-pedagogico/`: visualização da transposição didática.
- `assets/`: estilos, scripts e fontes locais compartilhados.
- `curriculo/`: fontes HTML, geradores e PDFs dos currículos de TI e educação.

### Atualizar os currículos

Edite o conteúdo compartilhado em `curriculo/gerar.py` e regenere os HTML e PDFs juntos. Para a conversão em Python, instale Playwright e seu Chromium uma vez:

```bash
python3 -m pip install playwright
python3 -m playwright install chromium
python3 curriculo/gerar.py
python3 curriculo/renderizar-pdf.py
```

O gerador também detecta Chromium instalado no sistema; `CHROMIUM_PATH` permite indicar um executável específico. As fontes são locais. O script `curriculo/gerar-pdf.mjs` continua disponível como alternativa para ambientes com Playwright Node.

## Privacidade e interpretação dos resultados

Os estudos de caso generalizam ou omitem nomes de empresas, domínios, servidores, endereços, credenciais e outros dados internos. Os exemplos públicos não devem ser interpretados como configurações prontas para produção. Reconstruções sintéticas são identificadas como tal, e resultados de amostras curtas não representam garantia de longo prazo.

“Implantação concluída” descreve a entrega do projeto; “em produção” descreve seu estado operacional. Hipóteses em investigação e protótipos publicados são indicados separadamente.

## Reutilização e fontes

As fontes Familjen Grotesk, Public Sans, JetBrains Mono, Archivo e Atkinson Hyperlegible foram convertidas para WOFF2 sem alteração de glifos. Suas licenças SIL Open Font License estão em `assets/fonts/` e se aplicam às respectivas fontes, não automaticamente ao código e aos materiais deste portfólio.

Este repositório não declara uma licença geral para o código ou os materiais. Para reutilização, consulte o autor e eventuais condições específicas dos projetos vinculados.

## Autor

Jeferson Luiz Pereira — infraestrutura de TI e ensino de Computação.
