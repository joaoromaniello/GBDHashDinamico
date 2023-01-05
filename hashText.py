class Elemento:
  def __init__(self, registro):
    self.registro = registro
    self.proximo = None

class Registro:
  def __init__(self, nseq, text):
    self.nseq = nseq
    self.text = text

class TabelaHash:
  def __init__(self, tamanho=5):
    self.tamanho = tamanho
    self.tabela = [None] * self.tamanho

  def hash(self, text):
    # Implementar a função de hash aqui
    # Exemplo: retornar o tamanho do texto modulo o tamanho da tabela
    return len(text) % self.tamanho

  def inserir(self, registro):
    posicao = self.hash(registro.text)
    elemento = Elemento(registro)
    elemento.proximo = self.tabela[posicao]
    self.tabela[posicao] = elemento

  def buscar(self, text):
    posicao = self.hash(text)
    elemento = self.tabela[posicao]
    while elemento is not None:
      if elemento.registro.text == text:
        return elemento.registro
      elemento = elemento.proximo
    return None

  def remover(self, text):
    posicao = self.hash(text)
    elemento = self.tabela[posicao]
    anterior = None
    while elemento is not None:
      if elemento.registro.text == text:
        if anterior is None:
          self.tabela[posicao] = elemento.proximo
        else:
          anterior.proximo = elemento.proximo
        return elemento.registro
      anterior = elemento
      elemento = elemento.proximo
    return None

  def imprimir(self):
    for i in range(self.tamanho):
      elemento = self.tabela[i]
      print("Posição {}:".format(i), end=" ")
      while elemento is not None:
        print("[{}]".format(elemento.registro.text), end=" ")
        elemento = elemento.proximo
      print()