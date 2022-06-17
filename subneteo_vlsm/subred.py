
import pandas as pd

from operaciones import calcularMascara, ObtenerBitsIP, CombertirDecimal, SumarUnBinario, SumaIP, RestaIP, AgruparIP
from red import Red

class SubRed:

    def __init__(self, direccion_utilizable: str = '255.0.0.0', cantidad_ips: int = 4, cantidad_subredes: int = 2) -> None:
        self.direccion_utilizable = direccion_utilizable
        self.cantidad_ips = cantidad_ips
        self.cantidad_subredes = cantidad_subredes

        # Calculamos los bits libres para generar la mascara
        self.__cantidad_bits_libres = None
        for i, v in enumerate([2**j for j in range(0,17)]):
            if v >= self.cantidad_ips:
                self.__cantidad_bits_libres = i
                break
        self.__cantidad_bits_mascara = 32 - self.__cantidad_bits_libres

        self.mascara_red = calcularMascara(self.__cantidad_bits_libres)[1]

        self.__bitsCompletos = ObtenerBitsIP(self.direccion_utilizable)
        self.__bits_Direccion = None
        self.__bits_Red = None
        self.__bits_Hots = None
        self.__calcular_tabla()

    def __Obtener_Bits(self):
        """Separamos en tres secciones los bits de la ip"""
        size = len(self.__bitsCompletos)
        indices = [size-1-i for i in range(0,size)]
        aux = ""
        for i in indices:
            if self.__bitsCompletos[i] == '1':
                self.__bits_Direccion = self.__bitsCompletos[0:i+1]
                aux = self.__bitsCompletos[i+1:size]
                break
        size = len(aux) - self.__cantidad_bits_libres
        self.__bits_Red = aux[0:size]
        self.__bits_Hots = aux[size:len(aux)]
        if self.cantidad_ips > 4:
            self.__bits_Red = SumarUnBinario(self.__bits_Red)
    
    def __ObtenerIP(self,bits:str):
        """Obtiene la ip juntando los bits"""
        oct1 = CombertirDecimal(bits[0:8])
        oct2 = CombertirDecimal(bits[8:16])
        oct3 = CombertirDecimal(bits[16:24])
        oct4 = CombertirDecimal(bits[24:32])
        return AgruparIP([oct1, oct2, oct3, oct4])

    def __calcular_tabla(self):
        """Calcula la tabla de ips"""
        self.__Obtener_Bits()
        self.__redes = []
        for i in range(0,self.cantidad_subredes):
            bits = "{}{}{}".format(self.__bits_Direccion,self.__bits_Red,self.__bits_Hots)
            id_red = self.__ObtenerIP(bits)
            self.__bits_Red = SumarUnBinario(self.__bits_Red)
            bits = "{}{}{}".format(self.__bits_Direccion,self.__bits_Red,self.__bits_Hots)
            next_idred = self.__ObtenerIP(bits)
            primera_ip = SumaIP(id_red)
            broadcast = RestaIP(next_idred)
            ultima_ip = RestaIP(broadcast)
            self.__redes.append(["Red {}".format(i+1), id_red, primera_ip, ultima_ip, broadcast, self.mascara_red,"Disponible"])

    def getTablaDirecciones(self):
        tabla = pd.DataFrame(columns=['Red', 'ID Red', 'Primera IP Utilizable', 'Ultima IP Utilizable', 'Broadcast', 'Mascara de la Red', 'Disponible'])
        columna1, columna2, columna3, columna4, columna5, columna6, columna7 = [], [], [], [], [], [], []
        for data in self.__redes:
            columna1.append(data[0])
            columna2.append(data[1])
            columna3.append(data[2])
            columna4.append(data[3])
            columna5.append(data[4])
            columna6.append(data[5])
            columna7.append(data[6])
        tabla['Red'] = columna1
        tabla['ID Red'] = columna2
        tabla['Primera IP Utilizable'] = columna3
        tabla['Ultima IP Utilizable'] = columna4
        tabla['Broadcast'] = columna5
        tabla['Mascara de la Red'] = columna6
        tabla['Disponible'] = columna7
        return tabla

    def asignarDireccion(self, red:Red):
        if red.utilizable != None:
            self.__redes[red.utilizable-1][0] = red.nameRed
            self.__redes[red.utilizable-1][6] = "Ocupada"
            red.setDatos(self.__redes[red.utilizable-1])
            return red
        if red.utilizable == None:
            for data in self.__redes:
                if data[6] == "Disponible":
                    data[0] = red.nameRed
                    data[6] = "Ocupada"
                    red.setDatos(data)
                    return red