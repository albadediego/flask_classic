from registros_ig import app
from flask import render_template, request, redirect, flash
from registros_ig.models import *
from datetime import date, datetime
from registros_ig.forms import MovementsForm

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
    form = MovementsForm()
    if request.method == "GET": #GET
        return render_template("create.html", dataForm=form)
    else: #POST
        if form.validate_on_submit():
            insert([ request.form['date'], request.form['concept'], request.form['quantity'] ])
            flash("Movimiento registrado correctamente")
            return redirect("/")
        else:
            return render_template("create.html",dataForm=form)
    
@app.route("/delete/<int:id>", methods=["GET","POST"])
def remove(id):
    if request.method == "GET":
        resultado = selectBy(id)
        return render_template("delete.html", data=resultado)
    else: #POST
        deleteBy(id)
        flash("Movimiento eliminado correctamente")
        return redirect("/")
    
@app.route("/update/<int:id>", methods=["GET","POST"])
def update(id):
    form = MovementsForm()
    if request.method == "GET":
        resultado = selectBy(id)
        form.date.data=datetime.strptime(resultado[1], "%Y-%M-%d")
        form.concept.data=resultado[2]
        form.quantity.data=resultado[3]
        return render_template("update.html", dataForm=form)
    else: #POST
        return f"registro para actualizar con id: {id}"