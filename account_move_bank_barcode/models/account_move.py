# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools, _

class AccountMove(models.Model):
    _inherit = 'account.move'

    bank_barcode = fields.Char(string='Cod. Barras Banco', compute='_compute_bank_barcode')

    def _compute_bank_barcode(self):
        # Formato:
        # - nro convenio: char 1 a 3: 3 digitos (Fijo = 067)
        # - nro factura/cpbte: char 4 a 15: 12 digitos (obligatorio)
        # - fecha vto: char 16 a 21: 6 digitos (DDMMAA obligatorio)
        # - importe: char 22 a 33: 12 digitos (Ultimos 2 digitos corresponden a decimal obligatorio)
        # - espacio libre: char 34 a 50: 17 digitos (si no representa nada completar con 0)
        #
        # Fuente Cod128 standard
        for move in self:
            move.bank_barcode = ''
            bank_barcode = ''
            subscription = ''

            if move.state == 'posted':
                bank_barcode = '067'  # nro convenio
                bank_barcode += ('000000000000' + move.name.replace("-",""))[-12:] #nro factura/cpbte
                bank_barcode += ('000000' + move.invoice_date_due.strftime('%d%m%y'))[-6:]  #fecha vto
                bank_barcode += ('0000000000' + "{:.2f}".format(move.amount_total).replace(".","").replace(",",""))[-12:]  #importe

                for line in move.invoice_line_ids:
                    if line.subscription_id:
                        subscription = line.subscription_id.code[3:]

                bank_barcode += ('00000000000000000' + subscription)[-17:]  #Espacio libre se indica nro de subscripcion

            move.bank_barcode = bank_barcode
