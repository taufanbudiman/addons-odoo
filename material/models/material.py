from odoo import fields, models, api
from odoo.exceptions import UserError


class Material(models.Model):
    _name = 'material.material'
    _description = 'Material Models'

    _material_type = [
        ('1', 'Fabric'),
        ('2', 'Jeans'),
        ('3', 'Cotton'),
    ]

    material_code = fields.Char(string='Code', required=True)
    name = fields.Char(string='Name', required=True)
    material_type = fields.Selection(
        _material_type, 'Type', index=True, required=True,
        help='1 - Fabric\n'
             '2 - Jeans\n'
             '3 - Cotton')
    buy_price = fields.Float(string='Buy Price', required=True)
    supplier_id = fields.Many2one('res.partner', string='Supplier',
                                  required=True,
                                  domain=[('supplier_rank', '>=', 1)])

    @api.constrains('buy_price')
    def _onchange_buy_price(self):
        for record in self:
            if 0 <= record.buy_price < 100:
                raise UserError('Buy Price must be greater than 100')


