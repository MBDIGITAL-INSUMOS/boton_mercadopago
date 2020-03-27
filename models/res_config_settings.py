from odoo import fields, models

import logging

_logger = logging.getLogger(__name__)


class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'
    mercadopago_client = fields.Char(
        string='Client id',
    )
    mercadopago_key = fields.Char(
        string='Client secret',
    )

    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res['mercadopago_client'] = self.env['ir.config_parameter'].sudo(
        ).get_param('mercadopago_client', default=False)
        res['mercadopago_key'] = self.env['ir.config_parameter'].sudo(
        ).get_param('mercadopago_key', default=False)


        return res


    def set_values(self):
        self.env['ir.config_parameter'].sudo().set_param(
            'mercadopago_client', self.mercadopago_client)
        self.env['ir.config_parameter'].sudo().set_param(
            'mercadopago_key', self.mercadopago_key)
        super(ResConfigSettings, self).set_values()
