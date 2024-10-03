
nombre= input("Ingrese su nombre: ")
salario = float(input("Ingrese el salario: "))
dias_laborados = int(input("Ingrese el número de días laborados: "))

def calcularLiquidacion(salario, dias_laborados):
    prima = (salario * dias_laborados) / 360
    cesantias = (salario * dias_laborados) / 360
    intereses_cesantias = (cesantias * 0.12) / dias_laborados
    vacaciones = (salario * dias_laborados) / 720

    total_liquidacion = prima + cesantias + intereses_cesantias + vacaciones

    return prima, cesantias, intereses_cesantias, vacaciones, total_liquidacion

prima, cesantias, intereses_cesantias, vacaciones, total_liquidacion = calcularLiquidacion(salario, dias_laborados)

print("-------Liquidacion-------")
print(f"{nombre} para los {dias_laborados} dias laborados y salario de {salario}, su liquidación se compone así: ")
print(f"Prima: {prima:.2f}")
print(f"Cesantías: {cesantias:.2f}")
print(f"Intereses a las Cesantías: {intereses_cesantias:.2f}")
print(f"Vacaciones: {vacaciones:.2f}")
print(f"Total Liquidación: {total_liquidacion:.2f}")


