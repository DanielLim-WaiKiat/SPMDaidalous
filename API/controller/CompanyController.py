from model.CompanyLocations import CompanyLocations
from flask import jsonify
from config import app, db

class CompanyController():

    def get_locations(request):
        data = request.get_json()
        try:
            if len(data) > 0:
                try:
                    locations = CompanyLocations.query.filter_by(company_id=data["company_id"]).all()

                    if locations == None:
                        return jsonify({
                            "code": 404,
                            "status": False,
                            "data": "Locations not found"
                        })
                    else:
                       locations_data = [l.location_name for l in locations]
                       print(locations_data)
                       return jsonify({
                            "code": 200,
                            "data": locations_data
                        })

                except Exception as error:
                    print(error)
                    return jsonify(
                        {
                            "code": 500,
                            "data": "Company Locations error. Please contact the administrator"
                        }
                    )
        except Exception as error:
            print(error)
            return jsonify(
                {
                    "code": 500,
                    "data": "Data format error"
                }
            )
        
    def get_emission_goals(request):
        data = request.get_json()
        try:
            if len(data) > 0:
                try:
                    locations = CompanyLocations.query.filter_by(company_id=data["company_id"]).all()

                    if locations == None:
                        return jsonify({
                            "code": 404,
                            "status": False,
                            "data": "Locations not found"
                        })
                    else:
                       locations_data = [l.emission_goal for l in locations]
                       print(locations_data)
                       return jsonify({
                            "code": 200,
                            "data": locations_data
                        })

                except Exception as error:
                    print(error)
                    return jsonify(
                        {
                            "code": 500,
                            "data": "Company Locations error. Please contact the administrator"
                        }
                    )
        except Exception as error:
            print(error)
            return jsonify(
                {
                    "code": 500,
                    "data": "Data format error"
                }
            )
        
    def get_emission_goals_by_location(request):
        data = request.get_json()
        try:
            if len(data) > 0:
                try:
                    locations = CompanyLocations.query.filter_by(company_id=data["company_id"], location_id=data["location_id"]).all()

                    if locations == None:
                        return jsonify({
                            "code": 404,
                            "status": False,
                            "data": "Locations not found"
                        })
                    else:
                       locations_data = [l.emission_goal for l in locations]
                       print(locations_data)
                       return jsonify({
                            "code": 200,
                            "data": locations_data
                        })

                except Exception as error:
                    print(error)
                    return jsonify(
                        {
                            "code": 500,
                            "data": "Company Locations error. Please contact the administrator"
                        }
                    )
        except Exception as error:
            print(error)
            return jsonify(
                {
                    "code": 500,
                    "data": "Data format error"
                }
            )