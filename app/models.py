
from flask_appbuilder import Model
from sqlalchemy import (
    Column, Integer, String, Text, Date, DateTime,
    Numeric, ForeignKey, Boolean, CheckConstraint,
    UniqueConstraint
)
from sqlalchemy.orm import relationship


# 1. VEHICULOS
class Vehiculo(Model):
    __tablename__ = "vehiculos"

    vehiculo_id = Column(Integer, primary_key=True)
    placa = Column(String(20), unique=True, nullable=False)
    color = Column(String(40), nullable=False)
    modelo = Column(String(80), nullable=False)
    capacidad = Column(Integer, nullable=False)
    estado = Column(String(30), nullable=False, default="Disponible")

    salidas = relationship("Salida", back_populates="vehiculo")

    def __repr__(self):
        return self.placa


# 2. CONDUCTORES
class Conductor(Model):
    __tablename__ = "conductores"

    conductor_id = Column(Integer, primary_key=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    numero_licencia = Column(String(40), unique=True, nullable=False)
    telefono = Column(String(30))
    estado = Column(String(20), nullable=False, default="Activo")

    salidas = relationship("Salida", back_populates="conductor")

    def __repr__(self):
        return f"{self.nombres} {self.apellidos}"


# 3. PAQUETES
class Paquete(Model):
    __tablename__ = "paquetes"

    paquete_id = Column(Integer, primary_key=True)
    nombre_paquete = Column(String(120), nullable=False)
    duracion_dias = Column(Integer, nullable=False)
    precio_persona = Column(Numeric(10, 2), nullable=False)
    descripcion = Column(Text)

    itinerarios = relationship(
        "Itinerario", back_populates="paquete"
    )
    reservas = relationship("Reserva", back_populates="paquete")
    salidas = relationship("Salida", back_populates="paquete")

    def __repr__(self):
        return self.nombre_paquete


# 4. ITINERARIOS
class Itinerario(Model):
    __tablename__ = "itinerarios"

    itinerario_id = Column(Integer, primary_key=True)
    dia = Column(Integer, nullable=False)
    actividad = Column(String(150), nullable=False)
    lugar = Column(String(150))
    descripcion = Column(Text)

    paquete_id = Column(
        Integer, ForeignKey("paquetes.paquete_id"), nullable=False
    )
    paquete = relationship("Paquete", back_populates="itinerarios")

    def __repr__(self):
        return f"Día {self.dia}: {self.actividad}"


# 5. CLIENTES
class Cliente(Model):
    __tablename__ = "clientes"

    __table_args__ = (
        CheckConstraint(
            "(ci IS NOT NULL AND ci <> '') OR "
            "(pasaporte IS NOT NULL AND pasaporte <> '')",
            name="ck_cliente_documento"
        ),
    )

    cliente_id = Column(Integer, primary_key=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    edad = Column(Integer, nullable=False)
    sexo = Column(String(20), nullable=False)
    nacionalidad = Column(String(60), nullable=False)
    ci = Column(String(30))
    pasaporte = Column(String(40))
    telefono = Column(String(30))
    correo = Column(String(120))

    reservas = relationship("Reserva", back_populates="cliente")
    pasajeros_salidas = relationship(
        "PasajeroSalida", back_populates="cliente"
    )

    def __repr__(self):
        return f"{self.nombres} {self.apellidos}"


# 6. RESERVAS
class Reserva(Model):
    __tablename__ = "reservas"

    reserva_id = Column(Integer, primary_key=True)
    fecha_reserva = Column(Date, nullable=False)
    fecha_salida = Column(Date, nullable=False)
    cantidad_personas = Column(Integer, nullable=False, default=1)
    estado = Column(String(30), nullable=False, default="Pendiente")

    cliente_id = Column(
        Integer, ForeignKey("clientes.cliente_id"), nullable=False
    )
    paquete_id = Column(
        Integer, ForeignKey("paquetes.paquete_id"), nullable=False
    )

    cliente = relationship("Cliente", back_populates="reservas")
    paquete = relationship("Paquete", back_populates="reservas")
    pagos = relationship("Pago", back_populates="reserva")

    def __repr__(self):
        return (
        f"Reserva {self.reserva_id} - "
        f"{self.cliente} - {self.paquete}"
    )


# 7. SALIDAS
class Salida(Model):
    __tablename__ = "salidas"

    salida_id = Column(Integer, primary_key=True)
    fecha_inicio = Column(Date, nullable=False)
    hora_salida = Column(String(5))
    hora_llegada = Column(String(5))
    destino = Column(String(150), nullable=False)
    observaciones = Column(Text)

    conductor_id = Column(
        Integer, ForeignKey("conductores.conductor_id"), nullable=False
    )
    vehiculo_id = Column(
        Integer, ForeignKey("vehiculos.vehiculo_id"), nullable=False
    )
    paquete_id = Column(
        Integer, ForeignKey("paquetes.paquete_id"), nullable=False
    )

    conductor = relationship("Conductor", back_populates="salidas")
    vehiculo = relationship("Vehiculo", back_populates="salidas")
    paquete = relationship("Paquete", back_populates="salidas")
    pasajeros = relationship(
        "PasajeroSalida",
        back_populates="salida",
        cascade="all, delete-orphan"
    )

    @property
    def total_personas(self):
        return len(self.pasajeros)

    def __repr__(self):
         return (
        f"Salida {self.salida_id} - "
        f"{self.fecha_inicio} - {self.destino}"
    )


# 8. PASAJEROS DE CADA SALIDA
class PasajeroSalida(Model):
    __tablename__ = "pasajeros_salidas"

    __table_args__ = (
        UniqueConstraint(
            "salida_id", "cliente_id",
            name="uq_pasajero_salida"
        ),
    )

    pasajero_salida_id = Column(Integer, primary_key=True)
    destino_individual = Column(String(150))
    observaciones = Column(Text)

    salida_id = Column(
        Integer, ForeignKey("salidas.salida_id"), nullable=False
    )
    cliente_id = Column(
        Integer, ForeignKey("clientes.cliente_id"), nullable=False
    )

    salida = relationship("Salida", back_populates="pasajeros")
    cliente = relationship("Cliente", back_populates="pasajeros_salidas")

def __repr__(self):
    return f"{self.cliente} - {self.salida}"

# 9. PAGOS
class Pago(Model):
    __tablename__ = "pagos"

    pago_id = Column(Integer, primary_key=True)
    monto_pagado = Column(Numeric(10, 2), nullable=False)
    fecha_pago = Column(DateTime, nullable=False)
    metodo_pago = Column(String(30), nullable=False)

    reserva_id = Column(
        Integer, ForeignKey("reservas.reserva_id"), nullable=False
    )
    reserva = relationship("Reserva", back_populates="pagos")

    def __repr__(self):
        return f"Pago {self.pago_id}"
