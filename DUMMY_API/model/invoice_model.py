from config import *

class Invoice(db.Model):
    __tablename__ = 'invoice'

    invoice_id = db.Column(db.Integer, primary_key=True)
    invoice_category = db.Column(db.String, nullable=False)
    invoice_number = db.Column(db.String, nullable=False)
    invoice_date = db.Column(db.Date, nullable=False)
    payment_method = db.Column(db.String, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    company_name = db.Column(db.String, nullable=False)
    supplier_name = db.Column(db.String, nullable=False)

    
    def __init__(self, invoice_id, invoice_category, invoice_number, invoice_date, payment_method, total_amount, company_name, supplier_name):

        self.invoice_id = invoice_id
        self.invoice_category = invoice_category
        self.invoice_number = invoice_number
        self.invoice_date = invoice_date
        self.payment_method = payment_method
        self.total_amount = total_amount
        self.company_name = company_name
        self.supplier_name = supplier_name

    def jsonInvoice(self):
        return {
            "invoice_id": self.invoice_id,
            "invoice_category": self.invoice_category,
            "invoice_number": self.invoice_number,
            "invoice_date": self.invoice_date,
            "payment_amount": self.payment_method,
            "total_amount": self.total_amount,
            "company_name": self.company_name,
            "supplier_name": self.supplier_name
        }