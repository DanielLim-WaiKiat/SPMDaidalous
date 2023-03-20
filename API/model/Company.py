from config import db

class Company(db.Model):
    __tablename__ = "company"

    company_id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    industry = db.Column(db.String, nullable=False)

    
    def __init__(self, company_id, company_name, address, industry):
        self.company_id = company_id
        self.company_name = company_name
        self.address = address
        self.industry = industry
        
    
