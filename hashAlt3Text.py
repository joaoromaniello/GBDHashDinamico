class Registro:
  def __init__(self, nseq, text):
    self.nseq = nseq
    self.text = text

class Elemento:
  def __init__(self, nseq, text):
    self.registro = Registro(nseq, text)
    self.rids = []
    self.proximo = None

class TabelaHash:
  def __init__(self):
    self.tamanho = 10
    self.tabela = [None] * self.tamanho

  def hash(self, text):
    return hash(text) % self.tamanho

  def inserir(self, nseq, text):
    posicao = self.hash(text)
    elemento = self.tabela[posicao]
    while elemento is not None:
      if elemento.registro.text == text:
        elemento.rids.append(nseq)
        return
      elemento = elemento.proximo
    novo_elemento = Elemento(nseq, text)
    novo_elemento.rids.append(nseq)
    novo_elemento.proximo = self.tabela[posicao]
    self.tabela[posicao] = novo_elemento

  def buscar(self, text):
    posicao = self.hash(text)
    elemento = self.tabela[posicao]
    while elemento is not None:
      if elemento.registro.text == text:
        return elemento.rids
      elemento = elemento.proximo
    return None

  def imprimir(self):
    for i in range(self.tamanho):
      elemento = self.tabela[i]
      print(f"{i}: ", end="")
      while elemento is not None:
        print(f"{elemento.registro.text} ({elemento.rids}) -> ", end="")
        elemento = elemento.proximo
      print("None")