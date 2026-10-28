from motor_reglas import (
    encadenar_hacia_adelante, formatear_traza,
    REGLAS_INICIALES, REGLAS_BASE,
)

hechos = {"embalaje_danado"}

print("===== SIN R7 =====")
fin, tr = encadenar_hacia_adelante(hechos, REGLAS_INICIALES)
print(formatear_traza(hechos, fin, tr))

print("===== CON R7 =====")
fin, tr = encadenar_hacia_adelante(hechos, REGLAS_BASE)
print(formatear_traza(hechos, fin, tr))