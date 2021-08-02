import array
class Queue:
    def __init__(self,size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))

    def vacio(self):
        return self.size == 0

    def llena(self):
        return self.size == self.max

    def encola(self,x):
        if self.size == self.max:
            return False
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0
        return True

    def saca(self):
        if self.size == 0:
            return None
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x


def test1():
    q = Queue(5)
    res = q.vacio() #res=true, cola creada pero vacia aun
    if res == False:  
        print ("Error")
        return
    res = q.encola(1) #1er elemento encolado (1)
    if res == False:  #res=true
        print ("Error")
        return
    res = q.encola(2) #2do elemento encolado (2)
    if res == False:
        print ("Error")
        return
    x = q.saca() #1er elemento (1) desencolado, 2 se convierte en 1er elemento
    if x != 1:
        print ("Error")
        return
    x = q.saca() #1er elemento (2) desencolado
    if x != 2:
        print ("Error")
        return
    res = q.vacio() 
    if res == False:
        print ("Error")
        return
    print ("test1 OK")

def test2():
    q = Queue(3)
    res = q.vacio() #res=true, cola creada pero vacia aun
    if res == False:
        print ("Error")
        return
    res = q.encola(10) #1er elemento encolado (10)
    if res == False:
        print ("Error")
        return
    res = q.encola(11) #2do elemento encolado (11)
    if res == False:
        print ("Error")
        return
    res = q.encola(12) #3er elemento encolado (12), cola llena
    if res == False:
        print ("Error")
        return
    if q.tail !=0: # cuando  tail = total de elementos (3) vuelve a posicion 0
        print ("Error")
        return
    #print(q.tail)
    print("test2 OK")

def test3():
    q = Queue(1)
    res = q.vacio() #res=true, cola creada pero vacia aun
    if res == False:
        print ("Error")
        return
    x=q.saca() #intenta eliminar elemento que no hay
    if not x is None: #x != None
        print ("Error")
        return
    res = q.encola(10)  #1er elemento encolado (10)
    if res == False:
        print ("Error")
        return
    x=q.saca() #desencola 1er elemento (x=10)
    if x!=10 or q.head !=0: #x=10, head=0
        print ("Error")
        return
    print("test3 OK")

def asserts(self):
    #1ra situacion:  tamaño de la cola nunca podrá ser un número negativo o cero
    assert self.size >= 0 and self.size <= self.max
    
    if self.tail > self.head: #cola-cabeza
        assert (self.tail - self.head) == self.size #se comprueba el nro de elementos actuales
    
    if self.tail < self.head: #cola dio la vuelta 
        assert (self.head - self.tail) == (self.max - self.size)
    
    if self.tail == self.head: #llena o vacia si cabeza = cola misma posicion
        assert (self.size == 0) or (self.size == self.max)
    
    return

test1()
test2()
test3()
