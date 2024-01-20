from odoo import models, fields
class DemoClass(models.Model):
    _name= "demo.class"
    name = fields.Char("Name")
    date = fields.Date("Date")
    _order = "name, date_published desc"
    name = fields.Char("Title", default=None, help = "Book cover title.", readonly= False, index = False, deprecated = True, groups="", states={})
    title = fields.Char("ISBN")
    book_type = fields.Selection(
        [("paper", "Paperback"),
         ("hard", "Hardcover"),
         ("electronic", "Electronic"),
         ("other", "Other")],"Type")
    notes = fields.Text("Internal Notes")
    descr = fields.Html("Description")

    copies = fields.Integer(default=1)
    average_rating = fields.Float("Average Rating", (3,2))
    price = fields.Monetary("Price", "currency_id")
    
    currency_id= fields.Many2one("res.currency")

    date_published = fields.Date()
    last_borrowed_date = fields.Datetime(
        "last borrowed on",
        default= lambda self: fields.Datetime.now()
        # default this part of the code defines a default value for the last_borrowed_date field using a Python lambda function.
# The lambda function is used to execute fields.Datetime.now() when a new record is created, providing the current date and time as the default value for the field.
    )