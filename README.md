# Mesa de Partes Digital

Sistema de consola desarrollado en Python para registrar, atender y consultar
expedientes de una institución educativa.

## Funciones

- Registro de solicitantes y generación de códigos correlativos.
- Asignación y derivación de expedientes a las áreas correspondientes.
- Actualización de estados, archivado y reapertura de expedientes.
- Historial de movimientos para consultar el seguimiento de cada expediente.
- Búsqueda por código, fecha, nombre o apellido.
- Visualización de expedientes y generación de un listado de texto.
- Guardado de expedientes en formato JSON entre sesiones.

## Requisitos

Python 3.12 o superior. El proyecto utiliza únicamente la biblioteca estándar de
Python, por lo que no requiere instalar paquetes adicionales.

## Ejecución

Abre una terminal en la carpeta del proyecto y ejecuta:

```powershell
py Sistema_digital.py
```

Si utilizas el comando `python` para iniciar Python:

```sh
python Sistema_digital.py
```

El menú permite registrar, atender, buscar y visualizar expedientes. Selecciona
la opción **5** para salir.

## Archivos del proyecto

- `MESA_DE_PARTES.psc`: pseudocódigo original en PSeInt.
- `Sistema_digital.py`: versión mejorada con persistencia e historial de atención.
- `Mesa_partes.py`: versión inicial del sistema.
- `expedientes.txt/registro.txt`: datos locales de los expedientes en formato JSON.
- `expedientes.txt/listado.txt`: listado de expedientes generado por el sistema.

La carpeta `expedientes.txt` se crea al guardar el primer expediente. Los datos
locales están excluidos del control de versiones mediante `.gitignore`.
