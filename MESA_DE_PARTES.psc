// Funcion para validar que la fecha tenga el formato estricto DD-MM-AAAA
Funcion  esValida <- ValidarFecha(fecha)
	Definir esValida Como Logico
	Definir i Como Entero
	esValida <- Verdadero
	
	Si Longitud(fecha) <> 10 Entonces
		esValida <- Falso
	SiNo
		Si Subcadena(fecha, 3, 3) <> "-" O Subcadena(fecha, 6, 6) <> "-" Entonces
			esValida <- Falso
		SiNo
			Para i <- 1 Hasta 10 Hacer
				Si i <> 3 Y i <> 6 Entonces
					Si Subcadena(fecha, i, i) < "0" O Subcadena(fecha, i, i) > "9" Entonces
						esValida <- Falso
					FinSi
				FinSi
			FinPara
		FinSi
	FinSi
FinFuncion

// Funcion para limpiar y obtener iniciales de 3 letras del asunto
Funcion iniciales <- ExtraerIniciales(asunto)
	Definir iniciales, palabra Como Cadena
	Definir i, len, contPalabras Como Entero
	asunto <- Mayusculas(asunto)
	len <- Longitud(asunto)
	iniciales <- ""
	palabra <- ""
	contPalabras <- 0
	
	Para i <- 1 Hasta len Hacer
		Si Subcadena(asunto, i, i) <> " " Entonces
			palabra <- Concatenar(palabra, Subcadena(asunto, i, i))
		SiNo
			Si Longitud(palabra) >= 3 Y contPalabras < 3 Entonces
				iniciales <- Concatenar(iniciales, Subcadena(palabra, 1, 1))
				contPalabras <- contPalabras + 1
			FinSi
			palabra <- ""
		FinSi
	FinPara
	
	Si Longitud(palabra) >= 3 Y contPalabras < 3 Entonces
		iniciales <- Concatenar(iniciales, Subcadena(palabra, 1, 1))
		contPalabras <- contPalabras + 1
	FinSi
	
	Mientras Longitud(iniciales) < 3 Hacer
		iniciales <- Concatenar(iniciales, "X")
	FinMientras
FinSubProceso

// Funcion para dar formato correlativo de 5 dígitos (ej. 00001)
Funcion numStr <- FormatearNumero(num)
	Definir numStr Como Cadena
	numStr <- ConvertirATexto(num)
	Mientras Longitud(numStr) < 5 Hacer
		numStr <- Concatenar("0", numStr)
	FinMientras
FinFuncion

// Funcion para ordenar expedientes estrictamente por orden cronológico
Funcion OrdenarExpedientes(codigos Por Referencia, nombres Por Referencia, apellidos Por Referencia, fechar Por Referencia, asuntos Por Referencia, areas Por Referencia, estados Por Referencia, resoluciones Por Referencia, orden Por Referencia, totalExp Por Referencia)
	Definir i, j Como Entero
	Definir tempCod, tempNom, tempApe, tempFec, tempAsu, tempAre, tempEst, tempRes Como Cadena
	Definir tempOrd Como Entero
	Definir clave1, clave2 Como Cadena
	
	Si totalExp > 1 Entonces
		Para i <- 1 Hasta totalExp - 1 Hacer
			Para j <- 1 Hasta totalExp - i Hacer
				clave1 <- FormatearNumero(orden[j])
				clave2 <- FormatearNumero(orden[j+1])
				
				Si clave1 > clave2 Entonces
					tempCod <- codigos[j]
					codigos[j] <- codigos[j+1]
					codigos[j+1] <- tempCod
					
					tempNom <- nombres[j]
					nombres[j] <- nombres[j+1]
					nombres[j+1] <- tempNom
					
					tempApe <- apellidos[j]
					apellidos[j] <- apellidos[j+1]
					apellidos[j+1] <- tempApe
					
					tempFec <- fechar[j]
					fechar[j] <- fechar[j+1]
					fechar[j+1] <- tempFec
					
					tempAsu <- asuntos[j]
					asuntos[j] <- asuntos[j+1]
					asuntos[j+1] <- tempAsu
					
					tempAre <- areas[j]
					areas[j] <- areas[j+1]
					areas[j+1] <- tempAre
					
					tempEst <- estados[j]
					estados[j] <- estados[j+1]
					estados[j+1] <- tempEst
					
					tempRes <- resoluciones[j]
					resoluciones[j] <- resoluciones[j+1]
					resoluciones[j+1] <- tempRes
					
					tempOrd <- orden[j]
					orden[j] <- orden[j+1]
					orden[j+1] <- tempOrd
				FinSi
			FinPara
		FinPara
	FinSi
FinSubProceso

// Funcion para mostrar Ficha del Expediente
Funcion MostrarFicha(codigo, nombre, apellido, fecha, asunto, area, estado, resolucion)
	Escribir "--------------------------------------------------"
	Escribir "               FICHA DE EXPEDIENTE                "
	Escribir "--------------------------------------------------"
	Escribir "CÓDIGO     : ", codigo
	Escribir "SOLICITANTE: ", nombre, " ", apellido
	Escribir "FECHA      : ", fecha
	Escribir "ASUNTO     : ", asunto
	Escribir "ÁREA       : ", area
	Escribir "ESTADO     : ", estado
	Escribir "RESOLUCIÓN : ", resolucion
	Escribir "--------------------------------------------------"
FinFuncion

// Funcion para seleccionar un Área predefinida
Funcion areaNom <- SeleccionarArea(numOp Por Referencia)
	Definir opAreaStr, areaNom Como Cadena
	Definir opValida Como Logico
	
	opValida <- Falso
	Repetir
		Escribir "Seleccione el Área Especializada:"
		Escribir "1. Dirección"
		Escribir "2. Secretaría"
		Escribir "3. Tesorería"
		Escribir "4. Coordinación académica"
		Escribir "5. Tutoría"
		Escribir "6. Asociación de padres de familia"
		Escribir "Elija opción (1-6): "
		Leer opAreaStr
		
		Segun opAreaStr Hacer
			"1":
				areaNom <- "Direccion"
				numOp <- 1
				opValida <- Verdadero
			"2":
				areaNom <- "Secretaria"
				numOp <- 2
				opValida <- Verdadero
			"3":
				areaNom <- "Tesoreria"
				numOp <- 3
				opValida <- Verdadero
			"4":
				areaNom <- "Coordinacion academica"
				numOp <- 4
				opValida <- Verdadero
			"5":
				areaNom <- "Tutoria"
				numOp <- 5
				opValida <- Verdadero
			"6":
				areaNom <- "Asociacion de padres de familia"
				numOp <- 6
				opValida <- Verdadero
			De Otro Modo:
				Escribir "[ERROR] Opción no válida. Por favor, ingrese un número del 1 al 6."
				Escribir ""
		FinSegun
	Hasta Que opValida
FinFuncion

// ALGORITMO PRINCIPAL
Algoritmo MESA_DE_PARTES
	Dimension codigos[100]
	Dimension nombres[100]
	Dimension apellidos[100]
	Dimension fechar[100]
	Dimension asuntos[100]
	Dimension areas[100]
	Dimension estados[100]
	Dimension resoluciones[100]
	Dimension orden[100]
	
	Definir totalExp, op, i, posElegida, numOpArea1, numOpArea2, secuenciaGlobal Como Entero
	Definir nombre, apellido, fecha, asunto, codigoGen, iniciales, numCorrelativo, res, otraArea, busqueda, opStr, codigoIngresado, opBuscarStr, detalleDerivacion, resFinal, areaOriginal, resOtraArea Como Cadena
	Definir encontrado, fechaOk, posOk, codigoExiste, yaAtendido Como Logico
	
	totalExp <- 0
	secuenciaGlobal <- 0
	op <- 0
	
	Repetir
		Borrar Pantalla
		Escribir "=================================================="
		Escribir "        SISTEMA DE GESTIÓN DE EXPEDIENTES        "
		Escribir "=================================================="
		Escribir "1. REGISTRAR EXPEDIENTES" 
		Escribir "2. ATENDER EXPEDIENTES"
		Escribir "3. BUSCAR EXPEDIENTE"
		Escribir "4. VISUALIZAR EXPEDIENTES"
		Escribir "5. SALIR"
		Escribir "--------------------------------------------------"
		Escribir "Elija una opción (1-5): "
		Leer opStr
		
		Segun opStr Hacer
			"1":
				op <- 1
				Borrar Pantalla
				Escribir "=== REGISTRAR EXPEDIENTE ==="
				
				Repetir
					Escribir "Ingrese nombre: "
					Leer nombre
					Si Longitud(nombre) = 0 Entonces
						Escribir "[ERROR] El nombre no puede estar vacío."
					FinSi
				Hasta Que Longitud(nombre) > 0
				
				Repetir
					Escribir "Ingrese apellidos: "
					Leer apellido
					Si Longitud(apellido) = 0 Entonces
						Escribir "[ERROR] El apellido no puede estar vacío."
					FinSi
				Hasta Que Longitud(apellido) > 0
				
				Repetir
					Escribir "Ingrese fecha (DD-MM-AAAA): "
					Leer fecha
					fechaOk <- ValidarFecha(fecha)
					Si NO fechaOk Entonces
						Escribir "[ERROR] Formato incorrecto. Debe ser DD-MM-AAAA (ej. 12-10-2026)."
					FinSi
				Hasta Que fechaOk
				
				Repetir
					Escribir "Ingrese asunto (ej. TRAMITE DE BECAS SOCIOECONOMICA): "
					Leer asunto
					Si Longitud(asunto) = 0 Entonces
						Escribir "[ERROR] El asunto no puede estar vacío."
					FinSi
				Hasta Que Longitud(asunto) > 0
				
				totalExp <- totalExp + 1
				secuenciaGlobal <- secuenciaGlobal + 1
				
				iniciales <- ExtraerIniciales(asunto)
				numCorrelativo <- FormatearNumero(totalExp)
				codigoGen <- Concatenar("2026-", Concatenar(iniciales, Concatenar("-", numCorrelativo)))
				
				codigos[totalExp] <- codigoGen
				nombres[totalExp] <- nombre
				apellidos[totalExp] <- apellido
				fechar[totalExp] <- fecha
				asuntos[totalExp] <- asunto
				areas[totalExp] <- "Mesa de Partes"
				estados[totalExp] <- "En Tramite"
				resoluciones[totalExp] <- "Pendiente de atencion"
				orden[totalExp] <- secuenciaGlobal
				
				Escribir ""
				Escribir "¡EXPEDIENTE REGISTRADO CON ÉXITO!"
				MostrarFicha(codigoGen, nombre, apellido, fecha, asunto, areas[totalExp], estados[totalExp], resoluciones[totalExp])
				
				Escribir "Presione cualquier tecla para continuar..."
				Esperar Tecla
				
			"2":
				op <- 2
				Borrar Pantalla
				Escribir "=== ATENDER EXPEDIENTES ==="
				Si totalExp = 0 Entonces
					Escribir "No hay expedientes registrados."
				SiNo
					posOk <- Falso
					Repetir
						Escribir "Expedientes registrados:"
						Para i <- 1 Hasta totalExp Hacer
							Escribir "- [", codigos[i], "] | ", nombres[i], " ", apellidos[i], " | Asunto: ", asuntos[i], " (Estado: ", estados[i], ")"
						FinPara
						Escribir ""
						Escribir "Ingrese el CÓDIGO del expediente a atender: "
						Leer codigoIngresado
						codigoIngresado <- Mayusculas(codigoIngresado)
						
						codigoExiste <- Falso
						yaAtendido <- Falso
						posElegida <- 0
						
						Para i <- 1 Hasta totalExp Hacer
							Si Mayusculas(codigos[i]) = codigoIngresado Entonces
								codigoExiste <- Verdadero
								Si estados[i] = "Atendido" Entonces
									yaAtendido <- Verdadero
								SiNo
									Si estados[i] = "En Tramite" O estados[i] = "Pendiente de atencion" Entonces
										posElegida <- i
									FinSi
								FinSi
							FinSi
						FinPara
						
						Si NO codigoExiste Entonces
							Escribir "[ERROR] Código incorrecto. El expediente no existe."
							Escribir ""
						SiNo
							Si yaAtendido Entonces
								Escribir "[ERROR] El expediente ya se encuentra ATENDIDO."
								Escribir ""
							SiNo
								Si posElegida > 0 Entonces
									posOk <- Verdadero
								SiNo
									Escribir "[ERROR] El expediente ya fue derivado o atendido anteriormente."
									Escribir ""
								FinSi
							FinSi
						FinSi
					Hasta Que posOk
					
					Escribir ""
					Escribir "--- DESIGNACIÓN DE ÁREA ---"
					Escribir "Expediente seleccionado: ", codigos[posElegida], " - ", asuntos[posElegida]
					Escribir ""
					
					areaOriginal <- SeleccionarArea(numOpArea1)
					areas[posElegida] <- areaOriginal
					
					Escribir ""
					Repetir
						Escribir "¿El área asignada (", areas[posElegida], ") puede resolver el expediente? (SI/NO): "
						Leer res
						res <- Mayusculas(res)
						Si res <> "SI" Y res <> "NO" Entonces
							Escribir "[ERROR] Respuesta no válida. Debe ingresar SI o NO."
						FinSi
					Hasta Que res = "SI" O res = "NO"
					
					Si res = "SI" Entonces
						Repetir
							Escribir "Ingrese el detalle/forma de resolución: "
							Leer resoluciones[posElegida]
							Si Longitud(resoluciones[posElegida]) = 0 Entonces
								Escribir "[ERROR] Debe especificar la resolución."
							FinSi
						Hasta Que Longitud(resoluciones[posElegida]) > 0
						estados[posElegida] <- "Atendido"
					SiNo
						Escribir ""
						Escribir "El área no pudo resolverlo."
						Repetir
							Escribir "Ingrese el motivo/detalle por el cual se deriva: "
							Leer detalleDerivacion
							Si Longitud(detalleDerivacion) = 0 Entonces
								Escribir "[ERROR] Debe ingresar el motivo de derivación."
							FinSi
						Hasta Que Longitud(detalleDerivacion) > 0
						
						estados[posElegida] <- Concatenar("Derivado (Op. ", Concatenar(ConvertirATexto(numOpArea1), ")"))
						resoluciones[posElegida] <- detalleDerivacion
						
						Escribir ""
						Escribir "=== SELECCIONE LA NUEVA ÁREA PARA DERIVAR ==="
						otraArea <- SeleccionarArea(numOpArea2)
						
						Escribir ""
						Repetir
							Escribir "¿La nueva área (", otraArea, ") puede resolver el expediente ahora mismo? (SI/NO): "
							Leer resOtraArea
							resOtraArea <- Mayusculas(resOtraArea)
							Si resOtraArea <> "SI" Y resOtraArea <> "NO" Entonces
								Escribir "[ERROR] Respuesta no válida. Debe ingresar SI o NO."
							FinSi
						Hasta Que resOtraArea = "SI" O resOtraArea = "NO"
						
						Repetir
							Escribir "Ingrese la resolución final / detalle de atención de la nueva área: "
							Leer resFinal
							Si Longitud(resFinal) = 0 Entonces
								Escribir "[ERROR] Debe ingresar la resolución final."
							FinSi
						Hasta Que Longitud(resFinal) > 0
						
						totalExp <- totalExp + 1
						secuenciaGlobal <- secuenciaGlobal + 1
						
						codigos[totalExp] <- codigos[posElegida]
						nombres[totalExp] <- nombres[posElegida]
						apellidos[totalExp] <- apellidos[posElegida]
						fechar[totalExp] <- fechar[posElegida]
						asuntos[totalExp] <- asuntos[posElegida]
						areas[totalExp] <- otraArea
						
						Si resOtraArea = "SI" Entonces
							estados[totalExp] <- "Atendido"
						SiNo
							estados[totalExp] <- "En Tramite"
						FinSi
						resoluciones[totalExp] <- resFinal
						orden[totalExp] <- secuenciaGlobal
					FinSi
					
					OrdenarExpedientes(codigos, nombres, apellidos, fechar, asuntos, areas, estados, resoluciones, orden, totalExp)
					
					Escribir ""
					Escribir "¡ATENCIÓN/DERIVACIÓN REGISTRADA EXITOSAMENTE!"
				FinSi
				
				Escribir "Presione cualquier tecla para continuar..."
				Esperar Tecla
				
			"3":
				op <- 3
				Borrar Pantalla
				Escribir "=== BUSCAR EXPEDIENTE ==="
				Si totalExp = 0 Entonces
					Escribir "No hay expedientes registrados."
				SiNo
					Repetir
						Escribir "Buscar por:"
						Escribir "1. Código"
						Escribir "2. Fecha"
						Escribir "3. Nombre o Apellido"
						Escribir "Elija opción (1-3): "
						Leer opBuscarStr
						
						Si opBuscarStr <> "1" Y opBuscarStr <> "2" Y opBuscarStr <> "3" Entonces
							Escribir "[ERROR] Opción no válida. Ingrese 1, 2 o 3."
							Escribir ""
						FinSi
					Hasta Que opBuscarStr = "1" O opBuscarStr = "2" O opBuscarStr = "3"
					
					Repetir
						Segun opBuscarStr Hacer
							"1":
								Escribir "Ingrese el CÓDIGO a buscar (ej. 2026-TBC-00001): "
							"2":
								Escribir "Ingrese la FECHA a buscar (DD-MM-AAAA): "
							"3":
								Escribir "Ingrese el NOMBRE o APELLIDO a buscar: "
						FinSegun
						Leer busqueda
						
						Si Longitud(busqueda) = 0 Entonces
							Escribir "[ERROR] El término de búsqueda no puede estar vacío."
							Escribir ""
						FinSi
					Hasta Que Longitud(busqueda) > 0
					
					busqueda <- Mayusculas(busqueda)
					encontrado <- Falso
					
					Para i <- 1 Hasta totalExp Hacer
						Segun opBuscarStr Hacer
							"1":
								Si Mayusculas(codigos[i]) = busqueda Entonces
									MostrarFicha(codigos[i], nombres[i], apellidos[i], fechar[i], asuntos[i], areas[i], estados[i], resoluciones[i])
									encontrado <- Verdadero
								FinSi
							"2":
								Si fechar[i] = busqueda Entonces
									MostrarFicha(codigos[i], nombres[i], apellidos[i], fechar[i], asuntos[i], areas[i], estados[i], resoluciones[i])
									encontrado <- Verdadero
								FinSi
							"3":
								Si Mayusculas(nombres[i]) = busqueda O Mayusculas(apellidos[i]) = busqueda Entonces
									MostrarFicha(codigos[i], nombres[i], apellidos[i], fechar[i], asuntos[i], areas[i], estados[i], resoluciones[i])
									encontrado <- Verdadero
								FinSi
						FinSegun
					FinPara
					
					Si NO encontrado Entonces
						Escribir "No se encontraron expedientes con la información ingresada."
					FinSi
				FinSi
				Escribir "Presione cualquier tecla para continuar..."
				Esperar Tecla
			"4":
				op <- 4
				Borrar Pantalla
				Escribir "=== VISUALIZACIÓN DE EXPEDIENTES ==="
				Si totalExp = 0 Entonces
					Escribir "No hay expedientes registrados para mostrar."
				SiNo
					Escribir "-----------------------------------------------------------------------------------------------"
					Escribir "CÓDIGO          | FECHA      | SOLICITANTE             | ÁREA                   | ESTADO       "
					Escribir "-----------------------------------------------------------------------------------------------"
					Para i <- 1 Hasta totalExp Hacer
						Escribir codigos[i], " | ", fechar[i], " | ", nombres[i], " ", apellidos[i], " | ", areas[i], " | ", estados[i]
					FinPara
					Escribir "-----------------------------------------------------------------------------------------------"
				FinSi
				Escribir "Presione cualquier tecla para continuar..."
				Esperar Tecla
			"5":
				op <- 5
				Escribir "Nos vemos luego. Gracias por usar el sistema."
				Esperar Tecla
			De Otro Modo:
				op <- 0
				Escribir "[ERROR] Opción no válida. Intente de nuevo."
				Esperar Tecla
		FinSegun
	Hasta Que op = 5
FinAlgoritmo