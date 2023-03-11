from model.Invoice import Invoice
from flask import jsonify
from config import app, db
import datetime

class InvoiceController():

    def get_emission_by_company(request):
        data = request.get_json()
        try:
            if len(data) > 0:
                try:
                    emissions = Invoice.query.filter_by(company_id=data["company_id"]).all()

                    if emissions == None:
                        return jsonify({
                            "code": 404,
                            "status": False,
                            "data": "Locations not found"
                        })
                    else:
                       emission_data = [l.emission_amount for l in emissions]
                       return jsonify({
                            "code": 200,
                            "data": emission_data
                        })

                except Exception as error:
                    print(error)
                    return jsonify(
                        {
                            "code": 500,
                            "data": "Emission error. Please contact the administrator"
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
    
    def get_emission_by_company_location(request):
        data = request.get_json()
        try:
            if len(data) > 0:
                try:
                    emissions = Invoice.query.filter_by(company_id=data["company_id"], location_id=data["location_id"]).all()

                    if emissions == None:
                        return jsonify({
                            "code": 404,
                            "status": False,
                            "data": "Locations not found"
                        })
                    else:
                       emission_data = [l.emission_amount for l in emissions]
                       return jsonify({
                            "code": 200,
                            "data": emission_data
                        })

                except Exception as error:
                    print(error)
                    return jsonify(
                        {
                            "code": 500,
                            "data": "Emission error. Please contact the administrator"
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
        

    def get_emission_by_company_location(request):
        data = request.get_json()
        try:
            if len(data) > 0:
                try:
                    emissions = Invoice.query.filter_by(company_id=data["company_id"], location_id=data["location_id"]).all()

                    if emissions == None:
                        return jsonify({
                            "code": 404,
                            "status": False,
                            "data": "Locations not found"
                        })
                    else:
                       emission_data = [l.emission_amount for l in emissions]
                       return jsonify({
                            "code": 200,
                            "data": emission_data
                        })

                except Exception as error:
                    print(error)
                    return jsonify(
                        {
                            "code": 500,
                            "data": "Emission error. Please contact the administrator"
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
        
    def get_emission_scope_by_company(request):
        data = request.get_json()
        scope_1 = ("Petrol")
        scope_2 = ("Water", "Electricity")
        scope_3 = ("Travel", "Material", "Delivery")
        scope_1_output = 0
        scope_2_output = 0
        scope_3_output = 0
        try:
            if len(data) > 0:
                try:
                    emissions = Invoice.query.filter_by(company_id=data["company_id"]).all()

                    if emissions == None:
                        return jsonify({
                            "code": 404,
                            "status": False,
                            "data": "Locations not found"
                        })
                    else:
                        emission_data = [(l.invoice_category, l.emission_amount) for l in emissions]
                       
                        for i in emission_data:
                            if i[0] in scope_1:
                                scope_1_output += i[1]
                            elif i[0] in scope_2:
                                scope_2_output += i[1]
                            elif i[0] in scope_3:
                                scope_3_output += i[1]

                        return jsonify({
                            "code": 200,
                            "data": {
                                "scope1": scope_1_output,
                                "scope2": scope_2_output,
                                "scope3": scope_3_output
                            }
                        })

                except Exception as error:
                    print(error)
                    return jsonify(
                        {
                            "code": 500,
                            "data": "Emission error. Please contact the administrator"
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
        
    def get_emission_scope_by_company_location(request):
        data = request.get_json()
        scope_1 = ("Petrol")
        scope_2 = ("Water", "Electricity")
        scope_3 = ("Travel", "Material", "Delivery")
        scope_1_output = 0
        scope_2_output = 0
        scope_3_output = 0
        try:
            if len(data) > 0:
                try:
                    emissions = Invoice.query.filter_by(company_id=data["company_id"], location_id=data["location_id"]).all()

                    if emissions == None:
                        return jsonify({
                            "code": 404,
                            "status": False,
                            "data": "Locations not found"
                        })
                    else:
                        emission_data = [(l.invoice_category, l.emission_amount) for l in emissions]
                       
                        for i in emission_data:
                            if i[0] in scope_1:
                                scope_1_output += i[1]
                            elif i[0] in scope_2:
                                scope_2_output += i[1]
                            elif i[0] in scope_3:
                                scope_3_output += i[1]

                        return jsonify({
                            "code": 200,
                            "data": {
                                "scope1": scope_1_output,
                                "scope2": scope_2_output,
                                "scope3": scope_3_output
                            }
                        })

                except Exception as error:
                    print(error)
                    return jsonify(
                        {
                            "code": 500,
                            "data": "Emission error. Please contact the administrator"
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
    
    def get_tax_by_company(request):
        data = request.get_json()
        total_emission = {1 : 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
        total_tax = {1 : 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
        try:
            if len(data) > 0:
                try:
                    emissions = Invoice.query.filter_by(company_id=data["company_id"]).all()

                    if emissions == None:
                        return jsonify({
                            "code": 404,
                            "status": False,
                            "data": "Locations not found"
                        })
                    else:
                        emission_data = [(l.invoice_date, l.emission_amount) for l in emissions]
                       
                        for i in emission_data:
                            total_emission[i[0].month] += i[1]
                        
                        for month, emission in total_emission.items():
                            tax_amt = emission / 1000 * 5
                            if tax_amt < 5:
                                if tax_amt != 0:
                                    tax_amt = 5
                            total_tax[month] = tax_amt

                        return jsonify({
                            "code": 200,
                            "data": total_tax
                        })

                except Exception as error:
                    print(error)
                    return jsonify(
                        {
                            "code": 500,
                            "data": "tax emission error. Please contact the administrator"
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
        
    def get_tax_by_company_location(request):
        data = request.get_json()
        total_emission = {1 : 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
        total_tax = {1 : 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
        try:
            if len(data) > 0:
                try:
                    emissions = Invoice.query.filter_by(company_id=data["company_id"], location_id=data["location_id"]).all()

                    if emissions == None:
                        return jsonify({
                            "code": 404,
                            "status": False,
                            "data": "Locations not found"
                        })
                    else:
                        emission_data = [(l.invoice_date, l.emission_amount) for l in emissions]
                       
                        for i in emission_data:
                            total_emission[i[0].month] += i[1]
                        
                        for month, emission in total_emission.items():
                            tax_amt = emission / 1000 * 5
                            if tax_amt < 5:
                                if tax_amt != 0:
                                    tax_amt = 5
                            total_tax[month] = tax_amt

                        return jsonify({
                            "code": 200,
                            "data": total_tax
                        })

                except Exception as error:
                    print(error)
                    return jsonify(
                        {
                            "code": 500,
                            "data": "tax emission error. Please contact the administrator"
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