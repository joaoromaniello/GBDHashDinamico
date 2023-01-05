# HASH DINÂMICO
Este projeto consiste em uma implementação de uma estrutura de dados de hash dinâmico e de uma estrutura de dados de árvore de busca em Python para a disciplina de Gerênciamento de Banco de dados do curso de Ciência da computação.

A estrutura de dados de hash dinâmico permite as operações de busca, inserção e remoção de registros utilizando uma chave NSEQ. Quando uma posição na tabela hash tem mais registros do que o número máximo permitido, o tamanho da tabela é automaticamente aumentado.

A estrutura de dados de árvore de busca permite as operações de busca, inserção e remoção de registros utilizando uma chave TEXT.

Para utilizar as estruturas de dados, basta instanciar a classe TabelaHash ou ArvoreBusca e chamar as funções de busca, inserção e remoção conforme necessário.

Exemplos de uso das estruturas de dados estão incluídos no código fornecido.

## **Exemplo de representação de uma tabela utilizando a alternativa 1**:

| NSEQ | TEXT       |                         
|------|------------|
| 1    | Registro 1 |           
| 2    | Registro 2 |
| 3    | Registro 3 |
| 4    | Registro 4 |
| 5    | Registro 5 |
| 6    | Registro 6 |

## **Exemplo de representação de uma tabela utilizando a alternativa 3**:
| Índice | Chave do índice | RIDs |
|--------|-----------------|------|
| 0      | Carlos          | 3    |
| 1      | Ana             | 1, 9 |
| 2      | Bruno           | 2, 7 |



  # **COMO UTILIZAR** <br>
 A utilização de cada uma delas foi representada nas classes main de acordo com o nome de cada uma, sendo assim, para visualizar cada uma das indexações basta ir na classe main correspondente, adicionar registro utilizando a função **inserir**, e imprimir.
 
   ## **hashAlt3Text**: 
  Classe responsavel pela indexação utilizando a alternativa 3 para indices baseados no campo TEXT  <br>
  ## **hashNSeq**:
  Classe responsavel pela indexação utilizando a alternativa 1 para indices baseados no campo NSEQ  <br>
  ## **hashText**:
  Classe responsavel pela indexação utilizando a alternativa 1 para indices baseados no campo TEXT<br>


Espero que este projeto possa ser útil para você e que possa contribuir para o seu aprendizado. Qualquer dúvida ou sugestão, fique à vontade para entrar em contato ou fazer uma pergunta na seção de issues do GitHub. Agradeço a sua visita e espero vê-lo novamente em breve!
