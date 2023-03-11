from config import db

class CompanyLocations(db.Model):
    __tablename__ = "company_locations"

    location_id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, nullable=False)
    location_name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    emission_goal = db.Column(db.Float, nullable=False)

    
    def __init__(self, location_id, company_id, location_name, address, emission_goal):
        self.location_id = location_id
        self.company_id = company_id
        self.location_name = location_name
        self.address = address
        self.emission_goal = emission_goal
        
    
