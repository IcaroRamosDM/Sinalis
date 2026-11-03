# Verificação da versão 0.16.0

Revisão concluída em 02/11/2026, com núcleo C17 e interface C++17/FLTK.

## Ensaios realizados

- Regressões de importação, critérios, sinais, filtros, espectro, medições,
  comparação, sessões, cadeias, lotes e relatórios.
- **4.295.712 comparações numéricas independentes** com NumPy/SciPy.
- **11.029 verificações de segurança/formato** e **1.040 verificações CLI**,
  incluindo entradas e argumentos aleatórios com sementes registradas.
- **4.771 cenários de falha de alocação C** e 2.800 orçamentos de alocação cJSON.
- ASan/UBSan no núcleo e na interface; LSan no núcleo. A GUI foi exercitada em
  Xvfb e automaticamente na sessão gráfica do Ubuntu 26.04.1.
- Análise estática GCC, testes das ferramentas de build, formatação e exemplos
  compilados da documentação.
- **29 verificações adicionais de uso**, incluindo cancelamento, salvamento,
  foco/ajuda, proteção de arquivos e recusa de textos inválidos nas sessões.
- Leitura independente de PDF/SVG/HTML/PNG, com conferência de texto Unicode,
  páginas, anexo de configuração, escaping e pixels de teste.
- Instalação, dependências, registro de aplicativo, integridade, fluxo CLI e
  regressões gráficas do **instalador público final** em userlands isolados de
  Ubuntu 24.04/26.04 e Debian 12/13.
- ZIP Windows x64 conferido por conteúdo, CRC, SHA-256 e cabeçalhos PE. Os dois
  pacotes contêm aplicativo, exemplos e documentação/licenças de uso; os fontes
  privados e os dados pessoais ficam fora da distribuição.

Os números representam verificações e comparações automatizadas, incluindo
iterações de testes. Não correspondem a cenários humanos independentes nem a
uma medida de cobertura de todo o software.

## Preparação da 1.0

- 33 verificações novas da interface: desfazer/refazer, rascunhos incompletos,
  troca de família de filtro, recuperação opcional, exclusividade da pasta,
  corrupção, preservação de temporários e abertura dos exemplos guiados.
- Regressões gráficas em escalas 100%, 125%, 150% e 200%, com capturas para
  inspeção. Isso não constitui aceitação humana de legibilidade/acessibilidade.
- Processo de gravação interrompido durante uma sessão: arquivo anterior
  preservado e legível; temporário abandonado preservado. Não foi um ensaio de
  falta de energia ou de durabilidade do sistema de arquivos.
- Benchmark CLI com 1.000, 100.000 e 1.000.000 pontos: importação/estatísticas,
  média móvel/exportação, salvar/abrir sessão e PDF, com três repetições e
  registro de máquina, tempo total e pico de memória por processo.
- Evidências de aceitação identificam versão/artefato; testes automáticos não
  preenchem os registros de avaliação humana da 1.0.

Foram escolhidos dois conjuntos experimentais públicos: as duas séries de
20 observações do [NIST Pontius](https://www.itl.nist.gov/div898/strd/lls/data/LINKS/DATA/Pontius.dat)
e 121.265 amostras do canal drive end do ensaio 105 da
[CWRU, grupo a 12 kHz](https://engineering.case.edu/bearingdatacenter/12k-drive-end-bearing-fault-data).
Estatísticas, comparação de séries e filtragem foram conferidas com referências
numéricas independentes. São dados publicados de bancada; não houve novo ensaio
físico local nem certificação pelo NIST/CWRU.

No Pontius, X representa a ordem das observações, sem inferir tempo. O canal
CWRU é convertido externamente de MAT para CSV, sem reamostragem, com a taxa
publicada de 12.000 amostras/s. Unidades Y não confirmadas nas fontes consultadas
permanecem desconhecidas. Os dados originais/conversões não acompanham os pacotes;
as fontes e seus limites ficam registrados nas evidências de desenvolvimento.

A versão 1.0 continua dependente do [roteiro de aceitação](ACEITACAO.md).

## Dependências

FLTK 1.4.5 e cJSON 1.7.19 têm arquivos de origem verificados por SHA-256; cJSON
recebe um ajuste local de precisão numérica. Avisos conhecidos foram analisados
quanto ao código e às plataformas usados: `cJSON_Utils`/JSON Patch não são
integrados, `cJSON_Compare` não é chamado pelo aplicativo e a distribuição é
somente x86-64. Essa classificação de alcance não equivale a corrigir os avisos
no projeto upstream nem a garantir ausência de problemas futuros. Fontes:
[cJSON no Debian Security Tracker](https://security-tracker.debian.org/tracker/source-package/cjson)
e [documentação oficial FLTK](https://www.fltk.org/documentation.php).

## Limites explícitos

- **Execução nativa Windows permanece pendente.** Compilação, inspeção PE e
  testes Linux não substituem uso real em Windows, políticas de instituição ou
  antivírus.
- Userlands isolados e Xvfb não substituem aceitação humana em todos os desktops,
  escalas, equipamentos ou tecnologias assistivas. Não há certificação de
  acessibilidade ou adequação industrial.
- A verificação de leaks do processo gráfico exclui caches globais de fontes/X11
  de terceiros. O núcleo recebeu a checagem de leaks.
- Testes não garantem ausência absoluta de erros. Confira dados, unidades,
  critérios e resultados importantes para seu ensaio.

Os checksums dos arquivos efetivamente publicados acompanham a release em
`SHA256SUMS.txt`. Releases anteriores permanecem disponíveis para consulta.
