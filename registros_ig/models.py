import sqlite3

def selectAll():
    conexion = sqlite3.connect("data/movimientos.sqlite")
    cur = conexion.cursor()
    res = cur.execute("SELECT * from movement;")
    filas = res.fetchall() #datos de columnas (2025-09-01, Nomina, 1800),(2025-09-05, Mercado, -100)
    columnas = res.description #nombre de columnas en las primeras filas (id,000),(date,000)

    lista_diccionario = []

    for f in filas:
        posicion = 0
        diccionario = {}
        for c in columnas:
            diccionario[c[0]] = f[posicion]
            posicion+=1
        lista_diccionario.append(diccionario)
    conexion.close()
    return lista_diccionario

def insert(registroForm):
    conexion = sqlite3.connect("data/movimientos.sqlite")
    cur = conexion.cursor()
    res = cur.execute("INSERT INTO movement(date, concept, quantity) VALUES(?,?,?);", registroForm)
    conexion.commit() #funcion para validar el registro antes de guardar

    conexion.close()