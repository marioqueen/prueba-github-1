# Tabla de verdad de la implicación A -> B
# Usamos la equivalencia: A -> B ≡ (not A) or B

import pandas as pd

valores = [True, False]

filas = []
for A in valores:
    for B in valores:
        implicacion = (not A) or B
        filas.append({
            "A": A,
            "B": B,
            "A -> B": implicacion
        })

tabla = pd.DataFrame(filas)

tabla
