from odoo import models, fields, api, _

class ProjectTaskServiceType(models.Model):
    _name = 'project.task.service'
    
    name = fields.Char(string='Nombre')
    parent_id = fields.Many2one('project.task.service', string='Servicio Padre')