from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route("/")
def main():
    return "main"

@app.route("/base")
def base():
    return render_template("base.html")


#nuestros endpoints
@app.route("/catalogo-main")
def catalogoMain():
    return render_template("catalogo_main.html")

@app.route("/catalogo-form")
def catalogoForm():
    return render_template("catalogo_form.html")

@app.route("/cliente-main")
def clienteMain():
    return render_template("cliente_main.html")

@app.route("/cliente-form")
def clienteForm():
    return render_template("cliente_form.html")

@app.route("/contrato-main")
def contratoMain():
    return render_template("contrato_main.html")

@app.route("/contrato-form")
def contratoForm():
    return render_template("contrato_form.html")

@app.route("/empleado-main")
def empleadoMain():
    return render_template("empleado_main.html")

@app.route("/empleado-form")
def empleadoForm():
    return render_template("empleado_form.html")

@app.route("/nomina-main")
def nominaMain():
    return render_template("nomina_main.html")

@app.route("/nomina-form")
def nominaForm():
    return render_template("nomina_form.html")

@app.route("/proveedor-main")
def proveedorMain():
    return render_template("proveedor_main.html")

@app.route("/proveedor-form")
def proveedorForm():
    return render_template("proveedor_form.html")

@app.route("/servicio-main")
def servicioMain():
    return render_template("servicio_main.html")

@app.route("/servicio-form")
def servicioForm():
    return render_template("servicio_form.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500, debug=True)
    pass
