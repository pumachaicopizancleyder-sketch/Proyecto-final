import json
from pathlib import Path
from datetime import datetime
from tempfile import NamedTemporaryFile
carpeta_proyecto = Path(__file__).resolve().parent
ruta = carpeta_proyecto / "expedientes.txt" / "registro.txt"
def guardar_expedientes(ruta, expedientes):
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta_temporal = None
    try:
        with NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=ruta.parent,
            prefix="registro-",
            suffix=".tmp",
            delete=False
        ) as archivo:
            ruta_temporal = Path(archivo.name)
            json.dump(expedientes, archivo, ensure_ascii=False, indent=2)
        ruta_temporal.replace(ruta)
    finally:
        if ruta_temporal is not None:
            ruta_temporal.unlink(missing_ok=True)
def cargar_expedientes(ruta):
    if not ruta.exists():
        return []
    with ruta.open("r", encoding="utf-8") as archivo:
        return json.load(archivo)
def selecionar_asunto():
    asuntos = [
        "Solicitud de Vacante",
        "Constancia de Estudios",
        "Constancia de Matricula",
        "Solicitud de Traslado",
        "Solicitid de Exoneracion",
        "Justificacion de Inasistencia",
        "Rectificación de Nombre y/o Apellido",
        "Certificado de Estudios",
        "Constancia de practicas",
        "Certificado de Conducta",
        "Examen de subsanación",
        "Otros"]
    while True:
        print("==RESUMEN DE SOLICITUD==")
        for i, asunto in enumerate(asuntos, start=1):
            print(f"{i}.{asunto}")
        opcion = input("Elija un asunto(1-12): ")
        if opcion.isdecimal() and 1<= int(opcion) <= len(asuntos):
            asunto = asuntos[int(opcion) - 1]
            if asunto == "Otros":
                asunto = input("Especifique el asunto: ").strip()
                while asunto == "":
                    asunto = input("Especifique el asunto: ").strip()
            return asunto
        print ("Opción inválida. Ingrese un número del 1 al 12")
def mostrar_ficha(expediente):
    print("-" * 55)
    print("FICHA DE EXPEDIENTE".center(55))
    print(f"CÓDIGO     : {expediente['Código']}")
    print(f"SOLICITANTE: {expediente['Nombre']} {expediente['Apellido']}")
    print(f"DNI        : {expediente['DNI']}")
    print(f"TELEFONO   : {expediente['Telefono']}")
    print(f"CORREO     : {expediente['Correo']}")
    print(f"FECHA      : {expediente['Fecha']}")
    print(f"HORA       : {expediente['Hora']}")
    print(f"ASUNTO     : {expediente['Asunto']}")
    print(f"FOLIO      : {expediente['Folio']}")
    print(f"ÁREA       : {expediente['Area']}")
    print(f"ESTADO     : {expediente['Estado']}")
    print("-" * 55)
def formatear_listado(expedientes):
    filas = [["CÓDIGO", "FECHA", "SOLICITANTE", "ÁREA", "ESTADO"]]

    for expediente in expedientes:
        filas.append([
            str(expediente["Código"]),
            str(expediente["Fecha"]),
            f"{expediente['Nombre']} {expediente['Apellido']}",
            str(expediente.get("Area", "Mesa de Partes")),
            str(expediente.get("Estado", "Registrado"))
        ])

    anchos = [18, 10, 30, 30, 15]
    for fila in filas:
        for columna, valor in enumerate(fila):
            anchos[columna] = max(anchos[columna], len(valor))

    filas_formateadas = []
    for fila in filas:
        columnas = []
        for columna, valor in enumerate(fila):
            columnas.append(valor.ljust(anchos[columna]))
        filas_formateadas.append(" | ".join(columnas))

    separador = "-" * len(filas_formateadas[0])
    lineas = [separador, filas_formateadas[0], separador]
    lineas.extend(filas_formateadas[1:])
    lineas.append(separador)
    return "\n".join(lineas) + "\n"
def guardar_listado(ruta_tabla, expedientes):
    with ruta_tabla.open("w", encoding="utf-8") as archivo:
        archivo.write("=== LISTADO DE EXPEDIENTE===\n")
        archivo.write(formatear_listado(expedientes))
def generar_codigo(expedientes, anio):
    ultimo_numero = 0
    for expediente in expedientes:
        numero = expediente.get("Código", "").split("-")[-1]
        if numero.isdecimal():
            ultimo_numero = max(ultimo_numero, int(numero))
    return f"{anio}-EXP-{ultimo_numero + 1:04d}"
def registrar_expediente(ruta, expedientes_guardados):
    print("==REGISTRAR EXPEDIENTES==")
    ahora = datetime.now()
    #Asignacion de Código
    codigo = generar_codigo(expedientes_guardados, ahora.year)
    #Registro Nombre
    while True:
        nombre = input("Ingrese nombre: ").strip()
        if len(nombre) == 0:
            print("[ERROR]El nombre no puede estar vacío")
        else:
            break
    #Registro Apellido
    while True: 
        apellido = input("Ingrese Apellido: ").strip()
        if len(apellido) == 0:
            print("[ERROR]El apellido no puede estar vacio")
        else:
            break
    #Registro DNI
    while True:
        dni = input("Ingrese DNI(8 dígitos): ").strip()
        if len(dni) != 8 or not dni.isdecimal():
            print("[ERROR]Ingrese correctamente el DNI(8 dígitos -> 75428961)")
        else:
            break
    #Registro Telefono
    while True:
        telefono = input("Ingrese teléfono(9 dígitos): ").strip()
        if len(telefono) != 9 or not telefono.isdecimal():
            print("[EROR]Ingrese telefeno correctamente(9 dígitos -> 978526412)")
        else:
            break
    #Registro Email
    while True:
        email = input("Ingrese su correo email: ").strip()
        if len(email) == 0:
            print("[ERROR]Ingrese su correo correctamente")
        elif not email.endswith("@gmail.com"):
            print("[ERROR]Ingrese su correo correctamente")
            print("El correo tiene que tener @gmail.com al final")
        else:
            break
    #Registro Asunto
    asunto = selecionar_asunto()
    print(f"Asunto selecionado: {asunto}")
    #Registro Fecha
    fecha = ahora.strftime("%d-%m-%Y")
    #Registro Hora
    hora = ahora.strftime("%H:%M")
    #Registro Folio
    while True:
        folio = input("Ingrese folio de solicitud: ")
        if not folio.isdecimal() or int(folio) < 2:
            print("Ingrese folio correctamente")
            print("El folio mínimo es 2")
        else:
            break
    expediente = {
        "Código" : codigo, 
        "Nombre": nombre, 
        "Apellido":apellido, 
        "DNI": dni,
        "Telefono": telefono,
        "Correo": email,
        "Fecha": fecha,
        "Hora": hora,
        "Asunto": asunto,
        "Folio": folio,
        "Area": "Mesa de Partes",
        "Estado": "Registrado"}
    expedientes_actualizados = expedientes_guardados + [expediente]
    try:
        guardar_expedientes(ruta, expedientes_actualizados)
    except OSError as error:
        print(f"No se pudo guardar el expediente: {error}")
        input("Presione Enter para continuar...")
        return

    expedientes_guardados.append(expediente)
    try:
        guardar_listado(ruta.parent / "listado.txt", expedientes_guardados)
    except OSError as error:
        print(f"Expediente guardado. No se pudo actualizar listado.txt: {error}")
    print("\n¡EXPEDIENTE REGISTRADO CON ÉXITO!")
    mostrar_ficha(expediente)
    input("Presione Enter para continuar...")
def buscar_por_código(expedientes, codigo):
    codigo = codigo.strip().upper()
    if codigo == "":
        return None
    for expediente in expedientes:
        if expediente.get("Código", "").upper() == codigo:
            return expediente
    return None
def seleccionar_area():
    areas = [
        "Mesa de Partes",
        "Dirección",
        "Sub Dirección Primaria",
        "Sub Dirección Secundaria",
        "Coordinación Pedagógica",
        "Coordinación de TOE",
        "Secretaria",
        "Psicología",
        "Comité de Convivencia"
    ]
    while True:
        print("\n=== ÁREA DE DESTINO ===")
        for numero, area in enumerate(areas, start=1):
            print(f"{numero}. {area}")
        print("0. Cancelar")
        opcion = input("Seleccione el área especializada( 1-9): ").strip()
        if opcion == "0":
            return None
        if opcion.isdecimal() and 1<= int(opcion) <= len(areas):
            return areas[int(opcion) - 1]
        print("Opción inválida. Ingrese un número del 0 al 9")
def seleccionar_estado():
    estados = [
        "Registrado",
        "En Revisión",
        "Observado",
        "Derivado",
        "En Proceso",
        "Aprobado",
        "Rechazado",
        "Archivado"
    ]
    while True:
        print("\n=== ACTUALIZACIÓN DE ESTADO ===")
        for numero, estado in enumerate(estados, start=1):
            print(f"{numero}. {estado}")
        print("0. Cancelar")
        opcion = input("Seleccione un estado (1-8): ").strip()
        if opcion == "0":
            return None
        if opcion.isdecimal() and 1 <= int(opcion) <= len(estados):
            return estados[int(opcion) - 1]
        print("[ERROR] Opción inválida, ingrese un número del 0 al 8")
def solicitar_detalle(mensaje):
    while True:
        detalle = input(f"{mensaje} (0 para cancelar): ").strip()
        if detalle == "0":
            return None
        if detalle != "":
            return detalle
        print("El detalle no puede estar vacío.")
def registrar_movimiento(ruta, expedientes, seleccionado, nueva_area, nuevo_estado, detalle, accion):
    ahora = datetime.now()
    movimiento = {
        "Fecha": ahora.strftime("%d-%m-%Y"),
        "Hora": ahora.strftime("%H:%M"),
        "Accion": accion,
        "AreaOrigen": seleccionado["Area"],
        "AreaDestino": nueva_area,
        "EstadoAnterior": seleccionado["Estado"],
        "EstadoNuevo": nuevo_estado,
        "Detalle": detalle
    }

    actualizado = seleccionado.copy()
    actualizado["Area"] = nueva_area
    actualizado["Estado"] = nuevo_estado
    actualizado["Historial"] = list(seleccionado.get("Historial") or [])
    actualizado["Historial"].append(movimiento)

    expedientes_actualizados = expedientes.copy()
    posicion = expedientes.index(seleccionado)
    expedientes_actualizados[posicion] = actualizado

    try:
        guardar_expedientes(ruta, expedientes_actualizados)
    except OSError as error:
        print(f"No se pudo guardar la atención: {error}")
        return False

    seleccionado.update(actualizado)

    try:
        guardar_listado(ruta.parent / "listado.txt", expedientes)
    except OSError as error:
        print(f"Atención guardada. No se pudo actualizar listado.txt: {error}")

    return True
def mostrar_historial(expediente):
    print("\n=== SEGUIMIENTO DEL EXPEDIENTE ===")
    print(f"Expediente: {expediente['Código']} - {expediente['Asunto']}")
    print(f"Fecha de registro: {expediente['Fecha']} {expediente['Hora']}")
    print(f"Área actual: {expediente['Area']}")
    print(f"Estado actual: {expediente['Estado']}")

    historial = expediente.get("Historial") or []
    if len(historial) == 0:
        print("Todavía no hay movimientos de atención registrados.")
        return

    for numero, movimiento in enumerate(historial, start=1):
        print("-" * 55)
        print(
            f"Movimiento {numero} | {movimiento.get('Fecha', '')} "
            f"{movimiento.get('Hora', '')} | "
            f"{movimiento.get('Accion', 'Atención')}"
        )
        print(
            f"Área: {movimiento.get('AreaOrigen', '')} -> "
            f"{movimiento.get('AreaDestino', '')}"
        )
        print(
            f"Estado: {movimiento.get('EstadoAnterior', '')} -> "
            f"{movimiento.get('EstadoNuevo', '')}"
        )
        print(f"Detalle: {movimiento.get('Detalle', '')}")

    print("-" * 55)
def atender_expediente(ruta,expedientes):
    print("\n === ATENDER EXPEDIENTES ===")
    if len(expedientes) == 0:
        print("No hay expedientes registrados")
        input("Presione Enter para continuar...")
        return
    print("--- Expedientes Registrados---")
    for expediente in expedientes:
        solicitante = f"{expediente["Nombre"]} {expediente["Apellido"]}"
        print(
            f"-[{expediente["Código"]}] | {solicitante} | "
            f"Asunto: {expediente["Asunto"]} | Estado: {expediente["Estado"]}"
        )
    while True:
        codigo = input(
            "\nIngrese el código del expediente a atender (0 para volver): "
        ).strip()
        if codigo == "0":
            return
        seleccionado = buscar_por_código(expedientes, codigo)
        if seleccionado is not None:
            break
        print("Código incorrecto. El expediente no existe")
    mostrar_ficha(seleccionado)

    while True:
        print("\n=== ACCIONES DE ATENCIÓN ===")
        print(
            f"Expediente seleccionado: {seleccionado['Código']} - "
            f"{seleccionado['Asunto']}"
        )
        print(f"Área actual: {seleccionado['Area']}")
        print(f"Estado actual: {seleccionado['Estado']}")
        print("1. Designar área y actualizar estado")
        print("2. Actualizar estado en el área actual")
        print("3. Ver seguimiento")
        print("4. Reabrir expediente")
        print("5. Archivar expediente")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una acción: ").strip()

        if opcion == "0":
            return

        if opcion == "3":
            mostrar_historial(seleccionado)
            input("Presione Enter para continuar...")
            continue

        cerrado = seleccionado["Estado"] in (
            "Aprobado", "Rechazado", "Archivado"
        )
        if opcion in ("1", "2") and cerrado:
            print("Para continuar la atención, elija Reabrir expediente.")
            continue

        nueva_area = seleccionado["Area"]
        mensaje_detalle = "Ingrese el detalle de esta atención"

        if opcion == "1":
            print("\n--- DESIGNACIÓN DE ÁREA ---")
            print(
                f"Expediente seleccionado: {seleccionado['Código']} - "
                f"{seleccionado['Asunto']}"
            )
            nueva_area = seleccionar_area()
            if nueva_area is None:
                continue
            nuevo_estado = seleccionar_estado()
            accion = "Designación de área"
        elif opcion == "2":
            nuevo_estado = seleccionar_estado()
            accion = "Actualización de estado"
        elif opcion == "4":
            if not cerrado:
                print("El expediente ya está activo.")
                continue
            nuevo_estado = "En Revisión"
            accion = "Reapertura"
            mensaje_detalle = "Ingrese el motivo de la reapertura"
        elif opcion == "5":
            if seleccionado["Estado"] == "Archivado":
                print("El expediente ya está archivado.")
                continue
            nuevo_estado = "Archivado"
            accion = "Archivo"
            mensaje_detalle = "Ingrese el motivo del archivado"
        else:
            print("Opción inválida. Ingrese un número del 0 al 5.")
            continue

        if nuevo_estado is None:
            continue
        if nuevo_estado == "Derivado":
            while nueva_area == seleccionado["Area"]:
                print("\n--- DERIVACIÓN DE EXPEDIENTE ---")
                print(
                    f"Expediente seleccionado: {seleccionado['Código']} - "
                    f"{seleccionado['Asunto']}"
                )
                print(f"Área de origen: {seleccionado['Area']}")
                nueva_area = seleccionar_area()
                if nueva_area is None:
                    break
                if nueva_area == seleccionado["Area"]:
                    print("El área de destino debe ser diferente al área de origen.")

            if nueva_area is None:
                continue
            accion = "Derivación"
            mensaje_detalle = "Ingrese el motivo de la derivación"
        if nuevo_estado == "Archivado":
            accion = "Archivo"

        detalle = solicitar_detalle(mensaje_detalle)
        if detalle is None:
            continue

        area_origen = seleccionado["Area"]
        guardado = registrar_movimiento(
            ruta, expedientes, seleccionado, nueva_area, nuevo_estado,
            detalle, accion
        )
        if guardado:
            if nuevo_estado == "Derivado":
                print("\nExpediente derivado correctamente.")
                print(f"Área de origen: {area_origen}")
                print(f"Área de destino: {nueva_area}")
                print("Estado: Derivado")
            else:
                print("\nAtención registrada correctamente.")
            mostrar_ficha(seleccionado)
            if nuevo_estado in ("Aprobado", "Rechazado"):
                print(f"Resultado del expediente: {nuevo_estado}")
            input("Presione Enter para continuar...")
def buscar_por_fecha(expedientes, fecha):
    fecha = fecha.strip()
    resultados = []
    if fecha == "":
        return resultados
    for expediente in expedientes:
        if expediente["Fecha"] == fecha:
            resultados.append(expediente)
    return resultados
def buscar_por_nombre(expedientes, texto):
    texto = texto.strip().upper()
    resultados = []
    if texto =="":
        return resultados
    for expediente in expedientes:
        nombre_completo = f"{expediente["Nombre"]} {expediente["Apellido"]}"
        if texto in nombre_completo.upper():
            resultados.append(expediente)
    return resultados
def buscar_expediente(expedientes):
    if len(expedientes) == 0:
        print("NO HAY EXPEDIENTES REGISTRADOS!")
        input("Presione Enter para continuar...")
        return
    while True:
        print("\n=== BUSCAR EXPEDIENTE ===")
        print("1. Buscar por código")
        print("2. Buscar por fecha(DD-MM-AAAA)")
        print("3. Buscar por nombre o apellido")
        print("0. Volver al menú principal")
        opcion = input("Selecione un criterio: ").strip()
        if opcion == "0":
            return
        if opcion not in ("1", "2", "3"):
            print("Opción inválida")
            continue
        texto = input("Ingrese el dato a buscar (0 para cambiar criterio): ").strip()
        if texto == "0":
            continue
        if texto == "":
            print("El dato de búsqueda no puede estar vacío")
            continue
        if opcion == "1":
            resultados = []
            encontrado = buscar_por_código(expedientes, texto)
            if encontrado is not None:
                resultados.append(encontrado)
        elif opcion == "2":
            resultados = buscar_por_fecha(expedientes, texto)
        else:
            resultados = buscar_por_nombre(expedientes, texto)
        if len(resultados) == 0:
            print("No se encontraron expedientes")
        else:
            print(f"Expediente encontrado: {len(resultados)}")
            for expediente in resultados:
                mostrar_ficha(expediente)
                mostrar_historial(expediente)
        input("Presione Enter para continuar...")
def visualizar_expedientes(expedientes):
    print("\n=== VISUALIZACIÓN DE EXPEDIENTES ===")

    if len(expedientes) == 0:
        print("No hay expedientes registrados para mostrar.")
    else:
        print(formatear_listado(expedientes), end="")

    input("Presione Enter para continuar...")

expedientes_guardados=cargar_expedientes(ruta)
def mostrar_menu():
    op = 0
    while op != 5:
        print("==================================================")
        print("        SISTEMA DE GESTIÓN DE EXPEDIENTES        ")
        print("==================================================")
        print("1. REGISTRAR EXPEDIENTES")
        print("2. ATENDER EXPEDIENTES")
        print("3. BUSCAR EXPEDIENTE")
        print("4. VISUALIZAR EXPEDIENTE")
        print("5. SALIR")
        try: 
            op = int(input("Elija una opción(1-5): "))
            if op == 1:
                registrar_expediente(ruta, expedientes_guardados)
            elif op == 2:
                atender_expediente(ruta, expedientes_guardados)
            elif op == 3:
                buscar_expediente(expedientes_guardados)
            elif op == 4:
                visualizar_expedientes(expedientes_guardados)
            elif op == 5:
                print("NOS VEMOS LUEGO, GRACIAS POR USAR EL SISTEMA")
                break
            else:
                print("Opcion inválida, ingrese una opcion de 1-5")
        except ValueError:
            print("Opcion inválida, ingrese una opcion de 1-5")
mostrar_menu()