# Componentes de terceiros

As permissões de uso pessoal, educacional e comercial do Sinalis dizem respeito
ao programa do autor. Não substituem nem restringem as licenças dos componentes
de terceiros. Estes continuam sujeitos aos seus próprios termos.

## FLTK 1.4.5

Sinalis is based in part on the work of the FLTK project (https://www.fltk.org).

FLTK utiliza a GNU Library General Public License v2 com exceções próprias,
incluindo a exceção para ligação estática de aplicações. A distribuição utiliza
a biblioteca oficial, configurada para a plataforma, sem alterações em seu
código-fonte.

Texto completo: `licenses/FLTK-COPYING.txt`.
[Projeto e licença](https://www.fltk.org/doc-1.4/license.html).

## cJSON 1.7.19

Copyright (c) 2009–2017 Dave Gamble and cJSON contributors. Licença MIT.

Texto completo: `licenses/cJSON-LICENSE.txt`.
[Projeto](https://github.com/DaveGamble/cJSON/tree/v1.7.19).

## Bibliotecas de imagens incluídas pelo FLTK

- **libpng:** avisos e licença em `licenses/libpng-LICENSE.txt`.
- **zlib:** avisos e licença em `licenses/zlib-README.txt`.
- **Independent JPEG Group / libjpeg:** avisos e condições em
  `licenses/libjpeg-README.txt`.

This software is based in part on the work of the Independent JPEG Group.

Esses componentes dão suporte à interface. Sua presença não significa que
o Sinalis importe sinais a partir de fotografias.

## Runtime Windows

O pacote Windows incorpora componentes de runtime do GCC/MinGW-w64.
Os avisos fornecidos pela distribuição das ferramentas estão em:

- `licenses/MinGW-w64-copyright.txt`;
- `licenses/GCC-MinGW-copyright.txt`, incluindo a GCC Runtime Library Exception;
- `licenses/GPL-3.txt`, texto da licença referenciada pelos avisos do GCC.

Esses avisos abrangem o conjunto de ferramentas; não significam que todos os
componentes listados nesses documentos estejam presentes no executável.
[Exceção do runtime GCC](https://www.gnu.org/licenses/gcc-exception-3.1.en.html).

## Bibliotecas do sistema Linux

O pacote `.deb` depende de bibliotecas do sistema, resolvidas pelo APT. Não
redistribui cópias de glibc, libstdc++ ou bibliotecas X11 dentro do instalador.
Os avisos desses pacotes ficam nos diretórios correspondentes em
`/usr/share/doc` do sistema. Os textos Windows acima são incluídos apenas no
pacote Windows.
