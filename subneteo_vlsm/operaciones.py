"""Modulo de operaciones para operar con bits"""

def CombertirBinario(decimal: int = 255) -> str:
    """Combierte un octeto decimal a binario
    @param decimal: Un entero positivo no mayor a 255
    @return: Retorna la cadena de bits obtenida
    """
    binario = ''
    # Si es 0 nos regresa ocho bits en ceros
    if decimal == 0: return '00000000'
    # Calculamos los bits mediante un loop
    while decimal > 0:
        if (decimal % 2) == 1:
            binario = '1' + binario
        else:
            binario = '0' + binario
        decimal //= 2
    # Si nos falta bits a la izquierda le agregamos los ceros restantes
    if len(binario) < 8:
        for i in range(0, 8 - len(binario)):
            binario = '0' + binario
    # retornamos el resultado
    return binario

def CombertirDecimal(binario: str = "11111111") -> int:
    """Combierte un octeto en binario a decimal
    @param binario: Una cadena de 8 bits
    @return: Regresa el octeto en decimal
    """
    decimal = 0
    for i, pow in enumerate([7, 6, 5, 4, 3, 2, 1, 0]):
        if binario[i] == '1':
            decimal += (2 ** pow)
    return decimal

def SumarUnBinario(binario: str = "00000001") -> str:
    """Suma un bit a un binario
    @param binario: Una cadena de bits
    @return: Regresa la cadena de bits más uno bit 
    """
    bits = BinarioList(binario)
    acarreo = 1
    # Recorremos los bits de deracha a izquierda para sumar
    for i in [(len(bits) - 1 - j) for j in range(0, len(bits))]:
        bits[i] += acarreo
        if bits[i] >= 2:
            acarreo = bits[i] // 2
            bits[i] -= (acarreo * 2)
            if i > 0:
                bits[i - 1] += acarreo
                acarreo = 0
        else:
            acarreo = 0
    return BinarioStr(bits)

def BinarioList(binario: str) -> list:
    """Combierte una cadena de binarios a una lista
    @param binario: Una cadena de binarios
    @return: Regresa una lista con los bits de la cadena
    """
    bits = []
    for i in range(0, len(binario)):
        bits.append(int(binario[i]))
    return bits

def BinarioStr(bits: list) -> str:
    """Combierte una lista de bits a una cadena binaria
    @param bits: Lista de bits
    @return: Refresa una cadena de los bits
    """
    binario = ''
    for i in bits:
        binario += str(i)
    return binario

def SumaIP(IP1: str, IP2: str = '0.0.0.1') -> str:
    """Suma dos IPs"""
    # Preparamos los datos separandolos
    ip1 = DesagruparIP(IP1)
    ip2 = DesagruparIP(IP2)
    acarreo = 0
    # Realizamos la suma
    for i in [3, 2, 1, 0]:
        ip1[i] += ip2[i]
        if ip1[i] >= 256:
            acarreo = ip1[i] // 256
            ip1[i] -= (acarreo * 256)
            if i > 0:
                ip1[i - 1] += acarreo
    # Retornamos el resultado
    return AgruparIP(ip1)

def RestaIP(IP1: str, IP2: str = '0.0.0.1') -> str:
    """Resta dos IPs"""
    # Funcion de Apollo
    def ApolloResta(ip: list, nivel: int):
        for i in [3,2,1,0]:
                if nivel == i:
                    ip[i] = 256
                if nivel > i:
                    if ip[i] != 0:
                        ip[i] -= 1
                        break
                    if ip[i] == 0:
                        ip[i] = 255
    # Primero preparar los datos
    ip1 = DesagruparIP(IP1)
    ip2 = DesagruparIP(IP2)
    # Realizamos la resta
    for i in [3, 2, 1, 0]:
        if ip1[i] == 0 and ip2[i] == 0:
            continue
        if ip1[i] == 0:
            ApolloResta(ip1, i)
        ip1[i] -= ip2[i]
    # Retornamos el resulato
    return AgruparIP(ip1)


def DesagruparIP(IP: str) -> list:
    """Combierte una IP en una lista"""
    ip = []
    for i in IP.split('.'):
        ip.append(int(i))
    return ip

def AgruparIP(IP: list) -> str:
    """Combierte una lista en una cadena IP"""
    ip = ''
    for i, octeto in enumerate(IP):
        ip += str(octeto)
        if i < 3:
            ip += '.'
    return ip

def ObtenerBitsIP(IP: str) -> str:
    """Obtiene todos los bits de una IP"""
    bits = ''
    ip = IP.split('.')
    for i in ip:
        bits += CombertirBinario(int(i))
    return bits

def calcularMascara(bistLibres: int):
    """Calcula la mascara a partir de los bits sobrantes"""
    mascaraB = ''
    mascaraD = ''
    aux = 32 - bistLibres
    for i in range(0, 4):
        for j in range(0, 8):
            if  aux > 0:
                mascaraB += '1'
            else:
                mascaraB += "0"
            aux -= 1
        if i < 3:
            mascaraB += "."

    octetos = mascaraB.split('.')
    for i, oct in enumerate(octetos):
        mascaraD += str(CombertirDecimal(oct))
        if i < 3:
            mascaraD += '.'

    return mascaraB, mascaraD