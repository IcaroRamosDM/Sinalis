# Histórico do Sinalis

## 0.16.0 — preparação da 1.0

- Recuperação opcional de capturas, configurações e rascunhos após falhas; cópia
  em segundo plano, controle de instância e retomada como trabalho não salvo.
- Temporários interrompidos de recuperação preservados com nome novo.
- Histórico limitado de desfazer/refazer para modelos e filtros, inclusive
  campos incompletos, sem cópias de capturas.
- Exercícios sintéticos guiados de nove etapas e senoide de 100 Hz.
- Rotina de verificação de release, benchmark com até um milhão de pontos,
  regressões em diferentes escalas e teste de interrupção de gravação.
- Contratos de compatibilidade e roteiro de aceitação da 1.0 documentados.
- Aceitação humana e execução nativa Windows permanecem pendentes; esta versão
  não recebe o selo 1.0.


## 0.15.1 — 02/11/2026

Esta distribuição reúne os recursos da linha 0.15 e uma revisão de robustez,
legibilidade dos fontes privados e experiência de uso.

- Sessões portáteis, comparação de capturas e medições condicionadas aos dados.
- Cadeias de até 16 filtros e avaliação de arquivos em lote.
- Exportações PNG/SVG/PDF/HTML e CSV de espectro, picos e diferenças.
- Indicação de alterações da sessão, com salvar/descartar/cancelar ao fechar ou
  substituir o trabalho. Cancelar o salvamento preserva a sessão aberta.
- Proteção unificada de capturas, modelos, referências e sessão contra destinos
  equivalentes, vínculos e sobrescritas indevidas.
- Correção da validação de entradas/saídas armazenadas em sessões, incluindo
  saídas inativas. Texto inválido da interface é recusado antes da restauração.
- Ajuda contextual por teclado, guia interno, atalhos, foco visível e contraste
  revisto, mantendo a identidade do aplicativo.
- Verificações numéricas, sanitizadores, falhas de alocação, análise estática,
  regressões gráficas e testes dos pacotes Linux.

A execução nativa Windows continua como validação externa pendente. O pacote
x64 é compilado e inspecionado; testes Linux/Xvfb não substituem essa etapa.

## 0.14.2

Distribuição pública anterior, com análise, geração, filtros, critérios,
Lagrange, envelope, espectro e pacotes Windows/Linux. Seus downloads continuam
disponíveis na página de releases.
