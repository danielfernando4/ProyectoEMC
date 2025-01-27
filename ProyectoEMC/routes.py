from flask import render_template, request, redirect, url_for
from modelsFKN import Cliente, ContratoEvento, Empleado, Evento, Oficina, Proveedor, ServicioProveedor
from db import *

def rutas(app, db):
    @app.route("/")
    def main():
        return f"Error al agregar: dato", 500


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
        servicioDAC = ServicioProveedorDAC()
        if request.method == 'GET':
            servicios = servicioDAC.getAll()
            return render_template("servicio_main.html", servicios = servicios)
        
        accion = request.form.get('accion')
        id = request.form.get('id')
        
        if accion == "buscar":
             servicios = servicioDAC.getById(id)
             return render_template("servicio_main.html", servicios = servicios)
         
        if accion == "eliminar":
            servicioDAC.delete(id)
        else:                    
            servicio = {
                    'id_servicio': request.form.get('id_servicio'),
                    'id_oficina': request.form.get('id_oficina'),
                    'id_proveedor': request.form.get('id_proveedor'),
                    'descripcion_ser': request.form.get('descripcion_ser'),
                    'precio_ser': float(request.form.get('precio_ser'))
            }

            if accion == "agregar":
                servicioDAC.add(servicio)
            elif accion == "actualizar":
                servicioDAC.update(id, servicio) 
                
        servicios = servicioDAC.getAll()
        return render_template("servicio_main.html", servicios = servicios)

    @app.route("/servicio-form", methods = ['POST', 'GET'])
    def servicioForm():
        servicioDAC = ServicioProveedorDAC()
        if request.method == 'POST':
            servicio = servicioDAC.getById(request.form.get('id_servicio'))
            return render_template("servicio_form.html", servicio = servicio, accion = "actualizar")
        
        return render_template("servicio_form.html", servicio = None, accion = "agregar")
    