#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
"""
Módulo que contiene una clase para la conexión con una tarjeta Arduino UNO por
medio del puerto serial.
"""
 
from serial import Serial
import simplejson,time
class ArduinoUNO(Serial):
    """
    Clase para la conexión con la tarjeta Arduino UNO, derivada de la clase
    Serial para entrablar comunicación.
    """
    def __init__(self, puerto, baudios, **args):
        "Inicia la conexión con el puerto serial."
        try:
            super(ArduinoUNO, self).__init__(
                port = puerto, baudrate = baudios, **args)
        except:
            return 515
         
    def leer(self):
        "Recibe los datos enviados por la tarjeta Arduino."
        jsonResult = self.readline()
        try:
            jsonObject = simplejson.loads(jsonResult)
            return jsonObject["x"],jsonObject["y"],jsonObject["a"]
        except Exception:
            pass
         
        
    def desconectar(self):
        "Termina la conexión con el puerto serial."
        self.close()
