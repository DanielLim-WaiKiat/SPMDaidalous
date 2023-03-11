import config
from controller.UserController import UserController
from controller.CompanyController import CompanyController
from controller.InvoiceController import InvoiceController
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS
from model.User import User

app = config.app
CORS(app)


@app.route("/monitoring")
def test_api():
    return jsonify(
        {
            "code": 200,
            "data": "API monitoring is working"
        }
    )


@app.route("/user/auth", methods=["POST"])
def auth_user():
    response = UserController.auth_user(request)
    return response


@app.route("/company/locations", methods=["POST"])
def get_locations():
    return CompanyController.get_locations(request)


@app.route("/invoice/emission", methods=["POST"])
def get_emission_by_company():
    return InvoiceController.get_emission_by_company(request)


@app.route("/invoice/emissionlocation", methods=["POST"])
def get_emission_by_company_location():
    return InvoiceController.get_emission_by_company_location(request)


@app.route("/invoice/emissionscope", methods=["POST"])
def get_emission_scope_by_company():
    return InvoiceController.get_emission_scope_by_company(request)


@app.route("/invoice/emissionscopelocation", methods=["POST"])
def get_emission_scope_by_company_location():
    return InvoiceController.get_emission_scope_by_company_location(request)


@app.route("/company/emissiongoal", methods=["POST"])
def get_emission_goals():
    return CompanyController.get_emission_goals(request)


@app.route("/company/emissiongoallocation", methods=["POST"])
def get_emission_goals_by_location():
    return CompanyController.get_emission_goals_by_location(request)


@app.route("/invoice/taxcompany", methods=["POST"])
def get_tax_by_company():
    return InvoiceController.get_tax_by_company(request)


@app.route("/invoice/taxcompanylocation", methods=["POST"])
def get_tax_by_company_location():
    return InvoiceController.get_tax_by_company_location(request)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
