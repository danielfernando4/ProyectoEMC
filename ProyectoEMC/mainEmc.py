from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route("/")
def main():
    return "main"

@app.route("/example")
def example():
    return render_template("example.html")

@app.route("/base")
def base():
    return render_template("base.html")


#nuestros endpoints
@app.route("/catalogoEvento")
def catalogoEvento():
    return render_template("catalogEventos.html")

@app.route("/contratoEvento")
def contratoEvento():
    return render_template("contratoEventos.html")

@app.route("/cliente")
def cliente():
    return render_template("clientes.html")

@app.route("/proveedor")
def proveedor():
    return render_template("proovedores.html")

@app.route("/servicio")
def servicio():
    return render_template("servicios.html")

@app.route("/empleado")
def empleado():
    return render_template("empleados.html")




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500, debug=True)
    pass
