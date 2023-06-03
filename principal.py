# -*- coding: utf-8 -*-

import os
import sys
import matplotlib
import numpy as np
from PyQt5 import QtCore, QtGui, Qt, QtWidgets, uic
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('qt5Agg')
import images

recoleccion_datos= 200
sensor_presion= np.random.rand(recoleccion_datos)
sensor_etiquetado= np.random.rand(recoleccion_datos)
sensor_nivel= np.random.randint(0, 1000, recoleccion_datos)
sensor_temperatura= np.random.randint(0, 100, recoleccion_datos)

class principal (QtWidgets.QMainWindow):
  
    def __init__(self):
        super (principal, self).__init__()
        uic.loadUi('principal.ui',self)
                  
        self.sensor_presion.clicked.connect(self.a)
        self.sensor_etiquetado.clicked.connect(self.b)
        self.sensor_nivel.clicked.connect(self.c)
        self.sensor_temperatura.clicked.connect(self.d)
        self.Datos()
        self.BOTON_LED.clicked.connect(self.e)
        
    def Datos(self):
        
        data = []
        with open ("./datos_taller.txt", "r") as file:
            for line in file:
                line_data = line.strip().split()
                data.append(line_data)
        
        self.Tabla.setColumnCount(len(data[0]))
        self.Tabla.setRowCount(len(data))
        
        for i, row in enumerate(data):
            for j, item in enumerate(row):
                self.Tabla.setItem(i, j, QtWidgets.QTableWidgetItem(item))
    
    def a(self):
            x= np.arange(1,201,1)
                    
            plt.plot(x, sensor_presion, linestyle='-', markerfacecolor='red')
            plt.xlabel('Tiempo (t)')
            plt.ylabel('Distancia (m)')
            plt.grid(True)
            plt.show()
        
    def b(self):
           x= np.arange(1,201,1)
           
           plt.plot(x, sensor_etiquetado,linestyle='-', markerfacecolor='yellow') 
           plt.xlabel('Tiempo(t)')
           plt.ylabel('Velocidad (km/h)')
           plt.grid(True)
           plt.show()
        
    def c(self):
          x= np.arange(1,201,1)
         
          plt.plot(x, sensor_nivel,linestyle='-', markerfacecolor='blue') 
          plt.xlabel('Tiempo (s)')
          plt.ylabel('Peso(Kg)')
          plt.grid(True)
          plt.show()
    def d(self):
          x= np.arange(1,201,1)
                  
          plt.plot(x, sensor_temperatura,linestyle='-', markerfacecolor='red') 
          plt.xlabel('Tiempo (t)')
          plt.ylabel('Temperatura(°C)')
          plt.grid(True)
          plt.show()
          
    def e(self):
         # Pin assignments
         import  RPi.GPIO as GPIO
         LED_PIN = 7
         BUTTON_PIN = 17
         # Setup GPIO module and pins
         GPIO.setmode(GPIO.BCM)
         GPIO.setup(LED_PIN, GPIO.OUT)
         GPIO.setup(BUTTON_PIN, GPIO.IN)
         # Set LED pin to OFF (no voltage)
         GPIO.output(LED_PIN, GPIO.LOW)
         try:
             # Loop forever
             while 1:
                 # Detect voltage on button pin
                 if GPIO.input(BUTTON_PIN) == 1:
                 # Turn on the LED
                    GPIO.output(LED_PIN, GPIO.HIGH)
                 else:
                   # Turn off the LED
                   GPIO.output(LED_PIN, GPIO.LOW)
         except KeyboardInterrupt:
             print('error')
         finally:
             GPIO.cleanup()
                  
def main():
        print('inicia')
        app=QtWidgets.QApplication(sys.argv)
        ventana=principal()
        ventana.show()
        sys.exit(app.exec_())
    
if  __name__=="__main__":
      main()   