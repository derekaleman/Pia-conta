#Validar entradas
import re
def validar_numero(entrada):
    # Expresión regular para validar números enteros o con decimales
    patron = r'^-?\d+(\.\d+)?$'
    return re.match(patron, entrada) is not None

#Preguntamos al Usuario Balance General 2022
print('Balance General 2022\n')
while True:
    saldo_inicial_efectivo = input("Ingresa el monto de Efectivo\n")
    if not saldo_inicial_efectivo:
          print("No se puede omitir.")
          continue
    elif not validar_numero(saldo_inicial_efectivo):
        print("Solo se aceptan números enteros o con decimales.")
        continue
    saldo_inicial_efectivo = float(saldo_inicial_efectivo)
    break
while True:
    saldo_clientes_2022 = input("Ingresa el monto de Clientes\n")
    if not saldo_clientes_2022: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(saldo_clientes_2022):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    saldo_clientes_2022 = float(saldo_clientes_2022)
    break
while True:
    deudores_diversos = input("Ingresa el monto de Deudores Diversos\n")
    if not deudores_diversos:
          print("No se puede omitir.")
          continue
    elif not validar_numero(deudores_diversos):
        print("Solo se aceptan números enteros o con decimales.")
        continue
    deudores_diversos = float(deudores_diversos)
    break
while True:
    funcionarios_empleados = input("Ingresa el monto de Funcionarios y Empleados\n")
    if not funcionarios_empleados:
          print("No se puede omitir.")
          continue
    elif not validar_numero(funcionarios_empleados):
        print("Solo se aceptan números enteros o con decimales.")
        continue
    funcionarios_empleados = float(funcionarios_empleados)
    break
while True:
    saldo_inicial_materiales = input("Ingresa el Inventario de Materiales\n")
    if not saldo_inicial_materiales:
          print("No se puede omitir.")
          continue
    elif not validar_numero(saldo_inicial_materiales):
        print("Solo se aceptan números enteros o con decimales.")
        continue
    saldo_inicial_materiales = float(saldo_inicial_materiales)
    break
while True:
    inventario_inicial_productos_terminados = input("Ingresa el Inventario de Productos Terminados\n")
    if not inventario_inicial_productos_terminados:
          print("No se puede omitir.")
          continue
    elif not validar_numero(inventario_inicial_productos_terminados):
        print("Solo se aceptan números enteros o con decimales.")
        continue
    inventario_inicial_productos_terminados = float(inventario_inicial_productos_terminados)
    break
while True:
    terreno = input("Ingresa el monto de Terreno\n")
    if not terreno:
          print("No se puede omitir.")
          continue
    elif not validar_numero(terreno):
        print("Solo se aceptan números enteros o con decimales.")
        continue
    terreno = float(terreno)
    break
while True:
    planta_equipo_r = input("Ingresa el monto de Planta y Equipo\n")
    if not planta_equipo_r:
          print("No se puede omitir.")
          continue
    elif not validar_numero(planta_equipo_r):
        print("Solo se aceptan números enteros o con decimales.")
        continue
    planta_equipo_r = float(planta_equipo_r)
    break
while True:
    depreciacion_acumulada_r = input("Ingresa el monto de Depreciacion Acumulada\n")
    if not depreciacion_acumulada_r:
          print("No se puede omitir.")
          continue
    elif not validar_numero(depreciacion_acumulada_r):
        print("Solo se aceptan números enteros o con decimales.")
        continue
    depreciacion_acumulada_r = float(depreciacion_acumulada_r)
    break
while True:
    saldo_proveedores_2022 = input("Ingresa el monto de Proveedores\n")
    if not saldo_proveedores_2022: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(saldo_proveedores_2022):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    saldo_proveedores_2022 = float(saldo_proveedores_2022)
    break
while True:
    documentos_pagar = input("Ingresa el monto de Documentos por Pagar\n")
    if not documentos_pagar:
          print("No se puede omitir.")
          continue
    elif not validar_numero(documentos_pagar):
        print("Solo se aceptan números enteros o con decimales.")
        continue
    documentos_pagar = float(documentos_pagar)
    break
while True:
    pago_isr_2022 = input("Ingresa el monto de Pago ISR por Pagar\n")
    if not pago_isr_2022:
          print("No se puede omitir.")
          continue
    elif not validar_numero(pago_isr_2022):
        print("Solo se aceptan números enteros o con decimales.")
        continue
    pago_isr_2022 = float(pago_isr_2022)
    break
while True:
    prestamos_bancarios = input("Ingresa el monto de Prestamos Bancarios\n")
    if not prestamos_bancarios:
          print("No se puede omitir.")
          continue
    elif not validar_numero(prestamos_bancarios):
        print("Solo se aceptan números enteros o con decimales.")
        continue
    prestamos_bancarios = float(prestamos_bancarios)
    break
while True:
    capital_aportado = input("Ingresa el monto del Capital Contribuido\n")
    if not capital_aportado:
          print("No se puede omitir.")
          continue
    elif not validar_numero(capital_aportado):
        print("Solo se aceptan números enteros o con decimales.")
        continue
    capital_aportado = float(capital_aportado)
    break
while True:
    capital_ganado = input("Ingresa el monto del Capital Ganado\n")
    if not capital_ganado:
          print("No se puede omitir.")
          continue
    elif not validar_numero(capital_ganado):
        print("Solo se aceptan números enteros o con decimales.")
        continue
    capital_ganado = float(capital_ganado)
    break

#Requerimiento de Materiales
print('\nRequerimiento de Materiales\n')
print('Producto 1\n')
while True:
    requerimiento_material_a_1_1 = input("Ingresa el Requerimiento del Material A\n")
    if not requerimiento_material_a_1_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(requerimiento_material_a_1_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    requerimiento_material_a_1_1 = float(requerimiento_material_a_1_1)
    break
while True:
    requerimiento_material_b_1_1 = input("Ingresa el Requerimiento del Material B\n")
    if not requerimiento_material_b_1_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(requerimiento_material_b_1_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    requerimiento_material_b_1_1 = float(requerimiento_material_b_1_1)
    break
while True:
    requerimiento_material_c_1_1 = input("Ingresa el Requerimiento del Material C\n")
    if not requerimiento_material_c_1_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(requerimiento_material_c_1_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    requerimiento_material_c_1_1 = float(requerimiento_material_c_1_1)
    break
print('\nProducto 2\n')
while True:
    requerimiento_material_a_2_1 = input("Ingresa el Requerimiento del Material A\n")
    if not requerimiento_material_a_2_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(requerimiento_material_a_2_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    requerimiento_material_a_2_1 = float(requerimiento_material_a_2_1)
    break
while True:
    requerimiento_material_b_2_1 = input("Ingresa el Requerimiento del Material B\n")
    if not requerimiento_material_b_2_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(requerimiento_material_b_2_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    requerimiento_material_b_2_1 = float(requerimiento_material_b_2_1)
    break
while True:
    requerimiento_material_c_2_1 = input("Ingresa el Requerimiento del Material C\n")
    if not requerimiento_material_c_2_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(requerimiento_material_c_2_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    requerimiento_material_c_2_1 = float(requerimiento_material_c_2_1)
    break
print('\nProducto 3\n')
while True:
    requerimiento_material_a_3_1 = input("Ingresa el Requerimiento del Material A\n")
    if not requerimiento_material_a_3_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(requerimiento_material_a_3_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    requerimiento_material_a_3_1 = float(requerimiento_material_a_3_1)
    break
while True:
    requerimiento_material_b_3_1 = input("Ingresa el Requerimiento del Material B\n")
    if not requerimiento_material_b_3_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(requerimiento_material_b_3_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    requerimiento_material_b_3_1 = float(requerimiento_material_b_3_1)
    break
while True:
    requerimiento_material_c_3_1 = input("Ingresa el Requerimiento del Material C\n")
    if not requerimiento_material_c_3_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(requerimiento_material_c_3_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    requerimiento_material_c_3_1 = float(requerimiento_material_c_3_1)
    break
print('')
while True:
    horas_requeridas_unidad_1_1 = input("Ingresa las Horas Mano de Obra del Producto 1\n")
    if not horas_requeridas_unidad_1_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(horas_requeridas_unidad_1_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    horas_requeridas_unidad_1_1 = float(horas_requeridas_unidad_1_1)
    break
while True:
    horas_requeridas_unidad_2_1 = input("Ingresa las Horas Mano de Obra del Producto 2\n")
    if not horas_requeridas_unidad_2_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(horas_requeridas_unidad_2_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    horas_requeridas_unidad_2_1 = float(horas_requeridas_unidad_2_1)
    break
while True:
    horas_requeridas_unidad_3_1 = input("Ingresa las Horas Mano de Obra del Producto 3\n")
    if not horas_requeridas_unidad_3_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(horas_requeridas_unidad_3_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    horas_requeridas_unidad_3_1 = float(horas_requeridas_unidad_3_1)
    break
print('')
while True:
    cuota_hora_1 = input("Ingresa la Cuota por hora de Mano de Obra del 1er. Semestre\n")
    if not cuota_hora_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(cuota_hora_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    cuota_hora_1 = float(cuota_hora_1)
    break
while True:
    cuota_hora_2 = input("Ingresa la Cuota por hora de Mano de Obra del 2do. Semestre\n")
    if not cuota_hora_2: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(cuota_hora_2):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    cuota_hora_2 = float(cuota_hora_2)
    break

#Informacion de Inventarios
print('\nInformacion de Inventarios\n')
print('1er. Semestre\n')
while True:
    inventario_final_material_a_1 = input("Ingresa el Inventario Inicial del Material A\n")
    if not inventario_final_material_a_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(inventario_final_material_a_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    inventario_final_material_a_1 = float(inventario_final_material_a_1)
    break
while True:
    inventario_final_material_b_1 = input("Ingresa el Inventario Inicial del Material B\n")
    if not inventario_final_material_b_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(inventario_final_material_b_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    inventario_final_material_b_1 = float(inventario_final_material_b_1)
    break
while True:
    inventario_final_material_c_1 = input("Ingresa el Inventario Inicial del Material C\n")
    if not inventario_final_material_c_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(inventario_final_material_c_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    inventario_final_material_c_1 = float(inventario_final_material_c_1)
    break
while True:
    inventario_final_1_1 = input("Ingresa el Inventario Final del producto 1\n")
    if not inventario_final_1_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(inventario_final_1_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    inventario_final_1_1 = float(inventario_final_1_1)
    break
while True:
    inventario_final_2_1 = input("Ingresa el Inventario Final del producto 2\n")
    if not inventario_final_2_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(inventario_final_2_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    inventario_final_2_1 = float(inventario_final_2_1)
    break
while True:
    inventario_final_3_1 = input("Ingresa el Inventario Final del producto 3\n")
    if not inventario_final_3_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(inventario_final_3_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    inventario_final_3_1 = float(inventario_final_3_1)
    break
print('\n2do. Semestre\n')
while True:
    inventario_final_material_a_2 = input("Ingresa el Inventario Final del Material A\n")
    if not inventario_final_material_a_2: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(inventario_final_material_a_2):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    inventario_final_material_a_2 = float(inventario_final_material_a_2)
    break
while True:
    inventario_final_material_b_2 = input("Ingresa el Inventario Final del Material B\n")
    if not inventario_final_material_b_2: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(inventario_final_material_b_2):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    inventario_final_material_b_2 = float(inventario_final_material_b_2)
    break
while True:
    inventario_final_material_c_2 = input("Ingresa el Inventario Final del Material C\n")
    if not inventario_final_material_c_2: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(inventario_final_material_c_2):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    inventario_final_material_c_2 = float(inventario_final_material_c_2)
    break
while True:
    inventario_final_1_2 = input("Ingresa el Inventario Final del producto 1\n")
    if not inventario_final_1_2: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(inventario_final_1_2):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    inventario_final_1_2 = float(inventario_final_1_2)
    break
while True:
    inventario_final_2_2 = input("Ingresa el Inventario Final del producto 2\n")
    if not inventario_final_2_2: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(inventario_final_2_2):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    inventario_final_2_2 = float(inventario_final_2_2)
    break
while True:
    inventario_final_3_2 = input("Ingresa el Inventario Final del producto 3\n")
    if not inventario_final_3_2: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(inventario_final_3_2):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    inventario_final_3_2 = float(inventario_final_3_2)
    break
#Costos materiales
print('\n1er. Semestre\n')
while True:
    precio_compra_material_a_1 = input("Ingresa el Precio de Compra del Material A\n")
    if not precio_compra_material_a_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(precio_compra_material_a_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    precio_compra_material_a_1 = float(precio_compra_material_a_1)
    break
while True:
    precio_compra_material_b_1 = input("Ingresa el Precio de Compra del Material B\n")
    if not precio_compra_material_b_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(precio_compra_material_b_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    precio_compra_material_b_1 = float(precio_compra_material_b_1)
    break
while True:
    precio_compra_material_c_1 = input("Ingresa el Precio de Compra del Material C\n")
    if not precio_compra_material_c_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(precio_compra_material_c_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    precio_compra_material_c_1 = float(precio_compra_material_c_1)
    break
print('\n2do. Semestre\n')
while True:
    precio_compra_material_a_2 = input("Ingresa el Precio de Compra del Material A\n")
    if not precio_compra_material_a_2: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(precio_compra_material_a_2):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    precio_compra_material_a_2 = float(precio_compra_material_a_2)
    break
while True:
    precio_compra_material_b_2 = input("Ingresa el Precio de Compra del Material B\n")
    if not precio_compra_material_b_2: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(precio_compra_material_b_2):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    precio_compra_material_b_2 = float(precio_compra_material_b_2)
    break
while True:
    precio_compra_material_c_2 = input("Ingresa el Precio de Compra del Material C\n")
    if not precio_compra_material_c_2: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(precio_compra_material_c_2):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    precio_compra_material_c_2 = float(precio_compra_material_c_2)
    break

#Productos
print('\nProductos\n')
print('Producto 1\n')
while True:
    precio_venta_1_1 = input("Ingresa el Precio de Venta del 1er. Semestre\n")
    if not precio_venta_1_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(precio_venta_1_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    precio_venta_1_1 = float(precio_venta_1_1)
    break
while True:
    precio_venta_1_2 = input("Ingresa el Precio de Venta del 2do. Semestre\n")
    if not precio_venta_1_2: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(precio_venta_1_2):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    precio_venta_1_2 = float(precio_venta_1_2)
    break
while True:
    unidades_vender_1_1 = input("Ingresa las Ventas planeadas del 1er. Semestre\n")
    if not unidades_vender_1_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(unidades_vender_1_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    unidades_vender_1_1 = float(unidades_vender_1_1)
    break
while True:
    unidades_vender_1_2 = input("Ingresa las Ventas planeadas del 2do. Semestre\n")
    if not unidades_vender_1_2: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(unidades_vender_1_2):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    unidades_vender_1_2 = float(unidades_vender_1_2)
    break
print('\nProducto 2\n')
while True:
    precio_venta_2_1 = input("Ingresa el Precio de Venta del 1er. Semestre\n")
    if not precio_venta_2_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(precio_venta_2_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    precio_venta_2_1 = float(precio_venta_2_1)
    break
while True:
    precio_venta_2_2 = input("Ingresa el Precio de Venta del 2do. Semestre\n")
    if not precio_venta_2_2: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(precio_venta_2_2):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    precio_venta_2_2 = float(precio_venta_2_2)
    break
while True:
    unidades_vender_2_1 = input("Ingresa las Ventas planeadas del 1er. Semestre\n")
    if not unidades_vender_2_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(unidades_vender_2_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    unidades_vender_2_1 = float(unidades_vender_2_1)
    break
while True:
    unidades_vender_2_2 = input("Ingresa las Ventas planeadas del 2do. Semestre\n")
    if not unidades_vender_2_2: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(unidades_vender_2_2):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    unidades_vender_2_2 = float(unidades_vender_2_2)
    break
print('\nProducto 3\n')
while True:
    precio_venta_3_1 = input("Ingresa el Precio de Venta del 1er. Semestre\n")
    if not precio_venta_3_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(precio_venta_3_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    precio_venta_3_1 = float(precio_venta_3_1)
    break
while True:
    precio_venta_3_2 = input("Ingresa el Precio de Venta del 2do. Semestre\n")
    if not precio_venta_3_2: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(precio_venta_3_2):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    precio_venta_3_2 = float(precio_venta_3_2)
    break
while True:
    unidades_vender_3_1 = input("Ingresa las Ventas planeadas del 1er. Semestre\n")
    if not unidades_vender_3_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(unidades_vender_3_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    unidades_vender_3_1 = float(unidades_vender_3_1)
    break
while True:
    unidades_vender_3_2 = input("Ingresa las Ventas planeadas del 2do. Semestre\n")
    if not unidades_vender_3_2: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(unidades_vender_3_2):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    unidades_vender_3_2 = float(unidades_vender_3_2)
    break

#Gastos de Administracion y Ventas
print('\nGastos de Administracion y Ventas\n')
while True:
    go_depreciacion = input("Ingresa el gasto de Depreciación anual\n")
    if not go_depreciacion: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(go_depreciacion):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    go_depreciacion = float(go_depreciacion)
    break
while True:
    sueldos_salarios = input("Ingresa el gasto de Sueldos y Salarios anual\n")
    if not sueldos_salarios: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(sueldos_salarios):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    sueldos_salarios = float(sueldos_salarios)
    break
while True:
    comisiones_go = input("Ingresa el Porcentaje de las comisiones (ingresa solamente el numero del porcentaje)\n")
    if not comisiones_go: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(comisiones_go):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    comisiones_go = float(comisiones_go)
    break
while True:
    go_varios_1 = input("Ingresa el monto de gastos Varios del 1er. Semestre\n")
    if not go_varios_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(go_varios_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    go_varios_1 = float(go_varios_1)
    break
while True:
    go_varios_2 = input("Ingresa el monto de gastos Varios del 2do. Semestre\n")
    if not go_varios_2: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(go_varios_2):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    go_varios_2 = float(go_varios_2)
    break
while True:
    intereses_prestamo = input("Ingresa el gasto de Intereses del Prestamo anual\n")
    if not intereses_prestamo: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(intereses_prestamo):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    intereses_prestamo = float(intereses_prestamo)
    break

#Gastos de Fabricacion Indirectos
print('\nGastos de Fabricacion Indirectos\n')
while True:
    gif_depreciacion = input("Ingresa el gasto de Depreciación anual\n")
    if not gif_depreciacion: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(gif_depreciacion):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    gif_depreciacion = float(gif_depreciacion)
    break
while True:
    gif_seguros = input("Ingresa el gasto de Seguros anual\n")
    if not gif_seguros: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(gif_seguros):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    gif_seguros = float(gif_seguros)
    break
while True:
    gif_mantenimiento_1 = input("Ingresa el gasto de Mantenimiento del 1er. Semestre\n")
    if not gif_mantenimiento_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(gif_mantenimiento_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    gif_mantenimiento_1 = float(gif_mantenimiento_1)
    break
while True:
    gif_mantenimiento_2 = input("Ingresa el gasto de Mantenimiento del 2do. Semestre\n")
    if not gif_mantenimiento_2: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(gif_mantenimiento_2):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    gif_mantenimiento_2 = float(gif_mantenimiento_2)
    break
while True:
    gif_energeticos_1 = input("Ingresa el gasto de Energeticos del 1er. Semestre\n")
    if not gif_energeticos_1: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(gif_energeticos_1):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    gif_energeticos_1 = float(gif_energeticos_1)
    break
while True:
    gif_energeticos_2 = input("Ingresa el gasto de Energeticos del 2do. Semestre\n")
    if not gif_energeticos_2: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(gif_energeticos_2):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    gif_energeticos_2 = float(gif_energeticos_2)
    break
while True:
    gif_varios = input("Ingresa el monto de gastos Varios anual\n")
    if not gif_varios: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(gif_varios):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    gif_varios = float(gif_varios)
    break
print('')
#Datos Adicionales
while True:
    compra_activo_fijo_maquinaria = input("Se adquirió un nuevo equipo valuado en:\n")
    if not compra_activo_fijo_maquinaria:
          print("No se puede omitir.")
          continue
    elif not validar_numero(compra_activo_fijo_maquinaria):
        print("Solo se aceptan números enteros o con decimales.")
        continue
    compra_activo_fijo_maquinaria = float(compra_activo_fijo_maquinaria)
    break
while True:
    isr = input("Ingresa el Porcentaje del ISR (ingresa solamente el numero del porcentaje)\n")
    if not isr: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(isr):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    isr = float(isr)
    break
while True:
    ptu = input("Ingresa el Porcentaje del PTU (ingresa solamente el numero del porcentaje)\n")
    if not ptu: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(ptu):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    ptu = float(ptu)
    break
while True:
    se_cobrara = input("En 2023 se cobrara el ___% del saldo de clientes del 2022. (ingresa el digito del procentaje)\n")
    if not se_cobrara: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(se_cobrara):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    se_cobrara = float(se_cobrara)
    break
while True:
    se_cobrara2 = input("En 2023 se cobrará el ___% de las ventas presupuestadas. (ingresa el digito del procentaje)\n")
    if not se_cobrara2: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(se_cobrara2):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    se_cobrara2 = float(se_cobrara2)
    break
while True:
    se_pagara = input("En 2022 se pagará el ___% del saldo de proveedores. (ingresa el digito del procentaje)\n")
    if not se_pagara: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(se_pagara):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    se_pagara = float(se_pagara)
    break
while True:
    se_pagara2 = input("En 2023 se pagará el ___% de las compras presupuestadas. (ingresa el digito del procentaje)\n")
    if not se_pagara2: #No se puede omitir
        print("No se puede omitir.")
        continue
    elif not validar_numero(se_pagara2):  # Verificar si la entrada es un número válido
        print("Solo se aceptan números enteros o con decimales.")
        continue
    se_pagara2 = float(se_pagara2)
    break

#Operaciones1
importe_venta_1_1 = unidades_vender_1_1*precio_venta_1_1
importe_venta_2_1 = unidades_vender_2_1*precio_venta_2_1
importe_venta_3_1 = unidades_vender_3_1*precio_venta_3_1

importe_venta_1_2 = unidades_vender_1_2*precio_venta_1_2
importe_venta_2_2 = unidades_vender_2_2*precio_venta_2_2
importe_venta_3_2 = unidades_vender_3_2*precio_venta_3_2

importe_venta_producto1_2023 = importe_venta_1_1+importe_venta_1_2
importe_venta_producto2_2023 = importe_venta_2_1+importe_venta_2_2
importe_venta_producto3_2023 = importe_venta_3_1+importe_venta_3_2

total_ventas_1semestre = importe_venta_1_1+importe_venta_2_1+importe_venta_3_1
total_ventas_2semestre = importe_venta_1_2+importe_venta_2_2+importe_venta_3_2
total_ventas_2023 = total_ventas_1semestre+total_ventas_2semestre

#Mostrar en pantalla 1
print(' ')
print('\nI. PRESUPUESTO DE OPERACION.\n')
print('~'*120)
print('\n1. PRESUPUESTO DE VENTAS.\n')

print('Producto 1')
print(f'Importe de Venta | 1er. Semestre: ${importe_venta_1_1:,} | 2do. Semestre: ${importe_venta_1_2:,} | 2023: ${importe_venta_producto1_2023:,}')
print('Producto 2')
print(f'Importe de Venta | 1er. Semestre: ${importe_venta_2_1:,} | 2do. Semestre: ${importe_venta_2_2:,} | 2023: ${importe_venta_producto2_2023:,}')
print('Prodcuto 3')
print(f'Importe de Venta | 1er. Semestre: ${importe_venta_3_1:,} | 2do. Semestre: ${importe_venta_3_2:,} | 2023: ${importe_venta_producto3_2023:,}\n')
print(f'Total de Ventas por Semestre | 1er. Semestre: ${total_ventas_1semestre:,} | 2do. Semestre: ${total_ventas_2semestre:,} | 2023: ${total_ventas_2023:,}')
print('~'*120)

#Operaciones 2
se_cobrara = se_cobrara/100
saldo_clientes_2022 = saldo_clientes_2022*se_cobrara
porcentaje_convertido = se_cobrara2/100
ventas_2023 = total_ventas_2023
total_clientes_2023 = saldo_clientes_2022+ventas_2023
cobranza_2022 = saldo_clientes_2022
cobranza_2023 = ventas_2023*porcentaje_convertido
suma_cobranza = cobranza_2022+cobranza_2023
saldo_clientes_2023 = total_clientes_2023-suma_cobranza

#Mostrar en pantalla 2
print(' ')
print('~'*120)
print('2. DETERMINACION DEL SALDO DE CLIENTES Y FLUJO DE ENTRADAS.\n')

print(f'Saldo de Clientes del 2023: ${saldo_clientes_2023:,}')
print('~'*120)

#Operaciones 3
total_unidades_1_1 = unidades_vender_1_1+inventario_final_1_1
inventario_inicial_1_1 = inventario_final_1_1
unidades_producir_1_1 = total_unidades_1_1-inventario_inicial_1_1

total_unidades_2_1 = unidades_vender_2_1+inventario_final_2_1
inventario_inicial_2_1 = inventario_final_2_1
unidades_producir_2_1 = total_unidades_2_1-inventario_inicial_2_1

total_unidades_3_1 = unidades_vender_3_1+inventario_final_3_1
inventario_inicial_3_1 = inventario_final_3_1
unidades_producir_3_1 = total_unidades_3_1-inventario_inicial_3_1

total_unidades_1_2 = unidades_vender_1_2+inventario_final_1_2
inventario_inicial_1_2 = inventario_final_1_1
unidades_producir_1_2 = total_unidades_1_2-inventario_inicial_1_2

total_unidades_2_2 = unidades_vender_2_2+inventario_final_2_2
inventario_inicial_2_2 = inventario_final_2_1
unidades_producir_2_2 = total_unidades_2_2-inventario_inicial_2_2

total_unidades_3_2 = unidades_vender_3_2+inventario_final_3_2
inventario_inicial_3_2 = inventario_final_3_1
unidades_producir_3_2 = total_unidades_3_2-inventario_inicial_3_2

unidades_producir_1_2023 = unidades_producir_1_1+unidades_producir_1_2
unidades_producir_2_2023 = unidades_producir_2_1+unidades_producir_2_2
unidades_producir_3_2023 = unidades_producir_3_1+unidades_producir_3_2


#Mostrar en pantalla 3
print('')
print('~'*120)
print('3. PRESUPUESTO DE PRODUCCION.\n')

print('Producto 1')
print(f'Unidades a Producir | 1er. Semestre: {unidades_producir_1_1:,} | 2do. Semestre: {unidades_producir_1_2:,} | 2023: {unidades_producir_1_2023:,}')
print('Producto 2')
print(f'Unidades a Producir | 1er. Semestre: {unidades_producir_2_1:,} | 2do. Semestre: {unidades_producir_2_2:,} | 2023: {unidades_producir_2_2023:,}')
print('Producto 3')
print(f'Unidades a Producir | 1er. Semestre: {unidades_producir_3_1:,} | 2do. Semestre: {unidades_producir_3_2:,} | 2023: {unidades_producir_3_2023:,}')
print('~'*120)

#Operaciones 4
#1 semestre
total_material_requerido_a_1_1 = unidades_producir_1_1*requerimiento_material_a_1_1
total_material_requerido_b_1_1 = unidades_producir_1_1*requerimiento_material_b_1_1
total_material_requerido_c_1_1 = unidades_producir_1_1*requerimiento_material_c_1_1

total_material_requerido_a_2_1 = unidades_producir_2_1*requerimiento_material_a_2_1
total_material_requerido_b_2_1 = unidades_producir_2_1*requerimiento_material_b_2_1
total_material_requerido_c_2_1 = unidades_producir_2_1*requerimiento_material_c_2_1

total_material_requerido_a_3_1 = unidades_producir_3_1*requerimiento_material_a_3_1
total_material_requerido_b_3_1 = unidades_producir_3_1*requerimiento_material_b_3_1
total_material_requerido_c_3_1 = unidades_producir_3_1*requerimiento_material_c_3_1
#2 semestre
total_material_requerido_a_1_2 = unidades_producir_1_2*requerimiento_material_a_1_1
total_material_requerido_b_1_2 = unidades_producir_1_2*requerimiento_material_b_1_1
total_material_requerido_c_1_2 = unidades_producir_1_2*requerimiento_material_c_1_1

total_material_requerido_a_2_2 = unidades_producir_2_2*requerimiento_material_a_2_1
total_material_requerido_b_2_2 = unidades_producir_2_2*requerimiento_material_b_2_1
total_material_requerido_c_2_2 = unidades_producir_2_2*requerimiento_material_c_2_1

total_material_requerido_a_3_2 = unidades_producir_3_2*requerimiento_material_a_3_1
total_material_requerido_b_3_2 = unidades_producir_3_2*requerimiento_material_b_3_1
total_material_requerido_c_3_2 = unidades_producir_3_2*requerimiento_material_c_3_1
#2023
total_material_requerido_a_1_2023 = total_material_requerido_a_1_1+total_material_requerido_a_1_2
total_material_requerido_b_1_2023 = total_material_requerido_b_1_1+total_material_requerido_b_1_2
total_material_requerido_c_1_2023 = total_material_requerido_c_1_1+total_material_requerido_c_1_2

total_material_requerido_a_2_2023 = total_material_requerido_a_2_1+total_material_requerido_a_2_2
total_material_requerido_b_2_2023 = total_material_requerido_b_2_1+total_material_requerido_b_2_2
total_material_requerido_c_2_2023 = total_material_requerido_c_2_1+total_material_requerido_c_2_2

total_material_requerido_a_3_2023 = total_material_requerido_a_3_1+total_material_requerido_a_3_2
total_material_requerido_b_3_2023 = total_material_requerido_b_3_1+total_material_requerido_b_3_2
total_material_requerido_c_3_2023 = total_material_requerido_c_3_1+total_material_requerido_c_3_2

#total materiales
material_requerido_a_1 = total_material_requerido_a_1_1+total_material_requerido_a_2_1+total_material_requerido_a_3_1
material_requerido_b_1 = total_material_requerido_b_1_1+total_material_requerido_b_2_1+total_material_requerido_b_3_1
material_requerido_c_1 = total_material_requerido_c_1_1+total_material_requerido_c_2_1+total_material_requerido_c_3_1

material_requerido_a_2 = total_material_requerido_a_1_2+total_material_requerido_a_2_2+total_material_requerido_a_3_2
material_requerido_b_2 = total_material_requerido_b_1_2+total_material_requerido_b_2_2+total_material_requerido_b_3_2
material_requerido_c_2 = total_material_requerido_c_1_2+total_material_requerido_c_2_2+total_material_requerido_c_3_2

material_requerido_a_2023 = material_requerido_a_1+material_requerido_a_2
material_requerido_b_2023 = material_requerido_b_1+material_requerido_b_2
material_requerido_c_2023 = material_requerido_c_1+material_requerido_c_2

#Mostrar en pantalla 4
print('')
print('~'*120)
print('4. PRESUPUESTO DE REQUERIMIENTOS DE MATERIALES.\n')

print('Producto 1')
print(f'Total de Material A requerido | 1er. Semestre: {total_material_requerido_a_1_1:,} | 2do. Semestre: {total_material_requerido_a_1_2:,} | 2023: {total_material_requerido_a_1_2023:,}')
print(f'Total de Material B requerido | 1er. Semestre: {total_material_requerido_b_1_1:,} | 2do. Semestre: {total_material_requerido_b_1_2:,} | 2023: {total_material_requerido_b_1_2023:,}')
print(f'Total de Material C requerido | 1er. Semestre: {total_material_requerido_c_1_1:,} | 2do. Semestre: {total_material_requerido_c_1_2:,} | 2023: {total_material_requerido_c_1_2023:,}')
print('Producto 2')
print(f'Total de Material A requerido | 1er. Semestre: {total_material_requerido_a_2_1:,} | 2do. Semestre: {total_material_requerido_a_2_2:,} | 2023: {total_material_requerido_a_2_2023:,}')
print(f'Total de Material B requerido | 1er. Semestre: {total_material_requerido_b_2_1:,} | 2do. Semestre: {total_material_requerido_b_2_2:,} | 2023: {total_material_requerido_b_2_2023:,}')
print(f'Total de Material C requerido | 1er. Semestre: {total_material_requerido_c_2_1:,} | 2do. Semestre: {total_material_requerido_c_2_2:,} | 2023: {total_material_requerido_c_2_2023:,}')
print('Producto 3')
print(f'Total de Material A requerido | 1er. Semestre: {total_material_requerido_a_3_1:,} | 2do. Semestre: {total_material_requerido_a_3_2:,} | 2023: {total_material_requerido_a_3_2023:,}')
print(f'Total de Material B requerido | 1er. Semestre: {total_material_requerido_b_3_1:,} | 2do. Semestre: {total_material_requerido_b_3_2:,} | 2023: {total_material_requerido_b_3_2023:,}')
print(f'Total de Material C requerido | 1er. Semestre: {total_material_requerido_c_3_1:,} | 2do. Semestre: {total_material_requerido_c_3_2:,} | 2023: {total_material_requerido_c_3_2023:,}\n')
print('Total de Requerimientos')
print(f'Material A | 1er Semestre: {material_requerido_a_1:,} | 2do. Semestre: {material_requerido_a_2:,} | 2023: {material_requerido_a_2023:,}')
print(f'Material B | 1er Semestre: {material_requerido_b_1:,} | 2do. Semestre: {material_requerido_b_2:,} | 2023: {material_requerido_b_2023:,}')
print(f'Material C | 1er Semestre: {material_requerido_c_1:,} | 2do. Semestre: {material_requerido_c_2:,} | 2023: {material_requerido_c_2023:,}')
print('~'*120)

#Operaciones 5
#1 semestre
total_materiales_a_1 = material_requerido_a_1+inventario_final_material_a_1
inventario_inicial_materiales_a_1 = inventario_final_material_a_1
material_comprar_a_1 = total_materiales_a_1-inventario_inicial_materiales_a_1
total_material_a_cash_1 = material_comprar_a_1*precio_compra_material_a_1

total_materiales_b_1 = material_requerido_b_1+inventario_final_material_b_1
inventario_inicial_materiales_b_1 = inventario_final_material_b_1
material_comprar_b_1 = total_materiales_b_1-inventario_inicial_materiales_b_1
total_material_b_cash_1 = material_comprar_b_1*precio_compra_material_b_1

total_materiales_c_1 = material_requerido_c_1+inventario_final_material_c_1
inventario_inicial_materiales_c_1 = inventario_final_material_c_1
material_comprar_c_1 = total_materiales_c_1-inventario_inicial_materiales_c_1
total_material_c_cash_1 = material_comprar_c_1*precio_compra_material_c_1

#2 semestre
total_materiales_a_2 = material_requerido_a_2+inventario_final_material_a_2
material_comprar_a_2 = total_materiales_a_2-inventario_inicial_materiales_a_1
total_material_a_cash_2 = material_comprar_a_2*precio_compra_material_a_2

total_materiales_b_2 = material_requerido_b_2+inventario_final_material_b_2
material_comprar_b_2 = total_materiales_b_2-inventario_inicial_materiales_b_1
total_material_b_cash_2 = material_comprar_b_2*precio_compra_material_b_2

total_materiales_c_2 = material_requerido_c_2+inventario_final_material_c_2
material_comprar_c_2 = total_materiales_c_2-inventario_inicial_materiales_c_1
total_material_c_cash_2 = material_comprar_c_2*precio_compra_material_c_2

#2023
material_comprar_a_2023 = material_comprar_a_1+material_comprar_a_2
material_comprar_b_2023 = material_comprar_b_1+material_comprar_b_2
material_comprar_c_2023 = material_comprar_c_1+material_comprar_c_2

total_material_a_cash_2023 = total_material_a_cash_1+total_material_a_cash_2
total_material_b_cash_2023 = total_material_b_cash_1+total_material_b_cash_2
total_material_c_cash_2023 = total_material_c_cash_1+total_material_c_cash_2

compras_totales_materiales_1 = total_material_a_cash_1+total_material_b_cash_1+total_material_c_cash_1
compras_totales_materiales_2 = total_material_a_cash_2+total_material_b_cash_2+total_material_c_cash_2
compras_totales_materiales_2023 = compras_totales_materiales_1+compras_totales_materiales_2

#Mostrar en pantalla 5
print('')
print('~'*120)
print('5. PRESUPUESTO DE COMPRA DE MATERIALES.\n')  

print('Material A')
print(f'Material a comprar | 1er. Semestre: {material_comprar_a_1:,} | 2do. Semestre: {material_comprar_a_2:,} | 2023: {material_comprar_a_2023:,}')
print(f'Total de Material A en $ | 1er. Semestre: ${total_material_a_cash_1:,} | 2do. Semestre: ${total_material_a_cash_2:,} | 2023: ${total_material_a_cash_2023:,}')
print('Material B')
print(f'Material a comprar | 1er. Semestre: {material_comprar_b_1:,} | 2do. Semestre: {material_comprar_b_2:,} | 2023: {material_comprar_b_2023:,}')
print(f'Total de Material B en $ | 1er. Semestre: ${total_material_b_cash_1:,} | 2do. Semestre: ${total_material_b_cash_2:,} | 2023: ${total_material_b_cash_2023:,}')
print('Material C')
print(f'Material a comprar | 1er. Semestre: {material_comprar_c_1:,} | 2do. Semestre: {material_comprar_c_2:,} | 2023: {material_comprar_c_2023:,}')
print(f'Total de Material C en $ | 1er. Semestre: ${total_material_c_cash_1:,} | 2do. Semestre: ${total_material_c_cash_2:,} | 2023: ${total_material_c_cash_2023:,}\n')
print(f'Compras totales | 1er. Semestre: ${compras_totales_materiales_1:,} | 2do. Semestre: ${compras_totales_materiales_2:,} | 2023: ${compras_totales_materiales_2023:,}')
print('~'*120)

#Operaciones 6
se_pagara = se_pagara/100
se_pagara2 = se_pagara2/100
total_proveedores_2023 = saldo_proveedores_2022+compras_totales_materiales_2023
proveedores2022 = saldo_proveedores_2022*se_pagara
proveedores_2023 = compras_totales_materiales_2023*se_pagara2
total_salidas_2023 = proveedores2022+proveedores_2023
saldo_proveedores_2023 = total_proveedores_2023-total_salidas_2023

#Mostrar en pantalla 6
print(' ')
print('~'*120)
print('6. DETERMINACION DEL SALDO DE PROVEEDORES Y FLUJO DE SALIDAS.\n')

print(f'Saldo de Proveedores del 2023: ${saldo_proveedores_2023:,}')
print('~'*120)

#Operaciones 7
total_horas_requeridas_1_1 = unidades_producir_1_1*horas_requeridas_unidad_1_1
importe_mod_1_1 = total_horas_requeridas_1_1*cuota_hora_1
total_horas_requeridas_2_1 = unidades_producir_2_1*horas_requeridas_unidad_2_1
importe_mod_2_1 = total_horas_requeridas_2_1*cuota_hora_1
total_horas_requeridas_3_1 = unidades_producir_3_1*horas_requeridas_unidad_3_1
importe_mod_3_1 = total_horas_requeridas_3_1*cuota_hora_1

total_horas_requeridas_1_2 = unidades_producir_1_2*horas_requeridas_unidad_1_1
importe_mod_1_2 = total_horas_requeridas_1_2*cuota_hora_2
total_horas_requeridas_2_2 = unidades_producir_2_2*horas_requeridas_unidad_2_1
importe_mod_2_2 = total_horas_requeridas_2_2*cuota_hora_2
total_horas_requeridas_3_2 = unidades_producir_3_2*horas_requeridas_unidad_3_1
importe_mod_3_2 = total_horas_requeridas_3_2*cuota_hora_2

importe_mod_1_2023 = importe_mod_1_1+importe_mod_1_2
importe_mod_2_2023 = importe_mod_2_1+importe_mod_2_2
importe_mod_3_2023 = importe_mod_3_1+importe_mod_3_2

total_horas_requeridas_1 = total_horas_requeridas_1_1+total_horas_requeridas_2_1+total_horas_requeridas_3_1
total_horas_requeridas_2 = total_horas_requeridas_1_2+total_horas_requeridas_2_2+total_horas_requeridas_3_2
total_horas_requeridas_2023 = total_horas_requeridas_1+total_horas_requeridas_2

total_mod_semestre_1 = importe_mod_1_1+importe_mod_2_1+importe_mod_3_1
total_mod_semestre_2 = importe_mod_1_2+importe_mod_2_2+importe_mod_3_2
total_mod_2023 = total_mod_semestre_1+total_mod_semestre_2

#Mostrar en pantalla 7
print('')
print('~'*120)
print('7. PRESUPUESTO DE MANO DE OBRA DIRECTA.\n')  

print('Producto 1')
print(f'Importe de M.O.D. | 1er. Semestre: ${importe_mod_1_1:,} | 2do. Semestre: ${importe_mod_1_2:,} | 2023: ${importe_mod_1_2023:,}')
print('Producto 2')
print(f'Importe de M.O.D. | 1er. Semestre: ${importe_mod_2_1:,} | 2do. Semestre: ${importe_mod_2_2:,} | 2023: ${importe_mod_2_2023:,}')
print('Producto 3')
print(f'Importe de M.O.D. | 1er. Semestre: ${importe_mod_3_1:,} | 2do. Semestre: ${importe_mod_3_2:,} | 2023: ${importe_mod_3_2023:,}\n')
print(f'Total de horas requeridas por semestre | 1er. Semestre: {total_horas_requeridas_1:,} | 2do. Semestre: {total_horas_requeridas_2:,} | 2023: {total_horas_requeridas_2023:,}\n')
print(f'Total de M.O.D. por semestre | 1er. Semestre: ${total_mod_semestre_1:,} | 2do. Semestre: ${total_mod_semestre_2:,} | 2023: ${total_mod_2023:,}')
print('~'*120)

#Operaciones 8

gif_depreciacion2 = gif_depreciacion/2
gif_seguros = gif_seguros/2
gif_varios = gif_varios/2

total_gif_1 = gif_depreciacion2+gif_seguros+gif_mantenimiento_1+gif_energeticos_1+gif_varios
total_gif_2 = gif_depreciacion2+gif_seguros+gif_mantenimiento_2+gif_energeticos_2+gif_varios
total_gif_2023 = total_gif_1+total_gif_2

costo_hora_gif = total_gif_2023/total_horas_requeridas_2023

#Mostrar en pantalla 8
print('')
print('~'*120)
print('8. PRESUPUESTO DE GASTOS INDIRECTOS DE FABRICACIÓN.\n')  

print(f'Total G.I.F. | 1er. Semestre: ${total_gif_1:,} | 2do. Semestre: ${total_gif_2:,} | 2023: ${total_gif_2023:,}\n')
print(f'Costo por Hora de G.I.F.: ${costo_hora_gif:,.2f}')
print('~'*120)

#Operaciones 9
comisiones_go = comisiones_go/100
go_depreciacion2 = go_depreciacion/2
sueldos_salarios = sueldos_salarios/2
intereses_prestamo = intereses_prestamo/2
comisiones_1 = total_ventas_1semestre*comisiones_go
comisiones_2 = total_ventas_2semestre*comisiones_go

total_gastos_operacion_1 = go_depreciacion2+sueldos_salarios+comisiones_1+go_varios_1+intereses_prestamo
total_gastos_operacion_2 = go_depreciacion2+sueldos_salarios+comisiones_2+go_varios_2+intereses_prestamo
total_gastos_operacion_2023 = total_gastos_operacion_1+total_gastos_operacion_2

#Mostrar en pantalla 9
print('')
print('~'*120)
print('9. PRESUPUESTO DE GASTOS DE OPERACIÓN.\n')  

print(f'Total de Gastos de Operacion | 1er. Semestre: ${total_gastos_operacion_1:,} | 2do. Semestre: ${total_gastos_operacion_2:,} | 2023: ${total_gastos_operacion_2023:,}')
print('~'*120)


#Operaciones 10
#producto 1
costo_unitario_a_1 = requerimiento_material_a_1_1*precio_compra_material_a_2
costo_unitario_b_1 = requerimiento_material_b_1_1*precio_compra_material_b_2
costo_unitario_c_1 = requerimiento_material_c_1_1*precio_compra_material_c_2
costo_unitario_mo_1 = cuota_hora_2*horas_requeridas_unidad_1_1
costo_unitario_gif_1 = costo_hora_gif*horas_requeridas_unidad_1_1
costo_unitario_1 = costo_unitario_a_1+costo_unitario_b_1+costo_unitario_c_1+costo_unitario_mo_1+costo_unitario_gif_1
#producto 2
costo_unitario_a_2 = requerimiento_material_a_2_1*precio_compra_material_a_2
costo_unitario_b_2 = requerimiento_material_b_2_1*precio_compra_material_b_2
costo_unitario_c_2 = requerimiento_material_c_2_1*precio_compra_material_c_2
costo_unitario_mo_2 = cuota_hora_2*horas_requeridas_unidad_2_1
costo_unitario_gif_2 = costo_hora_gif*horas_requeridas_unidad_2_1
costo_unitario_2 = costo_unitario_a_2+costo_unitario_b_2+costo_unitario_c_2+costo_unitario_mo_2+costo_unitario_gif_2
#producto 3
costo_unitario_a_3 = requerimiento_material_a_3_1*precio_compra_material_a_2
costo_unitario_b_3 = requerimiento_material_b_3_1*precio_compra_material_b_2
costo_unitario_c_3 = requerimiento_material_c_3_1*precio_compra_material_c_2
costo_unitario_mo_3 = cuota_hora_2*horas_requeridas_unidad_3_1
costo_unitario_gif_3 = costo_hora_gif*horas_requeridas_unidad_3_1
costo_unitario_3 = costo_unitario_a_3+costo_unitario_b_3+costo_unitario_c_3+costo_unitario_mo_3+costo_unitario_gif_3

#Mostrar en pantalla 10
print('')
print('~'*120)
print('10. DETERMINACIÓN DEL COSTO UNITARIO DE PRODUCTOS TERMINADOS.\n')

print(f'Producto 1 | Costo Unitario: ${costo_unitario_1:,.2f}')
print(f'Producto 2 | Costo Unitario: ${costo_unitario_2:,.2f}')
print(f'Producto 3 | Costo Unitario: ${costo_unitario_3:,.2f}')
print('~'*120)

#Operaciones 11
costo_total_material_a = inventario_final_material_a_2*precio_compra_material_a_2
costo_total_material_b = inventario_final_material_b_2*precio_compra_material_b_2
costo_total_material_c = inventario_final_material_c_2*precio_compra_material_c_2
inventario_final_materiales = costo_total_material_a+costo_total_material_b+costo_total_material_c

costo_total_producto_1 = inventario_final_1_2*costo_unitario_1
costo_total_producto_2 = inventario_final_2_2*costo_unitario_2
costo_total_producto_3 = inventario_final_3_2*costo_unitario_3
inventario_final_producto_terminado = costo_total_producto_1+costo_total_producto_2+costo_total_producto_3

#Mostrar en pantalla 11
print('')
print('~'*120)
print('\n11. VALUACIÓN DE INVENTARIOS FINALES.\n')

print(f'Inventario Final de Materiales: ${inventario_final_materiales:,}\n')
print(f'Inventario Final de Producto Terminado: ${inventario_final_producto_terminado:,.2f}')
print('~'*120)

#Presupuesto Financiero
print('\nII. PRESUPUESTO FINANCIERO.\n')
print('~'*120)
print('\nESTADO DE COSTO DE PRODUCCIÓN Y VENTAS\n')

#Operaciones
material_disponible = saldo_inicial_materiales+compras_totales_materiales_2023
materiales_utilizados = material_disponible-inventario_final_materiales
costo_produccion = materiales_utilizados+total_mod_2023+total_gif_2023
total_produccion_disponible = costo_produccion+inventario_inicial_productos_terminados
costo_ventas = total_produccion_disponible-inventario_final_producto_terminado

#Mostrar en pantalla
print('')
print('~'*120)
print('\nESTADO DE COSTO DE PRODUCCIÓN Y VENTAS.\n')

print(f'Material Disponible: {material_disponible:,}\n')
print(f'Materiales Utilizados: {materiales_utilizados:,}\n')
print(f'Costo de Produccion: {costo_produccion:,}\n')
print(f'Total de Produccion Disponible: {total_produccion_disponible:,}\n')
print(f'Costo de Ventas: ${costo_ventas:,.2f}')
print('~'*120)

#Estado de Resultados
utilidad_bruta = total_ventas_2023-costo_ventas
utilidad_operacion = utilidad_bruta-total_gastos_operacion_2023
isr = isr/100
isr_utilidad_operacion = utilidad_operacion*isr
ptu = ptu/100
ptu_utilidad_operacion = utilidad_operacion*ptu
utilidad_neta = utilidad_operacion-isr_utilidad_operacion-ptu_utilidad_operacion

#Mostrar en pantalla
print('')
print('~'*120)
print('\nESTADO DE RESULTADOS.\n')

print(f'Utilidad Bruta: ${utilidad_bruta:,.2f}\n')
print(f'Utilidad de Operacion: ${utilidad_operacion:,.2f}\n')
print(f'Utilidad Neta: ${utilidad_neta:,.2f}')
print('~'*120)

#Estado de Flujo de Efectivo
#Operaciones
saldo_inicial_efectivo
total_entradas = suma_cobranza
efectivo_disponible = saldo_inicial_efectivo+total_entradas
pago_gif = total_gif_2023-gif_depreciacion
pago_go = total_gastos_operacion_2023-go_depreciacion
total_salidas = proveedores_2023+proveedores2022+total_mod_2023+pago_gif+pago_go+compra_activo_fijo_maquinaria+pago_isr_2022+isr_utilidad_operacion
flujo_efectivo_actual = efectivo_disponible-total_salidas
#Mostrar en pantalla
print('')
print('~'*120)
print('\nESTADO DE FLUJO DE EFECTIVO.\n')

print(f'Saldo Inicial de Efectivo: ${saldo_inicial_efectivo:,}\n')
print(f'Total de Entradas: ${total_entradas:,}\n')
print(f'Efectivo Disponible: ${efectivo_disponible:,}\n')
print(f'Total de Salidas: ${total_salidas:,.2f}\n')
print(f'Flujo de Efectivo Actual: ${flujo_efectivo_actual:,.2f}')
print('~'*120)
#Corregido

#Balance General
#Operaciones
total_activos_circulantes = flujo_efectivo_actual+saldo_clientes_2023+deudores_diversos+funcionarios_empleados+inventario_final_materiales+inventario_final_producto_terminado
planta_equipo = planta_equipo_r+compra_activo_fijo_maquinaria
depreciacion_acumulada = depreciacion_acumulada_r+gif_depreciacion+go_depreciacion
total_activos_no_circulantes = terreno+planta_equipo-depreciacion_acumulada
activo_total = total_activos_circulantes+total_activos_no_circulantes

total_pasivo_corto_plazo = saldo_proveedores_2023+documentos_pagar+ptu_utilidad_operacion
total_pasivo_largo_plazo = prestamos_bancarios
pasivo_total = total_pasivo_corto_plazo+total_pasivo_largo_plazo

total_capital_contable = capital_aportado+capital_ganado+utilidad_neta
suma_pasivo_capital = pasivo_total+total_capital_contable

#Mostrar en pantalla
print('')
print('~'*120)
print('\nBALANCE GENERAL\n')

print(f'Total de Activos Circulantes: ${total_activos_circulantes:,.2f}')
print(f'Total de Activos No Circulantes: ${total_activos_no_circulantes:,}\n')
print(f'ACTIVO TOTAL: ${activo_total:,.2f}\n')
print(f'Total de Pasivo Corto Plazo: ${total_pasivo_corto_plazo:,.2f}')
print(f'Total de Pasivo Largo Plazo: ${total_pasivo_largo_plazo:,}\n')
print(f'PASIVO TOTAL: ${pasivo_total:,.2f}\n')
print(f'Total de Capital Contable: ${total_capital_contable:,.2f}\n')
print(f'SUMA DE PASIVO Y CAPITAL: ${suma_pasivo_capital:,.2f}')
print('~'*120)
#Corregido