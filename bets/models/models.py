# -*- coding: utf-8 -*-

from odoo import models, fields, api

class personal(models.Model):
    _name = 'bets.personal'

    name = fields.Char(string = "Nombre", required = True)
    apellidos = fields.Char(string="Apellidos", required=True)
    dni = fields.Char(string="DNI", required = True)
    puesto = fields.Many2one("bets.puesto", string="Puesto", required = True)
    notas = fields.Text(string = "Observaciones del empleado")

class puesto(models.Model):
    _name = 'bets.puesto'

    name = fields.Char(string="Cargo", required = True)
    horas_mensuales = fields.Integer(string="Nº de horas mensuales", required = True)
    sueldo_hora = fields.Integer(string="Euros por hora", required = True)
    sueldo = fields.Integer(compute="_value_pc", store=True)
    notas = fields.Text(string = "Observaciones del empleado")

    @api.depends('horas_mensuales','sueldo_hora')
    def _value_pc(self):
        self.sueldo = int(self.horas_mensuales) * int(self.sueldo_hora)

class cliente(models.Model):
    _name = 'bets.cliente'

    dni = fields.Char(string="DNI", required = True)
    nombre = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    name = fields.Char(compute="_value_nusuario", store = True)
    saldoinicial = fields.Char(string="SaldoInicial", store = True)
    saldo = fields.Integer(compute = "_calculoSaldo")
    apuesta = fields.One2many("bets.apuesta", "cliente", string="Apuesta")

    @api.depends('nombre','apellidos')
    def _value_nusuario(self):
        con = str(self.nombre)[:1] + str(self.apellidos)[:3].lower()
        self.name = str(con)

    @api.one
    @api.depends('apuesta')
    def _calculoSaldo(self):
        total = 0
        for record in self.apuesta:
            total = total + record.dineroApostado
            self.saldo = int(self.saldoinicial) - total

class partidos(models.Model):
    _name = 'bets.partidos'

    name = fields.Char(compute="_value_partido", store = True)
    equipo1 = fields.Char(string = "Equipo1", required = True)
    equipo2 = fields.Char(string = "Equipo2", required = True)
    dia = fields.Date(String = "Dia partido", required = True)

    @api.depends('equipo1','equipo2')
    def _value_partido(self):
        con = str(self.equipo1) + " - " + str(self.equipo2)
        self.name = str(con)

class apuesta(models.Model):
    _name = 'bets.apuesta'

    cliente = fields.Many2one("bets.cliente", string="Cliente", required=True)
    partidos = fields.Many2one("bets.partidos", string="Partidos", required=True)
    dineroApostado = fields.Integer(String="Dinero apostado", required=True)
