from flask import render_template, request, redirect, url_for, session
from db import * 


import idoficina


def rutas(app):


    app.secret_key = "clave_secreta" 


   

    @app.before_request
    def validar_sesion():
        rutas_protegidas = ["/catalogo-main", "/catalogo-form", "/cliente-main", "/cliente-form", 
                            "/contrato-main", "/contrato-form", "/empleado-main", "/empleado-form", "/nomina-main"]
        if request.path in rutas_protegidas and "oficina" not in session:
            return redirect(url_for("inicio"))
        
    @app.context_processor
    def inject_variables():
        return dict(modo=session.get("oficina", None))  # Esto puede cambiar dinámicamente

    @app.route("/", methods=['GET', 'POST'])
    def inicio():
        if request.method == 'POST':
            oficina = request.form.get("oficina")
            session["oficina"] = oficina  
            idoficina.id_oficina = session["oficina"]
            print(f"Oficina seleccionada: {session['oficina']}")  
            return redirect(url_for("catalogoMain"))  

        return render_template("inicio.html")
    

    @app.route("/logout")
    def logout():
        session.clear()  # Elimina todos los datos de sesión
        return redirect(url_for("inicio"))  # Redirige a la página de inicio




    @app.route("/base")
    def base():
        return render_template("base.html")


    # #nuestros endpoints
    # @app.route("/catalogo-main", methods = ['POST', 'GET'])
    # def catalogoMain():
    #     eventoDAC = EventoDAC()
    #     if request.method == 'GET':
    #         eventos = eventoDAC.getAll()
    #         return render_template("catalogo_main.html", eventos = eventos)
        
    #     accion = request.form.get('accion')
    #     id = request.form.get('id')
        
    #     if accion == "consultar_oficinas":
    #         eventos = eventoDAC.getAllOffices()
    #         return render_template("catalogo_main.html", eventos = eventos)           
        
    #     if accion == "eliminar":
    #         eventoDAC.delete(id)
    #     else:                    
    #         evento = {
    #             'id_evento': request.form.get('id_evento'),
    #             'id_oficina': request.form.get('id_oficina'),
    #             'tipo_evento': request.form.get('tipo_evento'),
    #             'costo_referencial': float(request.form.get('costo_referencial'))
    #         }

    #         if accion == "agregar":
    #             eventoDAC.add(evento)
    #         elif accion == "actualizar":
    #             eventoDAC.update(evento) 
                
    #     eventos = eventoDAC.getAll()
    #     return render_template("catalogo_main.html", eventos = eventos)
    @app.route("/catalogo-main", methods=['POST', 'GET'])
    def catalogoMain():
        eventoDAC = EventoDAC()
        selected_radio = "locales"  # Valor por defecto

        if request.method == 'GET':
            eventos = eventoDAC.getAll()
            return render_template("catalogo_main.html", eventos=eventos, selected_radio=selected_radio)

        accion = request.form.get('accion')
        selected_radio = request.form.get('radio', "locales")  # Obtener valor del radio button

        if accion == "consultar_oficinas":
            eventos = eventoDAC.getAllOffices()
            return render_template("catalogo_main.html", eventos=eventos, selected_radio=selected_radio)

        id = request.form.get('id')

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
        return render_template("catalogo_main.html", eventos=eventos, selected_radio=selected_radio)


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
        selected_radio = "locales"
        contratoDAC = ContratoEventoDAC()
        if request.method == 'GET':
            contratos = contratoDAC.getAll()
            return render_template("contrato_main.html", contratos = contratos)
        
        accion = request.form.get('accion')
        id = request.form.get('id')
        
        if accion == "buscar":
             contratos = contratoDAC.getById(id) if id else contratoDAC.getAll()
             return render_template("contrato_main.html", contratos = contratos)         
        
        if accion == "eliminar":
            contratoDAC.delete(id)



        if accion == "consultar_oficinas":
            contratos = contratoDAC.getAllOffices()
            return render_template("contrato_main.html", contratos=contratos, selected_radio=selected_radio)
        else:                    
            contrato = {
                'id_contrato': request.form.get('id_contrato'),
                'id_oficina': request.form.get('id_oficina'),
                'id_evento': request.form.get('id_evento'),
                'id_empleado': request.form.get('id_empleado'),
                'id_cliente': request.form.get('id_cliente'),
                'id_servicio': request.form.get('id_servicio'),
                'fecha_inicio': request.form.get('fecha_inicio'),
                'fecha_fin': request.form.get('fecha_fin'),
                'presupuesto': float(request.form.get('presupuesto')),
                'lugar': request.form.get('lugar'),
                'estado_contrato': request.form.get('estado_contrato'),
            }

            print(contrato)

            if accion == "agregar":
                contratoDAC.add(contrato)
            elif accion == "actualizar":
                contratoDAC.update(contrato) 
                
        contratos = contratoDAC.getAll()
        return render_template("contrato_main.html", contratos = contratos)

    @app.route("/contrato-form", methods = ['POST', 'GET'])
    def contratoForm():
        contratoDAC = ContratoEventoDAC()
        if request.method == 'POST':
            contrato = contratoDAC.getById(request.form.get('id_contrato'))[0]
            return render_template("contrato_form.html", contrato = contrato, accion = "actualizar")
        
        return render_template("contrato_form.html", contrato = None, accion = "agregar")

    @app.route("/empleado-main", methods = ['POST', 'GET'])
    def empleadoMain():
        selected_radio = "locales"  # Valor por defecto
        empleadoDAC = EmpleadoDAC()
        if request.method == 'GET':
            empleados = empleadoDAC.getAll()
            return render_template("empleado_main.html", empleados = empleados)
        
        accion = request.form.get('accion')
        id = request.form.get('id')
        
        if accion == "buscar":
             empleados = empleadoDAC.getById(id) if id else empleadoDAC.getAll()
             return render_template("empleado_main.html", empleados = empleados)         
        
        if accion == "eliminar":
            empleadoDAC.delete(id)


        if accion == "consultar_oficinas":
            empleados = empleadoDAC.getAllOffices()
            return render_template("empleado_main.html", empleados=empleados, selected_radio=selected_radio)
        else:                    
            empleado = {
                'id_empleado': request.form.get('id_empleado'),
                'id_oficina': request.form.get('id_oficina'),
                'nombre_emp': request.form.get('nombre_emp'),
                'apellido_emp': request.form.get('apellido_emp'),
                'cargo_emp': request.form.get('cargo_emp'),
                'telefono_emp': request.form.get('telefono_emp'),
                'correo_emp': request.form.get('correo_emp'),
            }

            print(empleado)
            if accion == "agregar":
                empleadoDAC.add(empleado)
            elif accion == "actualizar":
                empleadoDAC.update(empleado) 
                
        empleados = empleadoDAC.getAll()
        return render_template("empleado_main.html", empleados = empleados)

    @app.route("/empleado-form", methods = ['POST', 'GET'])
    def empleadoForm():
        empleadoDAC = EmpleadoDAC()
        if request.method == 'POST':
            empleado = empleadoDAC.getById(request.form.get('id_empleado'))[0]
            return render_template("empleado_form.html", empleado = empleado, accion = "actualizar")
        
        return render_template("empleado_form.html", empleado = None, accion = "agregar")

    @app.route("/nomina-main", methods = ['POST', 'GET'])
    def nominaMain():
        nominaDAC = NominaDAC()
        if request.method == 'GET':
            empleados = nominaDAC.getAll()
            return render_template("nomina_main.html", empleados = empleados)
        
        accion = request.form.get('accion')
        id = request.form.get('id')
        
        if accion == "buscar":
             empleados = nominaDAC.getById(id) if id else nominaDAC.getAll()
             return render_template("nomina_main.html", empleados = empleados)         
        
        if accion == "eliminar":
            nominaDAC.delete(id)
        else:                    
            empleado = {
                'id_empleado': request.form.get('id_empleado'),
                'salario': float(request.form.get('salario')),
                'fecha_contratacion': request.form.get('fecha_contratacion')
            }

            if accion == "agregar":
                nominaDAC.add(empleado)
            elif accion == "actualizar":
                nominaDAC.update(empleado) 
                
        empleados = nominaDAC.getAll()
        return render_template("nomina_main.html", empleados = empleados)

    @app.route("/nomina-form", methods = ['POST', 'GET'])
    def nominaForm():
        nominaDAC = NominaDAC()
        if request.method == 'POST':
            empleado = nominaDAC.getById(request.form.get('id_empleado'))[0]
            return render_template("nomina_form.html", empleado = empleado, accion = "actualizar")
        
        return render_template("nomina_form.html", empleado = None, accion = "agregar")

    @app.route("/proveedor-main", methods = ['POST', 'GET'])
    def proveedorMain():
        selected_radio = "locales"  # Valor por defecto
        proveedorDAC = ProveedorDAC()
        if request.method == 'GET':
            proveedores = proveedorDAC.getAll()
            return render_template("proveedor_main.html", proveedores = proveedores)
        
        accion = request.form.get('accion')
        id = request.form.get('id')
        
        if accion == "buscar":
             proveedores = proveedorDAC.getById(id) if id else proveedorDAC.getAll()
             return render_template("proveedor_main.html", proveedores = proveedores)         
        
        if accion == "consultar_oficinas":
            proveedores = proveedorDAC.getAllOffices()
            return render_template("proveedor_main.html", proveedores=proveedores, selected_radio=selected_radio)
        
        if accion == "eliminar":
            proveedorDAC.delete(id)
        
        else:                    
            proveedor = {
                'id_proveedor': request.form.get('id_proveedor'),
                'id_oficina': request.form.get('id_oficina'),
                'nombre_pro': request.form.get('nombre_pro'),
                'especialidad_pro': request.form.get('especialidad_pro')
            }
            
            print(proveedor)

            if accion == "agregar":
                proveedorDAC.add(proveedor)
            elif accion == "actualizar":
                proveedorDAC.update(proveedor) 
                
        proveedores = proveedorDAC.getAll()
        return render_template("proveedor_main.html", proveedores = proveedores)

    @app.route("/proveedor-form", methods = ['POST', 'GET'])
    def proveedorForm():
        proveedorDAC = ProveedorDAC()
        if request.method == 'POST':
            proveedor = proveedorDAC.getById(request.form.get('id_proveedor'))[0]
            return render_template("proveedor_form.html", proveedor = proveedor, accion = "actualizar")
        
        return render_template("proveedor_form.html", proveedor = None, accion = "agregar")
    
    @app.route("/oficina-main", methods = ['POST', 'GET'])
    def oficinaMain():
        oficinaDAC = OficinaDAC()
        if request.method == 'GET':
            oficinas = oficinaDAC.getAll()
            return render_template("oficina_main.html", oficinas = oficinas)
        
        accion = request.form.get('accion')
        id = request.form.get('id')
        
        if accion == "buscar":
             oficinas = oficinaDAC.getById(id) if id else oficinaDAC.getAll()
             return render_template("oficina_main.html", oficinas = oficinas)         
        
        if accion == "eliminar":
            oficinaDAC.delete(id)
        else:                    
            oficina = {
                'id_oficina': request.form.get('id_oficina'),
                'nombre_of': request.form.get('nombre_of'),
                'ubicacion': request.form.get('ubicacion'),
            }

            if accion == "agregar":
                oficinaDAC.add(oficina)
            elif accion == "actualizar":
                oficinaDAC.update(oficina) 
                
        oficinas = oficinaDAC.getAll()
        return render_template("oficina_main.html", oficinas = oficinas)

    @app.route("/oficina-form", methods = ['POST', 'GET'])
    def oficinaForm():
        oficinaDAC = OficinaDAC()
        if request.method == 'POST':
            print('hola ' + request.form.get('id_oficina'))
            oficina = oficinaDAC.getById(request.form.get('id_oficina'))[0]
            return render_template("oficina_form.html", oficina = oficina, accion = "actualizar")
        
        return render_template("oficina_form.html", oficina = None, accion = "agregar")
    
    @app.route("/servicio-main", methods = ['POST', 'GET'])
    def servicioMain():
        selected_radio = "locales"
        servicioDAC = ServicioProveedorDAC()
        if request.method == 'GET':
            servicios = servicioDAC.getAll()
            return render_template("servicio_main.html", servicios = servicios)
        
        accion = request.form.get('accion')
        id = request.form.get('id')
        
        if accion == "buscar":
             servicios = servicioDAC.getById(id) if id else servicioDAC.getAll()
             return render_template("servicio_main.html", servicios = servicios)         
        
        if accion == "eliminar":
            servicioDAC.delete(id)


        if accion == "consultar_oficinas":
            servicios = servicioDAC.getAllOffices()
            print(servicios)
            return render_template("servicio_main.html", servicios=servicios, selected_radio=selected_radio)
        
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
    