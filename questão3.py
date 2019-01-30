
class Fila():

  def __init__(self):
    self.fila = []
    self.MaximoAtendimento=0

  def Peek(self):
    tamanho= len(self.lista)
    return self.fila[0]

  def length (self):
    return len(self.fila)

  def enqueue(self):
    ordem= int(input("qual a ordem de chegada do cliente?"))

    if len(self.fila)==0:
      print("alcançou ao maximo de agendamento")
      self.MaximoAtendiento=1

    if self.MaximoAtendimento==0:
      self.fila.append(ordem)

  def dequeue(self):

    if len (self.fila==0):
      print ("não há agendamentos")

    else:
      self.fila.pop()

  def length (self):
    return len(self.fila)

  def isEmpty(self):
    if len(self.fila)==0:
      print("nada agendado")
    
    else:
      print("contem",self.fila)