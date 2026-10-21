"""Funcion para validar que la fecha (DD-MM-AAAA)"""
def ValidarFecha(fecha):
  
  esValida = True
  if len(fecha) != 10:
    esValida = False
  else:
    if fecha[2] != "-" or fecha[5] != "-":
      esValida = False
    else:
      indices_digitos = [0, 1, 3, 4, 6, 7, 8, 9]
      for i in indices_digitos:
        if not fecha[i].isdigit():
          esValida = False
  return esValida

"""Funcion para obtener el código del expediente"""
def ExtraerIniciales(asunto):
  asunto = asunto.upper()
  iniciales = ""
  palabra = ""
  contPalabras = 0

  for i in range(len(asunto)):
    caracter = asunto[i]
    if caracter != " ":
      palabra += caracter
    else:
      if len(palabra) >= 3 and contPalabras < 3:
        iniciales += palabra[0]
        contPalabras += 1
      palabra = ""

  if len(palabra) >= 3 and contPalabras < 3:
    iniciales += palabra[0]
    contPalabras += 1

  while len(iniciales) < 3:
    iniciales += "X"

  return iniciales

"""Funcion para dar formato correlativo de 5 dígitos (ej. 00001)"""
def FormatearNumero(num):
  numStr = str(num)
  while len(numStr) < 5:
    numStr = "0" + numStr
  return numStr

"""Funcion para ordenar expedientes"""
def OrdenarExpedientes(
    codigos,
    nombres,
    apellidos,
    fechar,
    asuntos,
    areas,
    estados,
    resoluciones,
    orden,
    totalExp,
):
  if totalExp > 1:
    for i in range(1, totalExp):
      for j in range(1, totalExp - i + 1):
        clave1 = FormatearNumero(orden[j])
        clave2 = FormatearNumero(orden[j + 1])

        if clave1 > clave2:
          # Intercambio de valores en los arreglos paralelos
          (
              codigos[j],
              codigos[j + 1],
          ) = (
              codigos[j + 1],
              codigos[j],
          )
          (
              nombres[j],
              nombres[j + 1],
          ) = (
              nombres[j + 1],
              nombres[j],
          )
          (
              apellidos[j],
              apellidos[j + 1],
          ) = (
              apellidos[j + 1],
              apellidos[j],
          )
          (
              fechar[j],
              fechar[j + 1],
          ) = (
              fechar[j + 1],
              fechar[j],
          )
          (
              asuntos[j],
              asuntos[j + 1],
          ) = (
              asuntos[j + 1],
              asuntos[j],
          )
          (
              areas[j],
              areas[j + 1],
          ) = (
              areas[j + 1],
              areas[j],
          )
          (
              estados[j],
              estados[j + 1],
          ) = (
              estados[j + 1],
              estados[j],
          )
          (
              resoluciones[j],
              resoluciones[j + 1],
          ) = (
              resoluciones[j + 1],
              resoluciones[j],
          )
          (
              orden[j],
              orden[j + 1],
          ) = (
              orden[j + 1],
              orden[j],
          )

def MostrarFicha(codigo, nombre, apellido, fecha, asunto, area, estado, resolucion):
  """Funcion para mostrar Ficha del Expediente"""
  print("-" * 50)
  print("               FICHA DE EXPEDIENTE                ")
  print("-" * 50)
  print(f"CÓDIGO     : {codigo}")
  print(f"SOLICITANTE: {nombre} {apellido}")
  print(f"FECHA      : {fecha}")
  print(f"ASUNTO     : {asunto}")
  print(f"ÁREA       : {area}")
  print(f"ESTADO     : {estado}")
  print(f"RESOLUCIÓN : {resolucion}")
  print("-" * 50)

"""Funcion para seleccionar un Área predefinida"""
def SeleccionarArea():
  opValida = False
  while not opValida:
    print("Seleccione el Área Especializada:")
    print("1. Dirección")
    print("2. Secretaría")
    print("3. Tesorería")
    print("4. Coordinación académica")
    print("5. Tutoría")
    print("6. Asociación de padres de familia")
    opAreaStr = input("Elija opción (1-6): ")

    if opAreaStr == "1":
      return "Direccion", 1
    elif opAreaStr == "2":
      return "Secretaria", 2
    elif opAreaStr == "3":
      return "Tesoreria", 3
    elif opAreaStr == "4":
      return "Coordinacion academica", 4
    elif opAreaStr == "5":
      return "Tutoria", 5
    elif opAreaStr == "6":
      return "Asociacion de padres de familia", 6
    else:
      print(
          "[ERROR] Opción no válida. Por favor, ingrese un número del 1 al 6.\n"
      )


def main():
  # Dimensionamiento de arreglos (tamaño 101 para usar índices del 1 al 100)
  codigos = [""] * 101
  nombres = [""] * 101
  apellidos = [""] * 101
  fechar = [""] * 101
  asuntos = [""] * 101
  areas = [""] * 101
  estados = [""] * 101
  resoluciones = [""] * 101
  orden = [0] * 101

  totalExp = 0
  secuenciaGlobal = 0
  op = 0

  while op != 5:
    print("\n" * 2)
    print("==================================================")
    print("        SISTEMA DE GESTIÓN DE EXPEDIENTES        ")
    print("==================================================")
    print("1. REGISTRAR EXPEDIENTES")
    print("2. ATENDER EXPEDIENTES")
    print("3. BUSCAR EXPEDIENTE")
    print("4. VISUALIZAR EXPEDIENTES")
    print("5. SALIR")
    print("--------------------------------------------------")
    opStr = input("Elija una opción (1-5): ")

    if opStr == "1":
      op = 1
      print("\n=== REGISTRAR EXPEDIENTE ===")

      while True:
        nombre = input("Ingrese nombre: ").strip()
        if len(nombre) == 0:
          print("[ERROR] El nombre no puede estar vacío.")
        else:
          break

      while True:
        apellido = input("Ingrese apellidos: ").strip()
        if len(apellido) == 0:
          print("[ERROR] El apellido no puede estar vacío.")
        else:
          break

      while True:
        fecha = input("Ingrese fecha (DD-MM-AAAA): ").strip()
        fechaOk = ValidarFecha(fecha)
        if not fechaOk:
          print(
              "[ERROR] Formato incorrecto. Debe ser DD-MM-AAAA (ej."
              " 12-10-2026)."
          )
        else:
          break

      while True:
        asunto = input(
            "Ingrese asunto (ej. TRAMITE DE BECAS SOCIOECONOMICA): "
        ).strip()
        if len(asunto) == 0:
          print("[ERROR] El asunto no puede estar vacío.")
        else:
          break

      totalExp += 1
      secuenciaGlobal += 1

      iniciales = ExtraerIniciales(asunto)
      numCorrelativo = FormatearNumero(totalExp)
      codigoGen = f"2026-{iniciales}-{numCorrelativo}"

      codigos[totalExp] = codigoGen
      nombres[totalExp] = nombre
      apellidos[totalExp] = apellido
      fechar[totalExp] = fecha
      asuntos[totalExp] = asunto
      areas[totalExp] = "Mesa de Partes"
      estados[totalExp] = "En Tramite"
      resoluciones[totalExp] = "Pendiente de atencion"
      orden[totalExp] = secuenciaGlobal

      print("\n¡EXPEDIENTE REGISTRADO CON ÉXITO!")
      MostrarFicha(
          codigoGen,
          nombre,
          apellido,
          fecha,
          asunto,
          areas[totalExp],
          estados[totalExp],
          resoluciones[totalExp],
      )

      input("Presione Enter para continuar...")

    elif opStr == "2":
      op = 2
      print("\n=== ATENDER EXPEDIENTES ===")
      if totalExp == 0:
        print("No hay expedientes registrados.")
      else:
        posOk = False
        while not posOk:
          print("Expedientes registrados:")
          for i in range(1, totalExp + 1):
            print(
                f"- [{codigos[i]}] | {nombres[i]} {apellidos[i]} | Asunto:"
                f" {asuntos[i]} (Estado: {estados[i]})"
            )
          print("")
          codigoIngresado = input(
              "Ingrese el CÓDIGO del expediente a atender: "
          ).strip().upper()

          codigoExiste = False
          yaAtendido = False
          posElegida = 0

          for i in range(1, totalExp + 1):
            if codigos[i].upper() == codigoIngresado:
              codigoExiste = True
              if estados[i] == "Atendido":
                yaAtendido = True
              elif (
                  estados[i] == "En Tramite"
                  or estados[i] == "Pendiente de atencion"
              ):
                posElegida = i

          if not codigoExiste:
            print("[ERROR] Código incorrecto. El expediente no existe.\n")
          else:
            if yaAtendido:
              print("[ERROR] El expediente ya se encuentra ATENDIDO.\n")
            else:
              if posElegida > 0:
                posOk = True
              else:
                print(
                    "[ERROR] El expediente ya fue derivado o atendido"
                    " anteriormente.\n"
                )

        print("\n--- DESIGNACIÓN DE ÁREA ---")
        print(f"Expediente seleccionado: {codigos[posElegida]} - {asuntos[posElegida]}\n")

        areaOriginal, numOpArea1 = SeleccionarArea()
        areas[posElegida] = areaOriginal

        print("")
        while True:
          res = input(
              f"¿El área asignada ({areas[posElegida]}) puede resolver el"
              " expediente? (SI/NO): "
          ).strip().upper()
          if res != "SI" and res != "NO":
            print("[ERROR] Respuesta no válida. Debe ingresar SI o NO.")
          else:
            break

        if res == "SI":
          while True:
            resoluciones[posElegida] = input(
                "Ingrese el detalle/forma de resolución: "
            ).strip()
            if len(resoluciones[posElegida]) == 0:
              print("[ERROR] Debe especificar la resolución.")
            else:
              break
          estados[posElegida] = "Atendido"
        else:
          print("\nEl área no pudo resolverlo.")
          while True:
            detalleDerivacion = input(
                "Ingrese el motivo/detalle por el cual se deriva: "
            ).strip()
            if len(detalleDerivacion) == 0:
              print("[ERROR] Debe ingresar el motivo de derivación.")
            else:
              break

          estados[posElegida] = f"Derivado (Op. {numOpArea1})"
          resoluciones[posElegida] = detalleDerivacion

          print("\n=== SELECCIONE LA NUEVA ÁREA PARA DERIVAR ===")
          otraArea, numOpArea2 = SeleccionarArea()

          print("")
          while True:
            resOtraArea = input(
                f"¿La nueva área ({otraArea}) puede resolver el expediente"
                " ahora mismo? (SI/NO): "
            ).strip().upper()
            if resOtraArea != "SI" and resOtraArea != "NO":
              print("[ERROR] Respuesta no válida. Debe ingresar SI o NO.")
            else:
              break

          while True:
            resFinal = input(
                "Ingrese la resolución final / detalle de atención de la nueva"
                " área: "
            ).strip()
            if len(resFinal) == 0:
              print("[ERROR] Debe ingresar la resolución final.")
            else:
              break

          totalExp += 1
          secuenciaGlobal += 1

          codigos[totalExp] = codigos[posElegida]
          nombres[totalExp] = nombres[posElegida]
          apellidos[totalExp] = apellidos[posElegida]
          fechar[totalExp] = fechar[posElegida]
          asuntos[totalExp] = asuntos[posElegida]
          areas[totalExp] = otraArea

          if resOtraArea == "SI":
            estados[totalExp] = "Atendido"
          else:
            estados[totalExp] = "En Tramite"
          resoluciones[totalExp] = resFinal
          orden[totalExp] = secuenciaGlobal

        OrdenarExpedientes(
            codigos,
            nombres,
            apellidos,
            fechar,
            asuntos,
            areas,
            estados,
            resoluciones,
            orden,
            totalExp,
        )
        print("\n¡ATENCIÓN/DERIVACIÓN REGISTRADA EXITOSAMENTE!")

      input("Presione Enter para continuar...")

    elif opStr == "3":
      op = 3
      print("\n=== BUSCAR EXPEDIENTE ===")
      if totalExp == 0:
        print("No hay expedientes registrados.")
      else:
        while True:
          print("Buscar por:")
          print("1. Código")
          print("2. Fecha")
          print("3. Nombre o Apellido")
          opBuscarStr = input("Elija opción (1-3): ").strip()
          if opBuscarStr not in ["1", "2", "3"]:
            print("[ERROR] Opción no válida. Ingrese 1, 2 o 3.\n")
          else:
            break

        while True:
          if opBuscarStr == "1":
            busqueda = input(
                "Ingrese el CÓDIGO a buscar (ej. 2026-TBC-00001): "
            ).strip()
          elif opBuscarStr == "2":
            busqueda = input("Ingrese la FECHA a buscar (DD-MM-AAAA): ").strip()
          else:
            busqueda = input("Ingrese el NOMBRE o APELLIDO a buscar: ").strip()

          if len(busqueda) == 0:
            print("[ERROR] El término de búsqueda no puede estar vacío.\n")
          else:
            break

        busqueda = busqueda.upper()
        encontrado = False

        for i in range(1, totalExp + 1):
          if opBuscarStr == "1":
            if codigos[i].upper() == busqueda:
              MostrarFicha(
                  codigos[i],
                  nombres[i],
                  apellidos[i],
                  fechar[i],
                  asuntos[i],
                  areas[i],
                  estados[i],
                  resoluciones[i],
              )
              encontrado = True
          elif opBuscarStr == "2":
            if fechar[i] == busqueda:
              MostrarFicha(
                  codigos[i],
                  nombres[i],
                  apellidos[i],
                  fechar[i],
                  asuntos[i],
                  areas[i],
                  estados[i],
                  resoluciones[i],
              )
              encontrado = True
          elif opBuscarStr == "3":
            if (
                nombres[i].upper() == busqueda
                or apellidos[i].upper() == busqueda
            ):
              MostrarFicha(
                  codigos[i],
                  nombres[i],
                  apellidos[i],
                  fechar[i],
                  asuntos[i],
                  areas[i],
                  estados[i],
                  resoluciones[i],
              )
              encontrado = True

        if not encontrado:
          print("No se encontraron expedientes con la información ingresada.")

      input("Presione Enter para continuar...")

    elif opStr == "4":
      op = 4
      print("\n=== VISUALIZACIÓN DE EXPEDIENTES ===")
      if totalExp == 0:
        print("No hay expedientes registrados para mostrar.")
      else:
        print("-" * 95)
        print(
            f"{'CÓDIGO':<15} | {'FECHA':<10} | {'SOLICITANTE':<25} |"
            f" {'ÁREA':<30} | {'ESTADO':<15}"
        )
        print("-" * 95)
        for i in range(1, totalExp + 1):
          solicitante = f"{nombres[i]} {apellidos[i]}"
          print(
              f"{codigos[i]:<15} | {fechar[i]:<10} | {solicitante:<25} |"
              f" {areas[i]:<30} | {estados[i]:<15}"
          )
        print("-" * 95)
      input("Presione Enter para continuar...")

    elif opStr == "5":
      op = 5
      print("Nos vemos luego. Gracias por usar el sistema.")
    else:
      op = 0
      print("[ERROR] Opción no válida. Intente de nuevo.")
      input("Presione Enter para continuar...")


if __name__ == "__main__":
  main()