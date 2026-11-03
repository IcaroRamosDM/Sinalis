# Verificação da versão 0.15.1

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
