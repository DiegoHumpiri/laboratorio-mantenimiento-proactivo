import os
import hashlib

# Antipatrón 1: Credenciales expuestas directamente en el código fuente (Hardcoded Secrets / Vulnerability)
DB_PASSWORD = "SuperSecretAdminPassword123_$"
API_KEY = "AIzaSyD-un_token_falso_de_ejemplo_con_alta_entropia"

def procesar_usuarios(lista_usuarios):
# Antipatrón 2: Complejidad Ciclomática Excesiva (Code Smell de Mantenibilidad)
# Demasiados bloques condicionales anidados que dificultan la cobertura de pruebas unitarias
    for usuario in lista_usuarios:
        if usuario['activo'] == True:
            if usuario['edad'] > 18:
                if usuario['rol'] == 'admin':
                    print("Acceso total concedido")
                elif usuario['rol'] == 'editor':
                    if usuario['permiso_escritura']:
                        print("Acceso de edición parcial")
                    else:
                        print("Acceso de lectura para editor")
                else:
                    print("Usuario estándar")
            else:
                print("Menor de edad")
        else:
            print("Usuario inactivo")


def calcular_impuesto_zona_a(monto):
# Antipatrón 3: Código Duplicado (Métricas de redundancia)
# Bloques idénticos copiados y pegados que violan el principio DRY (Don't Repeat Yourself)
    factor = 0.18
    total_con_impuesto = monto + (monto * factor)

    if total_con_impuesto > 5000:

        total_con_impuesto -= 100

    return total_con_impuesto

def calcular_impuesto_zona_b(monto):
# Duplicación explícita del bloque anterior cambiando únicamente el nombre de la función
    factor = 0.18
    total_con_impuesto = monto + (monto * factor)

    if total_con_impuesto > 5000:

        total_con_impuesto -= 100

    return total_con_impuesto

def operacion_insegura_y_muerta():
# Antipatrón 4: Bug Lógico y Código Muerto
# Intentar ejecutar una división por cero (falla en tiempo de ejecución garantizada)
    # Seguido de código que nunca se ejecutará debido al flujo previo
    divisor = 0
    resultado = 100 / divisor
    # Código muerto (Dead Code)
    print("Este mensaje jamás se imprimirá en consola")

    return resultado