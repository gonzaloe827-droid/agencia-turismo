
from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface

from .extensions import appbuilder
from .models import (
    Vehiculo,
    Conductor,
    Paquete,
    Itinerario,
    Cliente,
    Reserva,
    Salida,
    PasajeroSalida,
    Pago,
)


# 1. VEHICULOS
class VehiculoView(ModelView):
    datamodel = SQLAInterface(Vehiculo)

    list_columns = [
        "placa",
        "modelo",
        "color",
        "capacidad",
        "estado",
    ]

    search_columns = ["placa", "modelo", "color"]

    add_columns = [
        "placa",
        "color",
        "modelo",
        "capacidad",
        "estado",
    ]

    edit_columns = add_columns

    form_choices = {
        "estado": [
            ("Disponible", "Disponible"),
            ("En taller", "En taller"),
            ("Fuera de servicio", "Fuera de servicio"),
        ]
    }


# 2. CONDUCTORES
class ConductorView(ModelView):
    datamodel = SQLAInterface(Conductor)

    list_columns = [
        "nombres",
        "apellidos",
        "numero_licencia",
        "telefono",
        "estado",
    ]

    search_columns = [
        "nombres",
        "apellidos",
        "numero_licencia",
    ]

    add_columns = [
        "nombres",
        "apellidos",
        "numero_licencia",
        "telefono",
        "estado",
    ]

    edit_columns = add_columns

    form_choices = {
        "estado": [
            ("Activo", "Activo"),
            ("Inactivo", "Inactivo"),
        ]
    }


# 3. PAQUETES TURISTICOS
class PaqueteView(ModelView):
    datamodel = SQLAInterface(Paquete)

    list_columns = [
        "nombre_paquete",
        "duracion_dias",
        "precio_persona",
        "descripcion",
    ]

    search_columns = ["nombre_paquete"]

    add_columns = [
        "nombre_paquete",
        "duracion_dias",
        "precio_persona",
        "descripcion",
    ]

    edit_columns = add_columns


# 4. ITINERARIOS
class ItinerarioView(ModelView):
    datamodel = SQLAInterface(Itinerario)

    list_columns = [
        "paquete",
        "dia",
        "actividad",
        "lugar",
    ]

    add_columns = [
        "paquete",
        "dia",
        "actividad",
        "lugar",
        "descripcion",
    ]

    edit_columns = add_columns

    search_columns = ["actividad", "lugar"]


# 5. CLIENTES
class ClienteView(ModelView):
    datamodel = SQLAInterface(Cliente)

    list_columns = [
        "nombres",
        "apellidos",
        "edad",
        "sexo",
        "nacionalidad",
        "ci",
        "pasaporte",
        "telefono",
    ]

    search_columns = [
        "nombres",
        "apellidos",
        "ci",
        "pasaporte",
        "telefono",
        "correo",
    ]

    add_columns = [
        "nombres",
        "apellidos",
        "edad",
        "sexo",
        "nacionalidad",
        "ci",
        "pasaporte",
        "telefono",
        "correo",
    ]

    edit_columns = add_columns

    form_choices = {
        "sexo": [
            ("Masculino", "Masculino"),
            ("Femenino", "Femenino"),
            ("Otro", "Otro"),
        ]
    }


# 6. RESERVAS
class ReservaView(ModelView):
    datamodel = SQLAInterface(Reserva)

    list_columns = [
        "reserva_id",
        "cliente",
        "paquete",
        "fecha_reserva",
        "fecha_salida",
        "cantidad_personas",
        "estado",
    ]

    add_columns = [
        "cliente",
        "paquete",
        "fecha_reserva",
        "fecha_salida",
        "cantidad_personas",
        "estado",
    ]

    edit_columns = add_columns

    search_columns = ["estado"]

    form_choices = {
        "estado": [
            ("Pendiente", "Pendiente"),
            ("Confirmada", "Confirmada"),
            ("Cancelada", "Cancelada"),
        ]
    }


# 7. SALIDAS
class SalidaView(ModelView):
    datamodel = SQLAInterface(Salida)

    list_columns = [
        "salida_id",
        "fecha_inicio",
        "destino",
        "conductor",
        "vehiculo",
        "paquete",
    ]

    add_columns = [
        "fecha_inicio",
        "hora_salida",
        "hora_llegada",
        "destino",
        "observaciones",
        "conductor",
        "vehiculo",
        "paquete",
    ]

    edit_columns = add_columns

    search_columns = [
    "fecha_inicio",
    "destino",
    "hora_salida",
    "hora_llegada"
    ]


# 8. PASAJEROS DE CADA SALIDA
class PasajeroSalidaView(ModelView):
    datamodel = SQLAInterface(PasajeroSalida)

    list_columns = [
        "salida",
        "cliente",
        "destino_individual",
        "observaciones",
    ]

    add_columns = [
        "salida",
        "cliente",
        "destino_individual",
        "observaciones",
    ]

    edit_columns = add_columns

    search_columns = ["destino_individual"]


# 9. PAGOS
class PagoView(ModelView):
    datamodel = SQLAInterface(Pago)

    list_columns = [
        "pago_id",
        "reserva",
        "monto_pagado",
        "fecha_pago",
        "metodo_pago",
    ]

    add_columns = [
        "reserva",
        "monto_pagado",
        "fecha_pago",
        "metodo_pago",
    ]

    edit_columns = add_columns

    form_choices = {
        "metodo_pago": [
            ("Efectivo", "Efectivo"),
            ("QR", "QR"),
            ("Tarjeta", "Tarjeta"),
        ]
    }


# REGISTRO DE VISTAS EN EL MENU
appbuilder.add_view(
    VehiculoView,
    "Vehículos",
    icon="fa-car",
    category="Agencia",
)

appbuilder.add_view(
    ConductorView,
    "Conductores",
    icon="fa-id-card",
    category="Agencia",
)

appbuilder.add_view(
    PaqueteView,
    "Paquetes turísticos",
    icon="fa-suitcase",
    category="Agencia",
)

appbuilder.add_view(
    ItinerarioView,
    "Itinerarios",
    icon="fa-map",
    category="Agencia",
)

appbuilder.add_view(
    ClienteView,
    "Clientes",
    icon="fa-users",
    category="Agencia",
)

appbuilder.add_view(
    ReservaView,
    "Reservas",
    icon="fa-calendar",
    category="Agencia",
)

appbuilder.add_view(
    SalidaView,
    "Salidas",
    icon="fa-truck",
    category="Agencia",
)

appbuilder.add_view(
    PasajeroSalidaView,
    "Pasajeros por salida",
    icon="fa-user",
    category="Agencia",
)

appbuilder.add_view(
    PagoView,
    "Pagos",
    icon="fa-money",
    category="Agencia",
)
