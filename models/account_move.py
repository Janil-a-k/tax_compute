from odoo import fields,models,api

class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    def compute_tax(self):
        amount = 0
        for tax in self.tax_ids:
            amount = amount + tax.amount
        return ((self.quantity * self.price_unit) / 100) * amount
