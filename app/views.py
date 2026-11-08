
from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask import request
from flask_appbuilder import BaseView, expose
from datetime import datetime
from flask_appbuilder.security.decorators import has_access
from .ai import consultar_ia

from .extensions import appbuilder, db
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



# ==========================================
# 10. REPORTE DE SALIDAS Y PASAJEROS
# ==========================================

class ReporteSalidasView(BaseView):

    route_base = "/reporte_salidas"

    @expose("/")
    def list(self):

        # Obtener los filtros del formulario
        fecha = request.args.get("fecha", "")
        destino = request.args.get("destino", "")

        # Consultar las salidas de la base de datos
        consulta = db.session.query(Salida)

        # Filtrar por fecha
        if fecha:
            fecha_convertida = datetime.strptime(fecha, "%Y-%m-%d").date()

            consulta = consulta.filter(
                Salida.fecha_inicio == fecha_convertida
            )

        # Filtrar por destino
        if destino:
            consulta = consulta.filter(
                Salida.destino.ilike(f"%{destino}%")
            )

        # Ordenar por fecha
        salidas = consulta.order_by(
            Salida.fecha_inicio.desc()
        ).all()

        return self.render_template(
            "reportes/salidas.html",
            salidas=salidas,
            fecha=fecha,
            destino=destino
        )


# REGISTRO DEL REPORTE EN EL MENU
appbuilder.add_view(
    ReporteSalidasView,
    "Reporte de salidas",
    icon="fa-file-text",
    category="Reportes",
)


# ==========================================
# 11. REPORTE DE RESERVAS
# ==========================================

class ReporteReservasView(BaseView):

    route_base = "/reporte_reservas"

    @expose("/")
    def list(self):

        # Obtener los filtros del formulario
        fecha_salida = request.args.get("fecha_salida", "")
        estado = request.args.get("estado", "")

        # Consultar las reservas
        consulta = db.session.query(Reserva)

        # Filtrar por fecha de salida
        if fecha_salida:
            fecha_convertida = datetime.strptime(
                fecha_salida, "%Y-%m-%d"
            ).date()

            consulta = consulta.filter(
                Reserva.fecha_salida == fecha_convertida
            )

        # Filtrar por estado
        if estado:
            consulta = consulta.filter(
                Reserva.estado == estado
            )

        # Ordenar por fecha de salida
        reservas = consulta.order_by(
            Reserva.fecha_salida.desc()
        ).all()

        return self.render_template(
            "reportes/reservas.html",
            reservas=reservas,
            fecha_salida=fecha_salida,
            estado=estado
        )


# REGISTRO DEL REPORTE EN EL MENU
appbuilder.add_view(
    ReporteReservasView,
    "Reporte de reservas",
    icon="fa-calendar",
    category="Reportes",
)

# ==========================================
# 12. REPORTE DE PAGOS
# ==========================================

class ReportePagosView(BaseView):

    route_base = "/reporte_pagos"

    @expose("/")
    def list(self):

        # Obtener los filtros del formulario
        fecha_pago = request.args.get("fecha_pago", "")
        metodo_pago = request.args.get("metodo_pago", "")

        # Consultar los pagos
        consulta = db.session.query(Pago)

        # Filtrar por fecha de pago
        if fecha_pago:
            fecha_convertida = datetime.strptime(
                fecha_pago, "%Y-%m-%d"
            ).date()

            consulta = consulta.filter(
                Pago.fecha_pago == fecha_convertida
            )

        # Filtrar por método de pago
        if metodo_pago:
            consulta = consulta.filter(
                Pago.metodo_pago == metodo_pago
            )

        # Ordenar por fecha de pago
        pagos = consulta.order_by(
            Pago.fecha_pago.desc()
        ).all()

        return self.render_template(
            "reportes/pagos.html",
            pagos=pagos,
            fecha_pago=fecha_pago,
            metodo_pago=metodo_pago
        )


# REGISTRO DEL REPORTE EN EL MENU
appbuilder.add_view(
    ReportePagosView,
    "Reporte de pagos",
    icon="fa-money",
    category="Reportes",
)



# ==========================================
# 11. ASISTENTE TURISTICO CON INTELIGENCIA ARTIFICIAL
# ==========================================

class AsistenteTuristicoView(BaseView):

    route_base = "/asistente_turistico"

    @expose("/", methods=["GET", "POST"])
    @has_access
    def chat(self):

        pregunta = ""
        respuesta = ""

        # Consultar los paquetes registrados en MySQL
        paquetes = (
            db.session.query(Paquete)
            .order_by(Paquete.nombre_paquete)
            .all()
        )

        # Preparar la informacion real de la agencia
        informacion_agencia = ""

        for paquete in paquetes:

            informacion_agencia += (
                f"\nPAQUETE: {paquete.nombre_paquete}\n"
                f"DURACION: {paquete.duracion_dias} dias\n"
                f"PRECIO POR PERSONA: {paquete.precio_persona}\n"
                f"DESCRIPCION: {paquete.descripcion or 'Sin descripcion'}\n"
                "ITINERARIO:\n"
            )

            itinerarios = sorted(
                paquete.itinerarios,
                key=lambda item: item.dia
            )

            for itinerario in itinerarios:

                informacion_agencia += (
                    f"- Dia {itinerario.dia}: "
                    f"{itinerario.actividad}. "
                    f"Lugar: {itinerario.lugar or 'No especificado'}. "
                    f"Descripcion: "
                    f"{itinerario.descripcion or 'Sin descripcion'}.\n"
                )

        if not informacion_agencia:
            informacion_agencia = (
                "Actualmente no hay paquetes turisticos "
                "registrados en la base de datos."
            )

        # Procesar la pregunta del cliente
        if request.method == "POST":

            pregunta = request.form.get("pregunta", "").strip()

            if pregunta:

                respuesta = consultar_ia(
                    pregunta,
                    informacion_agencia
                )

        return self.render_template(
            "asistente.html",
            pregunta=pregunta,
            respuesta=respuesta,
            paquetes=paquetes
        )


# REGISTRO DEL ASISTENTE EN EL MENU
appbuilder.add_view(
    AsistenteTuristicoView,
    "Asistente turístico",
    icon="fa-comments",
    href="/asistente_turistico/"
)