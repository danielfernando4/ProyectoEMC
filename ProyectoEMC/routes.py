from flask import render_template, request, redirect, url_for
from modelsFKN import Cliente, ContratoEvento, Empleado, Evento, Oficina, Proveedor, ServicioProveedor

def rutas(app, db):
    @app.route("/")
    def main():
        servicioF = ServicioProveedor.query.all()
        return str(servicioF)


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
    
    @app.route("/servicio-main", methods = ['POST', 'GET'])
    def servicioMain():
        if request.method == 'GET':
            servicios = ServicioProveedor.query.all()
            return render_template("servicio_main.html", servicios = servicios)
        
        id_servicio = request.form.get('id_servicio')
        # id_oficina  = request.form.get('id_oficina')
        id_proveedor = request.form.get('id_proveedor')
        descripcion_ser = request.form.get('descripcion_ser')
        precio_ser  = float(request.form.get('precio_ser'))
        print(id_proveedor)
        servicio = ServicioProveedor(id_servicio = id_servicio, id_proveedor = id_proveedor, descripcion_ser = descripcion_ser, precio_ser = precio_ser)
        db.session.add(servicio)
        db.session.commit()
        
        servicios = ServicioProveedor.query.all()
        return render_template("servicio_main.html", servicios = servicios)

    @app.route("/servicio-form/<id_servicio>", methods = ['POST', 'GET'])
    def servicioForm(id_servicio):
        if request.method == 'POST':
            servicio = ServicioProveedor.query.filter(ServicioProveedor.id_servicio == id_servicio).first()
            return render_template("servicio_form.html", servicio = servicio)
        
        return render_template("servicio_form.html", servicio = None)
    
    @app.route("/eliminar/<model>/<page>", methods = ['POST', 'GET'])
    def eliminar(model, page):
        return redirect(url_for(page))