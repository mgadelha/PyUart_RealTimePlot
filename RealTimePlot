# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 19:48:54 2013

@author: Mauricio
"""
import sys
from PyQt4 import QtGui
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import Serial_KL25Z as serial

"""
Classe responsavel pela criação do objeto de plotagem 
"""
class MplCanvas(FigureCanvas):
    
    def __init__(self):    
        self.fig = Figure()
        FigureCanvas.__init__(self,self.fig)                            #Instancia o Canvas para a renderização
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding,   #Configura a politica de tamanho 
                                       QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        
"""
Classe responsavel pela criacao da aplicacao (widget)
"""    

MAXITERS = 50                                                           #Define o alcance em tempo real do eixo X na tela
class CPUMonitor(QtGui.QWidget):
    def __init__(self, parent = None):
        super(CPUMonitor, self).__init__(parent)
        
        #Set's Iniciais e Criação dos Objetos
        self.xlimit = MAXITERS             
        self.before = self.prepare_serial_axis_data()                   #Inicializa os valores iniciais        
        self.mpl_real = MplCanvas()                                     #Objeto fig.canvas
        
        #Set's dos eixos     
        self.ax = self.mpl_real.fig.add_subplot(111)                    #Criação dos Eixos     
        self.ax.set_xlim(0,self.xlimit)
        self.ax.set_ylim(-5,5)
        self.ax.set_autoscale_on(False)
        self.ax.grid()
        
        #Criação do QtLayout    
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.mpl_real)                                 #Adiciona o objeto mpl_real ao layout
        self.setLayout(layout)                                          #Define o objeto layout como layout principal
        
        #Criação das Listas para a atualização Dinamica dos Plot's
        self.x, self.y, self.z = [], [], []
        self.l_x, = self.ax.plot([], self.x,'r', label = 'X %')
        self.l_y, = self.ax.plot([], self.y,'g', label = 'Y %')
        self.l_z, = self.ax.plot([], self.z,'b', label = 'Z %')
        self.ax.legend()
        
        #Metodo de rendeziracao
        self.mpl_real.fig.canvas.draw()
        
        #Função de despacho de eventos por tempo do Qt
        self.cnt = 0
        self.timerEvent(None)   
        self.timer = self.startTimer(1)                                 #Definição da freq. inicial
    
    #Metodo para a aquisição dos dados seriais
    def prepare_serial_axis_data(self):             
        data = serial.SerialData()
        return data

                
    #Função que Captura os Eventos Gerados pelo timer
    def timerEvent(self, evento):
        
        result = self.prepare_serial_axis_data()
        self.x.append(result[0])                                        #Atualização das listas
        self.y.append(result[1])
        self.z.append(result[2])        
        
        #Metodo de Atualização dos eixos do Plot
        self.l_x.set_data(range(len(self.x)), self.x)                   #Atualiza os eixos
        self.l_y.set_data(range(len(self.y)), self.y)
        self.l_z.set_data(range(len(self.z)), self.z)
        
        #Renderização do plot
        self.mpl_real.fig.canvas.draw()
        
        #Comparação com o numero total de Pontos
        if self.cnt == MAXITERS:

            self.ax.clear()                                             #Limpa o eixo
            self.ax.set_xlim(0,self.xlimit)
            self.ax.set_ylim(-5,5)
            self.ax.set_autoscale_on(False)
            self.ax.grid()
            
            #Criação das Novas Listas
            self.x, self.y, self.z = [], [], []
            self.l_x, = self.ax.plot([], self.x,'r', label = 'X %')
            self.l_y, = self.ax.plot([], self.y,'g', label = 'Y %')
            self.l_z, = self.ax.plot([], self.z,'b', label = 'Z %')
            self.ax.legend()

    
            self.cnt = 0                                                #reinicia o contador
        
        else:
            self.cnt += 1


#Criação da App
app = QtGui.QApplication(sys.argv)
widget = CPUMonitor()
widget.show()
sys.exit(app.exec_())        
            
            
        
        
                
