# Face Recognition

O projeto consiste em um simples `AWS Lambda` para realizar o reconhecimento facial.

### Sobre o projeto:

A projeto é constituída por 2 buckets `S3`, sendo um deles responsável por armezenar um site estático, cujo o objetivo é apresentar os resultados do reconhecimento facial em uma simples tabela com os seguintes campos: miniatura da foto, nome da pessoa reconhecida e percentual de similaridade.
O outro bucket é responsável por armazenar o nosso banco de imagens e também por ser o `trigger` que dispara o `Lambda` que osquestra essa tarefa.
O nosso `Lambda` é responsável por identificar todas as imagens adicionadas em nosso bucket, quando uma nova imagem com o padrão de nomenclatura `_analyze.jpg` é adicionada em nosso bucket, o `Lambda` pega essa imagem, faz o processo de reconhecimento e monta uma resposta no formato `JSON` e envia isso para o nosso bucket do site estático para que o resultado seja exibido nessa camada de frontend.
O processo de reconhecimento facial é tratado pelo `Rekognition`, serviço responsável por indexar as imagens e realizar o reconhecimento de uma face qualquer fornecida para análise.


### Arquitetura:

[![node](https://github.com/jonathanmdr/face-rekognition-lambda/blob/master/docs/rekognition.png)](https://github.com/jonathanmdr/face-rekognition-lambda/blob/master)
