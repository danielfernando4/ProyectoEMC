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
    @app.route("/catalogo-main", methods = ['POST', 'GET'])
    def catalogoMain():
        eventoDAC = EventoDAC()
        if request.method == 'GET':
            eventos = eventoDAC.getAll()
            return render_template("catalogo_main.html", eventos = eventos)
        
        accion = request.form.get('accion')
        id = request.form.get('id')
        print(accion)
        print(id)
        if accion == "buscar":
             eventos = eventoDAC.getById(id) if id else eventoDAC.getAll()
             return render_template("catalogo_main.html", eventos = eventos)         
        
        if accion == "eliminar":
            eventoDAC.delete(id)
        else:                    
            evento = {
                'id_evento': request.form.get('id_evento'),
                'id_oficina': request.form.get('id_oficina'),
                'tipo_evento': request.form.get('tipo_evento'),
                'costo_referencial': float(request.form.get('costo_referencial'))
            }

            if accion == "agregar":
                eventoDAC.add(evento)
            elif accion == "actualizar":
                eventoDAC.update(evento) 
                
        eventos = eventoDAC.getAll()
        return render_template("catalogo_main.html", eventos = eventos)

    @app.route("/catalogo-form", methods = ['POST', 'GET'])
    def catalogoForm():
        eventoDAC = EventoDAC()
        if request.method == 'POST':
            evento = eventoDAC.getById(request.form.get('id_evento'))[0]
            return render_template("catalogo_form.html", evento = evento, accion = "actualizar")
        
        return render_template("catalogo_form.html", evento = None, accion = "agregar")
    
    @app.route("/cliente-main", methods = ['POST', 'GET'])
    def clienteMain():
        clienteDAC = ClienteDAC()
        if request.method == 'GET':
            clientes = clienteDAC.getAll()
            return render_template("cliente_main.html", clientes = clientes)
        
        accion = request.form.get('accion')
        id = request.form.get('id')
        print(accion)
        print(id)
        if accion == "buscar":
             clientes = clienteDAC.getById(id) if id else clienteDAC.getAll()
             return render_template("cliente_main.html", clientes = clientes)         
        
        if accion == "eliminar":
            clienteDAC.delete(id)
        else:                    
            cliente = {
                'id_cliente': request.form.get('id_cliente'),
                'nombre_cl': request.form.get('nombre_cl'),
                'apellido_cl': request.form.get('apellido_cl'),
                'correo_cl': request.form.get('correo_cl'),
                'telefono_cl': request.form.get('telefono_cl'),
                'direccion_cl': request.form.get('direccion_cl')
            }

            if accion == "agregar":
                clienteDAC.add(cliente)
            elif accion == "actualizar":
                clienteDAC.update(cliente) 
                
        clientes = clienteDAC.getAll()
        return render_template("cliente_main.html", clientes = clientes)

    @app.route("/cliente-form", methods = ['POST', 'GET'])
    def clienteForm():
        clienteDAC = ClienteDAC()
        if request.method == 'POST':
            cliente = clienteDAC.getById(request.form.get('id_cliente'))[0]
            return render_template("cliente_form.html", cliente = cliente, accion = "actualizar")
        
        return render_template("cliente_form.html", cliente = None, accion = "agregar")
    
    @app.route("/contrato-main", methods = ['POST', 'GET'])
    def contratoMain():
        return render_template("contrato_main.html")

    @app.route("/contrato-form", methods = ['POST', 'GET'])
    def contratoForm():
        return render_template("contrato_form.html")

    @app.route("/empleado-main", methods = ['POST', 'GET'])
    def empleadoMain():
        return render_template("empleado_main.html")

    @app.route("/empleado-form", methods = ['POST', 'GET'])
    def empleadoForm():
        return render_template("empleado_form.html")

    @app.route("/nomina-main", methods = ['POST', 'GET'])
    def nominaMain():
        return render_template("nomina_main.html")

    @app.route("/nomina-form", methods = ['POST', 'GET'])
    def nominaForm():
        return render_template("nomina_form.html")

    @app.route("/proveedor-main", methods = ['POST', 'GET'])
    def proveedorMain():
        return render_template("proveedor_main.html")

    @app.route("/proveedor-form", methods = ['POST', 'GET'])
    def proveedorForm():
        return render_template("proveedor_form.html")
    
    @app.route("/oficina-main", methods = ['POST', 'GET'])
    def oficinaMain():
        return render_template("oficina_main.html")

    @app.route("/oficina-form", methods = ['POST', 'GET'])
    def oficinaForm():
        return render_template("oficina_form.html")
    
    @app.route("/servicio-main", methods = ['POST', 'GET'])
    def servicioMain():
        servicioDAC = ServicioProveedorDAC()
        if request.method == 'GET':
            servicios = servicioDAC.getAll()
            return render_template("servicio_main.html", servicios = servicios)
        
        accion = request.form.get('accion')
        id = request.form.get('id')
        print(accion)
        print(id)
        if accion == "buscar":
             servicios = servicioDAC.getById(id) if id else servicioDAC.getAll()
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
                servicioDAC.update(servicio) 
                
        servicios = servicioDAC.getAll()
        return render_template("servicio_main.html", servicios = servicios)

    @app.route("/servicio-form", methods = ['POST', 'GET'])
    def servicioForm():
        servicioDAC = ServicioProveedorDAC()
        if request.method == 'POST':
            servicio = servicioDAC.getById(request.form.get('id_servicio'))[0]
            return render_template("servicio_form.html", servicio = servicio, accion = "actualizar")
        
        return render_template("servicio_form.html", servicio = None, accion = "agregar")
    