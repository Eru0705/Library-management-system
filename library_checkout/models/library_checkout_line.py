from odoo import models, fields, api

class CheckoutLine(models.Model):
    _name="library.checkout.line"
    _description= "Checkout Request Line"
    checkout_id=fields.Many2one("library.checkout",required=True)
    book_id=fields.Many2one("library.book", required=True)
    note= fields.Char("Notes")