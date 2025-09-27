from registros_ig import app
from flask import render_template, request, redirect
from registros_ig.models import *
from datetime import date

def validarFormulario(datosFormulario):
    errores = [] #Se crea la lista para guardar errores
    hoy = str(date.today())
    if datosFormulario['date'] > hoy:
        errores.append("La fecha no puede ser mayor a la actual")
    if datosFormulario['concept'] == "":
        errores.append("El concepto no puede ir vacío")
    if datosFormulario['quantity'] == "" or float(datosFormulario['quantity']) == 0.0:
        errores.append("El monto debe ser distinto de 0 y de vacío")
    return errores

@app.route("/")
def index():
    diccionario = selectAll()
    return render_template("index.html",lista=diccionario)

@app.route("/new", methods=["GET","POST"])
def create():
    if request.method == "GET": #GET
        return render_template("create.html", dataForm={})
    else: #POST
        errores = validarFormulario(request.form)
        if errores:
            return render_template("create.html", errors=errores,dataForm=request.form)
        insert([ request.form['date'], request.form['concept'], request.form['quantity'] ])

        return redirect("/")
    
@app.route("/delete/<int:id>", methods=["GET","POST"])
def remove(id):
    if request.method == "GET":
        resultado = selectBy(id)
        return render_template("delete.html", data=resultado)
    else: #POST
        return f"registro para eliminar con id: {id}"
    
@app.route("/update/<int:id>", methods=["GET","POST"])
def update(id):
    if request.method == "GET":
        resultado = selectBy(id)
        return render_template("update.html", datos=resultado)
    else: #POST
        return f"registro para actualizar con id: {id}"