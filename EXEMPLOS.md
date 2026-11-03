# Exemplos guiados

Abra **Sessão → Exemplos guiados…**, escolha o exercício e clique em
**Abrir captura do exemplo**. Se estiver trabalhando com outra captura, salve
sua sessão antes de trocar.

## Medições por etapas

O exemplo contém nove posições em milímetros, na ordem `0, 1, 2, 3, 4, 3, 2, 1, 0`.
O eixo X indica o número da etapa. O arquivo `examples/guided/TEST_etapas.json`
contém os limites usados no exercício.

1. Abra **Medições por etapas** e clique em **Avaliar modelo**. O resultado é **Aprovado**. O máximo é 4 mm na etapa 5 e o sinal volta a 0 mm na etapa 9.
2. Na regra do máximo, troque a faixa de 3,75 a 4,25 mm por `0` a `3.5` mm e avalie outra vez. O máximo de 4 mm agora ultrapassa o limite. O resultado passa a **Reprovado**.
3. Use **Sessão → Desfazer edição do modelo/filtro** até recuperar os dois limites anteriores. Clique em **Avaliar modelo** para atualizar o resultado.

## Sinal temporal e filtragem

O segundo exemplo é uma senoide de 100 Hz e amplitude de 1 V. A captura tem
1.000 amostras a 10.000 amostras por segundo.

1. Abra **Sinal temporal e filtragem**. Em **Caracterização**, a média fica próxima de zero, o valor RMS próximo de 0,7071 V e o pico a pico em 2 V.
2. Em **Medir características…**, use os níveis manuais `-1` e `1` V. O período é de 10 ms e o ciclo ativo fica próximo de 50%.
3. No espectro de amplitude, selecione a janela retangular e localize o pico de 100 Hz.
4. Na aba **Filtro**, clique em **De Validação**, escolha **Média móvel** com janela de 5 amostras e aplique. Compare a amplitude da saída com a da senoide original.

Use **Sessão → Salvar sessão…** para guardar a captura e os ajustes do exercício.
