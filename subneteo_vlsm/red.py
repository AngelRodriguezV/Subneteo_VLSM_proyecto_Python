from subneteo_vlsm.operaciones import calcularMascara

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
    
    def getMascaraProcedimiento(self):
        bitslibres = 0
        for i, pow in enumerate([2**j for j in range(0,17)]):
            if pow >= self.IPs:
                bitslibres = i
                break
        
        mascaraB, mascaraD = calcularMascara(bitslibres)
        
        print("{}  IPs:{}".format(self.nameRed,self.IPs))
        print("    host: (2 ^ {}) - 2: {}".format(bitslibres,(2**bitslibres)-2))
        print("    masacara: {} = {}".format(mascaraB, mascaraD))