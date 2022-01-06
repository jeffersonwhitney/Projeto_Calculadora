import PySimpleGUI as sg

class Calculadora:
  def __init__(self):
    #Layout da Caculadora
    
    sg.theme('Reddit')
    self.layout = [
      [sg.Text(' ')],# Onde mostram os numeros que serão calculados
      [sg.Button('7'),sg.Button('8'),sg.Button('9'),sg.Button('/')],# 7,8,9,/
      [sg.Button('4'),sg.Button('5'),sg.Button('6'),sg.Button('x')],# 4,5,6,x
      [sg.Button('1'),sg.Button('2'),sg.Button('3'),sg.Button('-')],# 1,2,3,-
      [sg.Button('0'),sg.Button('='),sg.Button('+')]# 0,=,+
    ]
  def Iniciar(self):
    # Criando a janela da Calculadora
    self.janela = sg.Window('Calculadora',layout=self.layout)
    self.eventos, self.valores = self.janela.read()
    try:  
        if self.eventos == '9':
          self.numeros = '9'
        elif self.eventos == '8':
          self.numeros = '8'
        elif self.eventos == '7':
          self.numeros = '7'
        elif self.eventos == '6':
          self.numeros = '6'
        elif self.eventos == '5':
          self.numeros = '5'
        elif self.eventos == '4':
          self.numeros = '4'
        elif self.eventos == '3':
          self.numeros = '3'
        elif self.eventos == '2':
          self.numeros = '2'
        elif self.eventos == '1':
          self.numeros = '1'
        elif self.eventos == '0':
          self.numeros = '0'
        elif self.eventos == '-':
          self.numeros = '-'
        elif self.eventos == '+':
          self.numeros = '+'
        elif self.eventos == '/':
          self.numeros = '/'
        elif self.eventos == '=':
          self.numeros = '='
    except:
            print('Ocorreu um erro ao receber sua resposta')

Calc = Calculadora()
Calc.Iniciar()
