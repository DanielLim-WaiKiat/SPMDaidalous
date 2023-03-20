from model.Company import Company
from flask import jsonify
from config import app, db

class CompanyController2():

    def get_company_id_by_name(name):
        try:
            if len(name) > 0:
                try:
                    company = Company.query.filter_by(company_name=name).first()
                    print(f'here {company.company_id}')
                    if company == None:
                        return jsonify({
                            "code": 404,
                            "status": False,
                            "data": "Company ID not found"
                        })
                    else:
                        return jsonify({
                            "code": 200,
                            "data": company.company_id
                        })

                except Exception as error:
                    print(error)
                    return jsonify(
                        {
                            "code": 500,
                            "data": "Company error. Please contact the administrator"
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