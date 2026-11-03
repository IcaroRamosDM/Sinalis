# Formatos de arquivo

O Sinalis 0.16.0 abre sinais em JSON e tabelas numéricas em CSV ou TXT. Se um
JSON contiver mais de uma série, a prévia permite escolher qual importar.
Confira as unidades de X e Y antes de comparar capturas. Alterar o nome de uma
unidade mantém os valores numéricos.

| Arquivo | O que guarda | Leitura | Gravação |
|---|---|---|---|
| `TEST_*.json` | Critérios de um modelo | Versões 1 a 9 | Versão 9 |
| `sinalis-filter` | Configuração de um filtro | Versões 1 a 3 | Versão 3 |
| `sinalis-chain` | Cadeia de filtros | Versão 1 | Versão 1 |
| `.sinalis` | Capturas e estado da sessão | Versão 1 | Versão 1 |
| `sinalis-signal` | Sinal exportado em JSON | `format_version` 1 | `format_version` 1 |
| `waveform-evaluation` | Resultado da avaliação | Amostras, quando presentes | `format_version` 1 |

CSV e TXT exportados usam ponto decimal e trazem um cabeçalho com os metadados.
O zoom aplicado ao gráfico não muda a quantidade de amostras exportadas.

## Cópia de recuperação

Se você ativar **Sessão → Recuperação automática…**, o Sinalis guarda a cópia
na pasta de estado do seu usuário.

| Sistema | Pasta |
|---|---|
| Linux | `$XDG_STATE_HOME/Sinalis/recovery` ou, por padrão, `~/.local/state/Sinalis/recovery` |
| Windows | `%LOCALAPPDATA%\Sinalis\recovery` |

Ao recuperar uma cópia, use **Salvar sessão…** para escolher um arquivo
permanente. Se o Sinalis informar que a recuperação está em uso, outra instância
pode estar gravando na mesma pasta. Um arquivo `.partial` nessa pasta é uma
gravação interrompida.

[Como salvar e reabrir uma sessão](USO.md)
