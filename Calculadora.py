import PySimpleGUI as sg

class Calculadora:
  def __init__(self):
    self.digitando = True
    self.numeros = ""
    
  def Iniciar(self):
    #Layout
    
    self.layout = [
      [sg.Text('Calculadora UMP-2000', justification='right', font=("Helvetica", 25))],
      [sg.Output(size=(25,2), font=("Helvetica", 25))],# Onde mostram os numeros que serão calculados
      [sg.Button('7', size=(5, 2),font=("Helvetica", 25)),sg.Button('8', size=(5, 2),font=("Helvetica", 25)),sg.Button('9', size=(5, 2),font=("Helvetica", 25)),sg.Button('/', size=(5, 2),font=("Helvetica", 25))],# 7,8,9,/
      [sg.Button('4', size=(5, 2),font=("Helvetica", 25)),sg.Button('5', size=(5, 2),font=("Helvetica", 25)),sg.Button('6', size=(5, 2),font=("Helvetica", 25)),sg.Button('x', size=(5, 2),font=("Helvetica", 25))],# 4,5,6,x
      [sg.Button('1', size=(5, 2),font=("Helvetica", 25)),sg.Button('2', size=(5, 2),font=("Helvetica", 25)),sg.Button('3', size=(5, 2),font=("Helvetica", 25)),sg.Button('-', size=(5, 2),font=("Helvetica", 25))],# 1,2,3,-
      [sg.Button('0', size=(5, 2),font=("Helvetica", 25)),sg.Button('=', size=(5, 2),font=("Helvetica", 25)),sg.Button('C', size=(5, 2),font=("Helvetica", 25)),sg.Button('+', size=(5, 2),font=("Helvetica", 25))]# 0,=,+,C
    ]
 
    # Criando a janela da Calculadora
    self.janela = sg.Window('Calculadora',layout=self.layout)
    try:
      while True:
        self.eventos, self.valores = self.janela.Read() #recebendo valores:
        while self.digitando == True:
          if self.eventos != '.':
            self.numeros=str(self.numeros)+str(self.eventos)
            print(self.numeros)
            break
          else:
            print('error')
            break
    except:
      print('Ocorreu um erro ao receber sua resposta')
      self.Iniciar()
      
    finally:
            # Ensure the window is closed even if an exception occurs
            self.janela.close()


Calc = Calculadora()
Calc.Iniciar()
