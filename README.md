# HASH DINÂMICO
Este projeto consiste em uma implementação de uma estrutura de dados de hash dinâmico e de uma estrutura de dados de árvore de busca em Python para a disciplina de Gerênciamento de Banco de dados do curso de Ciência da computação.

A estrutura de dados de hash dinâmico permite as operações de busca, inserção e remoção de registros utilizando uma chave NSEQ. Quando uma posição na tabela hash tem mais registros do que o número máximo permitido, o tamanho da tabela é automaticamente aumentado.

A estrutura de dados de árvore de busca permite as operações de busca, inserção e remoção de registros utilizando uma chave TEXT.

Para utilizar as estruturas de dados, basta instanciar a classe TabelaHash ou ArvoreBusca e chamar as funções de busca, inserção e remoção conforme necessário.

Exemplos de uso das estruturas de dados estão incluídos no código fornecido.

| NSEQ | TEXT       |
|------|------------|
| 1    | Registro 1 |
| 2    | Registro 2 |
| 3    | Registro 3 |
| 4    | Registro 4 |
| 5    | Registro 5 |
| 6    | Registro 6 |


Repare que no projeto existem varias classes, sendo elas: 
  hashAlt3Text: classe responsavel pela indexação utilizando a alternativa 3 para indices baseados no campo TEXT  <br>
  hashNSeq: classe responsavel pela indexação utilizando a alternativa 1 para indices baseados no campo NSEQ  <br>
  hashText: classe responsavel pela indexação utilizando a alternativa 1 para indices baseados no campo TEXT<br>
  
 A utilização de cada uma delas foi representada nas classes main de acordo com o nome de cada uma
