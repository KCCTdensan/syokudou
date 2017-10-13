#coding: UTF-8
import socket

class event():
    def __init__(self):
        self.string=[]

    def onEVT_KEY_DOWN(self,evt):
        print("keydown",evt.GetKeyCode())

    def onEVT_KEY_UP(self,evt):
        print("keyup",evt.GetKeyCode())