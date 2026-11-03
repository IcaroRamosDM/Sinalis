# Exercícios guiados — Sinalis 0.16.0

Abra **Sessão → Exemplos guiados…**. Cada exercício informa seus resultados
esperados e permite abrir a captura correspondente. Abrir substitui a captura
e o modelo de Validação após a decisão sobre alterações pendentes. As capturas
são sintéticas; os critérios são didáticos.

## 1. Medições por etapas

O arquivo `examples/guided/etapas.json` contém nove posições:
`0, 1, 2, 3, 4, 3, 2, 1, 0 mm`, em etapas 1–9. O modelo
`examples/guided/TEST_etapas.json` exige nove pontos, máximo entre 3,75 e 4,25 mm,
retorno de até 0,1 mm e evolução sem inversões em cada trecho.

1. Abra o exemplo de etapas e clique em **Avaliar**.
2. Confira **APROVADO**, máximo de 4 mm no ponto 5 e retorno de 0 mm.
3. Nos limites do máximo, coloque inferior `0` e superior `3.5`; avalie novamente.
   O resultado esperado é **REPROVADO**, com explicação no critério do máximo.
4. Use **Sessão → Desfazer edição do modelo/filtro** para retomar os campos.
   Avalie novamente para atualizar o resultado.
5. Salve uma sessão `.sinalis` em uma pasta pessoal. Exporte um relatório e
   confira os dados, unidades e limites. Reabra a sessão e verifique a retomada.

Sem base temporal, este conjunto não permite inferir frequência ou tempo de
resposta. Aprovar o exemplo não significa aprovar uma peça física.

## 2. Sinal temporal e filtragem

O arquivo `examples/guided/senoide.json` contém 1.000 amostras de uma senoide
de 100 Hz, amplitude 1 V e amostragem de 10.000 amostras/s.

1. Abra o exemplo temporal. Em **Caracterização**, confira média próxima de
   zero, RMS próximo de 0,707107 V e pico a pico de 2 V.
2. Em **Medir características**, escolha níveis manuais baixo `-1` e alto `1`.
   Espere período de 0,01 s, frequência de 100 Hz e duty próximo de 50%.
3. No espectro de amplitude, use janela retangular e confira o pico em 100 Hz.
   A resolução/janela escolhida afeta os valores apresentados no espectro.
4. Na aba **Filtro**, copie **De Validação**, selecione média móvel, janela de
   5 amostras e aplique. Compare a entrada preservada com a saída; o filtro
   também altera amplitude e bordas. Ele não é uma recomendação universal.
5. Salve uma sessão e exporte o gráfico/relatório para repetir a análise.

O exemplo temporal começa sem critérios de aprovação. Acrescentá-los exige
escolher uma especificação adequada ao objetivo do ensaio.

## Recuperar e rever

Ative cópias locais em **Sessão → Recuperação automática…** se desejar. Elas
não marcam a sessão como salva. O histórico de desfazer/refazer guarda campos
e configurações, sem duplicar amostras; não persiste entre execuções.
Consulte [compatibilidade e limites](COMPATIBILIDADE.md).
