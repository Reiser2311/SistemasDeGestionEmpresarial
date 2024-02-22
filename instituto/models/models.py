# -*- coding: utf-8 -*-

from odoo import models, fields, api


class profesor(models.Model):
    _name = 'instituto.profesor'
    _description = 'instituto.profesor'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre')
    direccion = fields.Char(string="Direccion")
    ciudad = fields.Selection([('malaga', 'Malaga'), ('sevilla', 'Sevilla'), ('huelva', 'Huelva'), ('granada', 'Granada'), ('cordoba', 'Cordoba'), ('jaen', 'Jaen'), ('cadiz', 'Cadiz'), ('almeria', 'Almeria')], string='Ciudad')
    telefono = fields.Char(string='Numero')
    asignaturas = fields.One2many('instituto.asignatura', 'profesor', string='Asignaturas')

class estudiante(models.Model):
    _name = 'instituto.estudiante'
    _description = 'instituto.estudiante'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre')
    apellidos = fields.Char(string='Apellidos')
    direccion = fields.Char(string="Direccion")
    ciudad = fields.Char(string='Ciudad')
    asignaturas = fields.Many2many('instituto.asignatura')

class asignatura(models.Model):
    _name = 'instituto.asignatura'
    _description = 'instituto.asignatura'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre')
    nivel = fields.Integer(string='Nivel')
    imagen = fields.Binary(string='Imagen')
    profesor = fields.Many2one('instituto.profesor')
    alumnado = fields.Many2many('instituto.estudiante')