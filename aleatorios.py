"""
Eduard Gibert Ramon

"""


class Aleat:
    '''
    Clase que genera numeros aleatorios usando el método LGC.
    
    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    16
    29
    18
    15

    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    18
    15
    20
    1
    '''

    def __init__(self, m=2**31 - 1, a=1103515245, c=12345, x0=1212121):
        '''
        __init__ --> conjunto de variables configurables con un valor de default.
        '''
        self.m = m
        self.a = a
        self.c = c
        self.x = x0

    def __next__(self):
        '''
        generación y devuelve el siguiente numero aleat.
        '''
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __call__(self, sem):
        '''
        Reinicia la secuencia con un nuervo valor de semilla.
        '''
        self.x = sem

def aleat(m = 2**48, a = 25214903917, c = 11, x0 = 1212121):
    """
    Esta función hace exactamente lo mismo que la clase que hemos creado anteriormente.

    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    34
    24
    38
    44

    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    44
    10
    32
    14
    """
    x = x0
    while True:
        x = ((x*a) + c) % m 
        i = (yield x)
        if i: x = i



import doctest
doctest.testmod()


