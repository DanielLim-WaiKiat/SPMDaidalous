from config import db

class Invoice(db.Model):
    __tablename__ = "invoice"

    invoice_id = db.Column(db.Integer, primary_key=True)
    invoice_category = db.Column(db.String, nullable=False)
    invoice_number = db.Column(db.String, nullable=False)
    invoice_date = db.Column(db.Date, nullable=False)
    payment_method = db.Column(db.String, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    supplier_id = db.Column(db.Integer, nullable=False)
    emission_amount = db.Column(db.Float, nullable=False)
    image_path = db.Column(db.String, nullable=False)
    company_id = db.Column(db.Integer, nullable=False)
    location_id = db.Column(db.Integer, nullable=False)

    
    def __init__(self, invoice_id, invoice_category, invoice_number, invoice_date, payment_method, total_amount, supplier_id, image_path, company_id, location_id):
        self.location_id = location_id
        self.company_id = company_id
        self.invoice_id = invoice_id
        self.invoice_category = invoice_category
        self.invoice_number = invoice_number
        self.invoice_date = invoice_date
        self.payment_method = payment_method
        self.total_amount = total_amount
        self.supplier_id = supplier_id
        self.image_path = image_path
    
