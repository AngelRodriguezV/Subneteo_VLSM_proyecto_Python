
class Red:
    """La clase red guarda la informacion de una Red"""

    def __init__(self, nameRed:str="Mi Red", IPs:int=4, utilizable:int=None):
        self.nameRed = nameRed
        self.IPs = IPs
        self.utilizable = utilizable
        self.id_red = None
        self.primera_ip = None
        self.ultima_ip = None
        self.broadcast = None
        self.mascara = None
    
    def setDatos(self, datos):
        self.id_red = datos[1]
        self.primera_ip = datos[2]
        self.ultima_ip = datos[3]
        self.broadcast = datos[4]
        self.mascara = datos[5]
  
    def getData(self):
        return [self.nameRed, self.id_red, self.primera_ip, self.ultima_ip, self.broadcast, self.mascara]