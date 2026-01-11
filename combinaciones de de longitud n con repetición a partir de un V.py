from itertools import product
import numpy as np

def combinaciones(V, n):
    """
    Devuelve todas las combinaciones de longitud n
    con repetición a partir de V.
    """
    return list(product(V, repeat=n))

V = ["A", "B", "A and B", "A or B",
     "not A", "not B", "not A or B", "not B or A"]

# Longitud 5
C = combinaciones(V, 6)
D = np.array(C)

print("Número de filas:", D.shape[0])
print(D[:5])   # mostramos solo las primeras 5
