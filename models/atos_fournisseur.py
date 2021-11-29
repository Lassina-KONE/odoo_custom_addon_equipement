from odoo import fields, models

class AtosFournisseur(models.Model):
	_name = 'res.partner'
	_inherit = 'res.partner'
	_description = 'Fournisseurs des Equipements du Stock Atos'
	
	name = fields.Char('Nom de la marque',required=True)
	equipement_ids = fields.One2many("atos_equipement","partner_id")
