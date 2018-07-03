# pln-python

Este trabalho foi desenvolvido para a disciplina de Inteligência Artificial I (Ciência da Computação - UEM) em Julho/2018 por
  
- Ricardo Henrique Brunetto (ra94182@uem.br)
- Thiago Kira (ra78750@uem.br)

## Descrição

Este trabalho visa a aplicar processamento de linguagem natural em artigos do padrão IEEE para extração de informações relevantes, como por exemplo:
  
- Título
- Autores
- Seções
- Referências
- Top 10 termos mais citados

Sendo a solução proposta através da construção de uma gramática para o artigo, fazendo uso de um *analisador léxico* e de um *interpretador*.

## Especificações Tecnológicas

Todo o programa foi escrito em `python`. As seguintes bibliotecas foram utilizadas:

- PLY       (`sudo pip install ply`)
- NLTK      (`sudo pip install nltk`)
- PDFMiner  (`sudo pip install pdfminer`)

Deve-se ter a disposição uma pasta na raiz do projeto nomeada `files`, contendo todos os arquivos em formato `.pdf` que se deseja aplicar a análise.

Então, basta executar o script `main.py` através do seguinte:
`python main.py`

## Implementação

Alguns detalhes de implementação constam no documento de apresentação, disponível [aqui](slides.pdf).

### Limitações e Sugestões

- Ficaram pendentes as seguintes funcionalidades:
  - Separar autor e título
  - Identificar o problema do artigo
  - Identificar o objetivo do artigo
  - Identificar a solução proposta no artigo
  - Interface gráfica
- Sugere-se aperfeiçoar a forma como os dados estão sendo salvos e refinar as referências bibliográficas.

## Licença

Este projeto segue a licença [Creative Commons Attribution-ShareAlike (BY-SA)](https://creativecommons.org/licenses/by-sa/4.0/), que está detalhada no arquivo [`LICENSE.md`](LICENSE.md).
<p align="center">
  <img src="https://licensebuttons.net/l/by-sa/3.0/88x31.png">
</p>
