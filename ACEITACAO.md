# Aceitação rumo à versão 1.0

A 0.16.0 é uma versão de preparação. A execução nativa Windows e a aceitação
humana com capturas reais ainda precisam de evidência. Testes automáticos,
compilação e conferência de arquivos têm alcance próprio.

## Registrar uma execução

Anote versão, sistema/desktop, resolução, escala, origem do pacote e SHA-256.
Registre os passos, resultado esperado, resultado observado e qualquer erro.
Use uma cópia de capturas reais e preserve seus originais. Dados pessoais e
capturas privadas não devem ser anexados publicamente; é possível comunicar
um defeito com exemplo sintético mínimo e sem informações sensíveis.

## Roteiro comum

1. Instale/extraia o pacote em uma máquina sem o ambiente de desenvolvimento.
   Abra pelo menu/Explorador, confira a versão e execute os
   [dois exercícios guiados](EXEMPLOS.md).
2. Importe uma captura real por etapas. Confira o conjunto escolhido, unidades,
   posições e critérios com uma referência independente revisada pelo responsável
   pelo ensaio. Compare os resultados por condição, incluindo inconclusivos.
3. Repita com uma captura temporal real, conferindo taxa, regularidade, medições
   aplicáveis e efeito dos filtros. Um filtro não deve esconder um defeito para
   tornar a captura aprovada.
4. Salve uma sessão com observações e campos ainda em edição, feche e reabra.
   Confira dados, rascunhos e parâmetros. Exporte e leia PDF/HTML e tabelas.
5. Teste salvar, descartar e cancelar ao fechar/substituir o trabalho, incluindo
   cancelar a janela de seleção do destino. Confira a proteção das entradas.
6. Ative recuperação opcional em uma sessão de teste, espere pelo menos
   30 segundos após editar e confira a indicação de cópia atualizada no menu.
   Se realizar uma interrupção deliberada, use somente esse trabalho descartável.
   Reabra e escolha recuperar, manter para depois ou descartar. Confira o estado
   recuperado e salve uma sessão permanente. Não é um teste de falta de energia.
7. Percorra os controles por teclado, abra ajuda, teste desfazer/refazer e
   confirme a legibilidade nas escalas/resoluções utilizadas. Registre cortes,
   sobreposições, foco perdido e ações difíceis de descobrir.
8. Uma pessoa que não conhece o programa deve completar importação, avaliação,
   interpretação de inconclusivo, sessão e relatório com a documentação, sem
   orientação constante do desenvolvedor.

## Linux

Verifique abertura pelo menu, diálogos de arquivos, permissões, fontes e símbolos
matemáticos, caminhos com espaços/acentos, PDF/HTML e retomada de sessão.
O layout mínimo é 1024×660 unidades lógicas de tela, além da decoração da janela;
a escala pode exigir uma resolução física maior. Registre o desktop e o modo
X11/Wayland utilizados. Testes em Xvfb não comprovam esta inspeção humana.

## Windows

Extraia o ZIP completo e use `Sinalis.exe`; não é necessário WSL, Python ou
permissão de administrador. Execute os mesmos cenários, incluindo pastas com
acentos/espaços, seletor de arquivos, retomada e diferentes escalas de tela.
Registre a edição/versão do Windows e o hash do pacote.

O mantenedor também possui uma rotina PowerShell de regressões nativas. Seu
resultado só conta depois de executado realmente no Windows; não substitui o
roteiro humano. Se uma política de segurança impedir a execução, registre o
bloqueio. Não desative antivírus nem contorne AppControl.

## Resultado necessário

Uma falha que provoque perda de dados, resultado incorreto, incompatibilidade
não explicada ou impossibilidade de concluir um fluxo bloqueia a 1.0. Corrigir,
repetir os casos afetados e identificar a versão efetivamente aceita. Melhorias
estéticas menores podem ser registradas para evolução posterior.
