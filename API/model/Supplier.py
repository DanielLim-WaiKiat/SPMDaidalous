from config import db

class Supplier(db.Model):
    __tablename__ = "supplier"

    supplier_id = db.Column(db.Integer, primary_key=True)
    supplier_name = db.Column(db.String, nullable=False)
    supplier_email = db.Column(db.String, nullable=False)
    supplier_phone = db.Column(db.String, nullable=False)
    supplier_address = db.Column(db.String, nullable=False)

    
    def __init__(self, supplier_id, supplier_name, supplier_email, supplier_phone, supplier_address):
        self.supplier_id = supplier_id
        self.supplier_name = supplier_name
        self.supplier_email = supplier_email
        self.supplier_phone = supplier_phone
        self.supplier_address = supplier_address
        
    
