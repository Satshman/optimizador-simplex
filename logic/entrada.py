import numpy as np

def ingresar_problema():

    print("\n=== INGRESO DEL PROBLEMA ===\n")

    tipo = input("Tipo (max/min): ").lower()

    n = int(input("Número de variables: "))
    m = int(input("Número de restricciones: "))

    # Función objetivo
    C = []

    print("\nFunción objetivo:")

    for i in range(n):
        valor = float(input(f"Coeficiente x{i+1}: "))
        C.append(valor)

    # Restricciones
    A = []
    b = []
    signos = []

    print("\nRestricciones:\n")

    for i in range(m):

        fila = []

        print(f"Restricción #{i+1}")

        for j in range(n):
            valor = float(input(f"Coeficiente x{j+1}: "))
            fila.append(valor)

        signo = input("Signo (<= >= =): ")

        rhs = float(input("Resultado: "))

        A.append(fila)
        signos.append(signo)
        b.append(rhs)

        print()

    return (
        tipo,
        np.array(C, dtype=float),
        np.array(A, dtype=float),
        signos,
        np.array(b, dtype=float)
    )