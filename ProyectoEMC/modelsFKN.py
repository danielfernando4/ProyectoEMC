from app import db
from sqlalchemy import Column, CHAR, String, Integer, DateTime, Numeric, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


# Tabla CLIENTE   
class Cliente(db.Model):
    __tablename__ = 'CLIENTE'

    id_cliente =    db.Column(db.CHAR(7), primary_key=True, nullable=False)
    nombre_cl =     db.Column(db.CHAR(40), nullable=False)
    apellido_cl =   db.Column(db.CHAR(40), nullable=False)
    correo_cl =     db.Column(db.CHAR(60), nullable=False)
    telefono_cl =   db.Column(db.CHAR(10), nullable=False)
    direccion_cl =  db.Column(db.CHAR(40), nullable=False)
    
    def __repr__(self):
        return f'Cliente {self.nombre_cl} con apellido {self.apellido_cl}'

# Tabla CONTRATO_DE_EVENTO
class ContratoEvento(db.Model):
    __tablename__ = 'CONTRATO_DE_EVENTO'

    id_contrato = Column(CHAR(7), primary_key=True, nullable=False)
    id_evento = Column(CHAR(6), ForeignKey('EVENTO.ID_EVENTO'), nullable=False)
    id_empleado = Column(CHAR(6), ForeignKey('EMPLEADO.ID_EMPLEADO'), nullable=False)
    id_cliente = Column(CHAR(7), ForeignKey('CLIENTE.ID_CLIENTE'), nullable=False)
    id_servicio = Column(CHAR(7), ForeignKey('SERVICIO_PROVEEDOR.ID_SERVICIO'), nullable=False)
    fecha_inicio = Column(DateTime, nullable=False)
    fecha_fin = Column(DateTime, nullable=False)
    presupuesto = Column(Numeric(10, 2), nullable=False)
    lugar = Column(CHAR(50), nullable=False)
    estado_contrato = Column(CHAR(10), nullable=False)

# Tabla EMPLEADO
class Empleado(db.Model):
    __tablename__ = 'EMPLEADO'

    id_empleado = Column(CHAR(6), primary_key=True, nullable=False)
    id_oficina = Column(CHAR(2), ForeignKey('OFICINA.ID_OFICINA'), nullable=False)
    nombre_emp = Column(CHAR(40), nullable=False)
    apellido_emp = Column(CHAR(40), nullable=False)
    cargo_emp = Column(CHAR(30), nullable=False)
    correo_emp = Column(CHAR(100), nullable=False)
    telefono_emp = Column(CHAR(10), nullable=False)
    salario = Column(Numeric(10, 2), nullable=False)
    fecha_contratacion = Column(Date, nullable=False)

# Tabla EVENTO
class Evento(db.Model):
    __tablename__ = 'EVENTO'

    id_evento = Column(CHAR(6), primary_key=True, nullable=False)
    id_oficina = Column(CHAR(2), ForeignKey('OFICINA.ID_OFICINA'), nullable=False)
    tipo_evento = Column(CHAR(40), nullable=False)
    costo_referencial = Column(Numeric(10, 2), nullable=False)

# Tabla OFICINA
class Oficina(db.Model):
    __tablename__ = 'OFICINA'

    id_oficina = Column(CHAR(2), primary_key=True, nullable=False)
    nombre_of = Column(CHAR(25), nullable=False)
    ubicacion = Column(CHAR(50), nullable=False)

# Tabla PROVEEDOR
class Proveedor(db.Model):
    __tablename__ = 'PROVEEDOR'

    id_proveedor = Column(CHAR(7), primary_key=True, nullable=False)
    id_oficina = Column(CHAR(2), ForeignKey('OFICINA.ID_OFICINA'), nullable=False)
    nombre_pro = Column(CHAR(50), nullable=False)
    especialidad_pro = Column(CHAR(30), nullable=False)

# Tabla SERVICIO_PROVEEDOR
class ServicioProveedor(db.Model):
    __tablename__ = 'SERVICIO_PROVEEDOR'

    id_servicio = Column(CHAR(7), primary_key=True, nullable=False)
    id_proveedor = Column(CHAR(7), ForeignKey('PROVEEDOR.ID_PROVEEDOR'), nullable=False)
    descripcion_ser = Column(CHAR(40), nullable=False)
    precio_ser = Column(Numeric(10, 2), nullable=False)
