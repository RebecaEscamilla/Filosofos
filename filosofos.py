import threading
from time import sleep
from random import randint

class Filosofo(threading.Thread):
    palillos = []
    estado = [0,0,0,0,0]
    
    def __init__(self,numFilosofo):
        super().__init__()
        self.numFilosofo = numFilosofo
        self.palillos.append(threading.RLock())
        
    def filosofar(self):
        print("Filosofo {} esta filosofando".format(self.numFilosofo))  
        sleep(randint(3,10))
        
    def comer(self):
        print("Filosofo {} quiere comer".format(self.numFilosofo))
        self.estado[self.numFilosofo-1] = 1
        i = (self.numFilosofo-2) % 5
        if self.estado[i] == 0:
            print("Filosofo {} tomo el palillo izquierdo".format(self.numFilosofo))
            self.palillos[i].acquire()
            j = self.numFilosofo % 5
            if self.estado[j] == 0:
                print("Filosofo {} tomo el palillo derecho".format(self.numFilosofo))
                self.palillos[j].acquire()
                print("Esta comiendo el filosofo {}".format(self.numFilosofo))
                sleep(randint(5,10))
                self.palillos[j].release()
                self.palillos[i].release()
                print("Termino de comer el filosofo {}".format(self.numFilosofo))
            else:
                print("Filosofo {} dejo el palillo izquierdo por que esta ocupado el derecho".format(self.numFilosofo))
                self.palillos[i].release()
        self.estado[self.numFilosofo-1] = 0

    def run(self):
        while True:
            sleep(randint(0,5))
            self.filosofar()
            self.comer()  
            
f1 = Filosofo(1)
f2 = Filosofo(2)
f3 = Filosofo(3)
f4 = Filosofo(4)
f5 = Filosofo(5)
f1.start()
f2.start()
f3.start()
f4.start()
f5.start()