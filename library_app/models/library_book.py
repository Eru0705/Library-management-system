from odoo import models, fields, api
from odoo.exceptions import ValidationError
class Book(models.Model):
    _name = "library.book"
    _description = "Book"
    name = fields.Char("Title")
    isbn = fields.Char("ISBN")
    active = fields.Boolean("Active?", default = True)
    date_published = fields.Date()
    image = fields.Binary("Cover")
    publisher_id = fields.Many2one("res.partner", string = "Publisher")
    author_ids = fields.Many2many("res.partner",string = "Authors")

    @api.constrains('isbn')
    def check_isbn(self):
        for book in self:
            if not book.isbn:
                raise ValidationError("Please provide an ISBN for %s" % book.name)

            if book.isbn and not len(book.isbn) ==5:
                raise ValidationError("%s ISBN is invalid\n Needs to be five digits only"%book.isbn)
            return True
        
    publisher_country_id=fields.Many2one(
        "res.country",string="Publisher Country",
        compute="_compute_publisher_country",
    )

    @api.depends("publisher_id.country_id")
    def compute_publisher_country(self):
        for book in self:
            book.publisher_country_id=Book.publisher_id.country_id
    
    @api.constrains('isbn')
    def constrain_isbn_valid(self):
        for book in self:
            if book.isbn and not book._check_isbn():
                raise ValidationError("%s is an invalid ISBN"%book.isbn)