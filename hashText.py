class Registro:
  def __init__(self, text, rid):
    self.text = text
    self.rid = rid

class NoArvore:
  def __init__(self, registro):
    self.registro = registro
    self.esquerda = None
    self.direita = None

  def getEsquerda(self):
    return self.esquerda

class ArvoreBusca:
  def __init__(self):
    self.raiz = None

  def buscar(self, text):
    atual = self.raiz
    while atual:
      if atual.registro.text == text:
        return atual.registro
      elif atual.registro.text > text:
        atual = atual.esquerda
      else:
        atual = atual.direita
    return None

  def inserir(self, registro):
    novo_no = NoArvore(registro)
    if self.raiz is None:
      self.raiz = novo_no
    else:
      atual = self.raiz
