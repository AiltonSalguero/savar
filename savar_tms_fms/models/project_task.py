from odoo import api, fields, models


class ProjectTask(models.Model):
    _inherit = 'project.task'
    
    task_service_id = fields.Many2one('project.task.service', string='Servicio')
    task_subservice_id = fields.Many2one('project.task.subservice', string='Subservicio')
    
