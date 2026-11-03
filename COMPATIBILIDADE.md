# Compatibilidade e preservação do trabalho

A 0.16.0 prepara a primeira versão estável do escopo offline. O compromisso
proposto para a 1.0 cobre os formatos e comandos anunciados, a preservação dos
originais e a explicação de alterações que afetem resultados.

| Documento | Leitura | Gravação |
|---|---|---|
| Modelo `TEST_` | Versões 1–9 | Versão 9 |
| Configuração `sinalis-filter` | Versões 1–3 | Versão 3 |
| Sessão `sinalis-session` | Versão 1 | Versão 1 |
| Cadeia `sinalis-chain` | Versão 1 | Versão 1 |
| Sinal `sinalis-signal` | `format_version` 1 | `format_version` 1 |
| Avaliação `waveform-evaluation` | Dados reimportáveis | `format_version` 1 |

A versão de um formato é independente da versão do aplicativo. Unidades são
declaradas, sem conversão automática. Números exportados usam ponto decimal e
até 17 algarismos significativos; textos usam UTF-8. A importação de JSON comum
continua limitada às estruturas reconhecidas, com escolha explícita quando
houver candidatos distintos.

Mudanças futuras de formato exigirão migração/diagnóstico explícitos. Mudanças
de cálculo com efeito observável precisarão de notas que expliquem diferenças;
compatibilidade numérica usa tolerâncias, sem promessa de identidade bit a bit
entre todos os compiladores e arquiteturas.

## Sessão, cópia de recuperação e backup

- Salvar modelo guarda critérios. Salvar sessão guarda capturas, parâmetros,
  visualização, observações e campos em edição.
- Recuperação automática começa desativada. Ao ativá-la, o Sinalis guarda uma
  cópia local a cada 30 segundos de alterações, em segundo plano. O intervalo
  pode aumentar enquanto há outra operação em andamento.
- No Linux, a pasta é `XDG_STATE_HOME/Sinalis/recovery` ou
  `~/.local/state/Sinalis/recovery`. No Windows, é
  `LOCALAPPDATA\Sinalis\recovery`. As cópias contêm dados da captura; ficam no
  computador e não são enviadas a um serviço.
- Uma instância por pasta pode escrever a cópia. Outra instância informa a
  indisponibilidade e continua funcionando.
- Uma cópia encontrada após falha exige uma escolha: recuperar, manter para
  depois ou descartar. Ela é protegida até essa decisão. O trabalho recuperado
  abre como não salvo, para você escolher o arquivo permanente.
- Temporários interrompidos da pasta de recuperação são preservados com nome
  novo `.partial`, permitindo novas cópias. Eles podem ser conferidos/removidos
  manualmente com o aplicativo fechado. Temporários nos destinos de exportação
  do usuário continuam preservados e provocam diagnóstico.
- Recuperação não substitui salvar nem fazer backup. CRC32 detecta corrupção
  acidental, sem autenticar a autoria. Não há garantia de recuperação após falta
  de energia, falha do disco ou alterações hostis simultâneas nos diretórios.

## Desfazer e refazer

O histórico guarda até 64 estados e 4 MiB por editor de modelo/filtro, somente
em memória. Capturas e saídas não são copiadas. Edições rápidas podem compor
uma etapa; antes de desfazer, o campo atual também é capturado.

Use o menu Sessão ou Ctrl+Alt+Z/Ctrl+Alt+Shift+Z para o editor completo.
Ctrl+Z dentro de um campo mantém o desfazer de texto habitual. Restaurar campos
não aplica filtros nem atualiza automaticamente uma avaliação. Abrir uma sessão
inicia um novo histórico.

## Sistemas

Linux: pacote amd64 dirigido a Ubuntu 24.04/26.04 e Debian 12/13. Windows: pacote
x64 portátil, cuja execução nativa continua pendente. Não são anunciados ARM,
macOS, aquisição de hardware em tempo real ou certificação industrial.
Consulte [verificações e limites](https://github.com/IcaroRamosDM/Sinalis/blob/v0.16.0/VALIDACAO.md) e [aceitação](ACEITACAO.md).
