from registros_ig.conexion import Conexion

def selectAll():
    conect = Conexion("SELECT * from movement;")
    filas = conect.res.fetchall() #datos de columnas (2025-09-01, Nomina, 1800),(2025-09-05, Mercado, -100)
    columnas = conect.res.description #nombre de columnas en las primeras filas (id,000),(date,000)

    lista_diccionario = []

    for f in filas:
        posicion = 0
        diccionario = {}
        for c in columnas:
            diccionario[c[0]] = f[posicion]
            posicion+=1
        lista_diccionario.append(diccionario)
    conect.con.close()
    return lista_diccionario

def insert(registroForm):
    conectInsert = Conexion("INSERT INTO movement(date, concept, quantity) VALUES(?,?,?);", registroForm)
    conectInsert.con.commit() #funcion para validar el registro antes de guardar
    conectInsert.con.close()

def selectBy(id):
    conectSelectBy = Conexion(f"SELECT * FROM movement WHERE id={id};")
    result = conectSelectBy.res.fetchall()
    conectSelectBy.con.close()
    return result[0]

def deleteBy(id):
    conectDelete = Conexion(f"DELETE FROM movement WHERE id={id};")
    conectDelete.con.commit() #funcion para validar borrado
    conectDelete.con.close()