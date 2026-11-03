# Guia de uso do Sinalis 0.15.1

O Sinalis analisa arquivos locais. Uma tela de pelo menos 1024 × 660 permite
usar a interface; 1280 × 900 oferece mais espaço para gráficos e critérios.

## Começar por uma captura

1. Clique em **Abrir sinal…** e escolha um JSON, CSV ou TXT numérico.
2. Se o arquivo contiver vários conjuntos possíveis, confira a prévia e escolha
   o sinal correto. Uma recuperação de arquivo defeituoso exige confirmação.
3. Em **Caracterização**, confira os pontos, as unidades e os metadados.
4. Em **Validação**, configure ou carregue o modelo que representa seu ensaio.
5. Clique em **Avaliar modelo** e confira os resultados e suas justificativas.

O sinal que acompanha a abertura do programa é um exemplo. Os limites dos
modelos de demonstração são fictícios. Editar a unidade de X muda a
identificação, sem converter os números.

## Modelo e sessão

**Salvar modelo…** guarda os critérios em `TEST_nome.json`. É útil para aplicar
as mesmas exigências a outras capturas. Alterações do modelo precisam ser
avaliadas ou salvas antes de exportar um resultado atualizado.

**Sessão → Salvar sessão…** guarda o trabalho completo em `.sinalis`: sinais,
modelo, estado dos filtros, configurações, observações, campos em edição e
visualização. Campos numéricos ainda incompletos podem ser guardados sem
aplicá-los. Ao retomar, a sessão utiliza os dados que contém; não abre
automaticamente os caminhos históricos registrados nela.

O asterisco no título indica alterações ainda não guardadas na sessão. Ao
fechar ou abrir outra sessão, você pode salvar, descartar ou cancelar a ação.
Cancelar a escolha do arquivo de salvamento também cancela a substituição.

Salvar um modelo ou exportar um sinal não substitui salvar a sessão. Mantenha
cópias de segurança dos arquivos importantes.

## Entender a avaliação

- **Aprovado:** os dados atenderam aos critérios configurados.
- **Reprovado:** pelo menos uma exigência necessária falhou.
- **Inconclusivo:** algum dado ou condição impediu a conclusão; leia o motivo.
- **Sem critérios:** nenhum requisito de aprovação foi ativado.

Em **Todos passarem**, cada regra ativa é necessária. Em **Pelo menos um
passar**, basta uma. Em **Parcial**, todas as regras do mesmo conjunto precisam
passar; basta um conjunto completo aprovado.

Mostrar a curva de Lagrange não ativa sua validação. Nós utilizados na
construção da curva não constituem uma comparação independente. Envelope e
critérios de Lagrange habilitados acrescentam suas próprias exigências.

## Comparar e medir

**Comparar capturas…** recebe uma referência e informa erros e diferenças.
Escolha entre coordenadas exatas e interpolação linear explícita. O programa
confere domínios e unidades; não extrapola a referência nem converte unidades
automaticamente. Correlação pode ficar indisponível para sinais constantes.

**Medir características…** localiza picos e, quando há base temporal regular
e transições suficientes, calcula período, frequência, duty e tempos de
subida/descida. O overshoot exige níveis de referência manuais. Um resultado
indisponível não é substituído por zero nem se torna um critério de aprovação
automaticamente.

## Gerar e filtrar

Em **Laboratório**, configure a forma de onda, quantidade/duração, frequência e
níveis antes de gerar. Ruído com semente fixa permite repetir o experimento.
Envie uma cópia para **Validação** ou **Filtro** quando desejar.

Em **Filtro**, confira a amostragem, escolha o processamento e compare a entrada
com a saída. Sugestões são heurísticas; características úteis também podem ser
suavizadas. Um processamento demorado permite navegar por outras abas; aguarde
sua conclusão antes de substituir a sessão.

**Cadeia de filtros…** permite organizar até 16 etapas, desativar ou reordenar
filtros e experimentar uma parte da cadeia. Cada execução começa pela entrada.

## Lotes e exportações

**Avaliar pasta…** aplica um modelo ou procura os `TEST_` correspondentes às
capturas selecionadas. O processamento não percorre subpastas nem segue links
de arquivos. Confira o resumo CSV: ele distingue avaliações, arquivos
existentes, erros e cancelamento.

No fluxo de arquivos, `ensaio.json` corresponde a `TEST_ensaio.json` e produz
`EVAL_ensaio.json`. Os originais são preservados; um relatório existente exige
uma decisão de sobrescrita.

**Exportar sinal…** guarda todas as amostras em JSON, CSV ou TXT, com metadados.
O zoom não reduz essa exportação. CSV/TXT utilizam ponto decimal e um cabeçalho
de metadados que o Sinalis consegue reimportar.

**Gráficos e relatório** oferece PNG, SVG, PDF e HTML. PNG representa o gráfico
visível; os relatórios utilizam os dados completos da avaliação. PDF inclui a
configuração no anexo `configuracao.json`; HTML apresenta a configuração no
próprio documento. Há também exportação CSV para espectro, picos e diferenças.

## Atalhos

| Tecla | Ação |
|---|---|
| Ctrl+1 a Ctrl+4 | Validação, Caracterização, Laboratório e Filtro |
| Ctrl+O | Abrir sinal |
| Ctrl+Shift+O | Abrir sessão |
| Ctrl+Shift+S | Salvar sessão |
| Ctrl+S | Salvar modelo em Validação, configuração em Filtro ou sessão nas outras abas |
| Ctrl+Enter | Avaliar, gerar ou aplicar filtro na aba correspondente |
| Tab / Shift+Tab | Percorrer os controles |
| F1 | Ajuda do campo em foco; guia quando não há ajuda contextual |
| Espaço / Enter no ícone (?) | Mostrar a explicação |
| Esc na janela principal | Dispensar ajuda |
| Ctrl+Q | Fechar, verificando alterações da sessão |

O menu **Sessão → Ajuda e atalhos…** oferece o guia dentro do aplicativo.

## Quando um resultado parecer estranho

Confira primeiro o arquivo escolhido, unidades, taxa de amostragem, critérios
ativos e avisos de recuperação. Considere a quantidade de amostras disponível:
poucos pontos não permitem inferir o movimento entre eles.

Para relatar um problema, informe versão, sistema, passos e resultado esperado.
Compartilhe somente exemplos que possam se tornar públicos. O Sinalis não
substitui calibração, ensaios físicos ou validação técnica independente.
