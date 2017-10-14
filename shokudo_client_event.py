#coding: UTF-8

import socket


class event():
    def __init__(self):
        self.string=[]

    def onEVT_KEY_DOWN(self,evt):
        keycode=evt.GetKeyCode()
        if keycode==13:
            
            pass
        else:

            self.string+=[keycode]
        print("keydown",evt.GetKeyCode())

    def onEVT_KEY_UP(self,evt):
        print(self.string)
        print("keyup",evt.GetKeyCode())