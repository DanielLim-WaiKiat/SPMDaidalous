from config import db
from model.invoice_model import Invoice
from flask import jsonify
import requests

class InvoiceController():

    def getAllInvoice():
        invoices = Invoice.query.all()
        # print(invoices)
        if len(invoices) > 0:
            return jsonify(
                {
                "code": 200,
                "data": [invoice.jsonInvoice() for invoice in invoices]
                }
            )

        return jsonify(
            {
                "code": 404,
                "message": "No invoices"
            }
        )
    
    def addInvoice(request):
        if request.is_json:
            data = request.get_json()
            # print(data)
            if len(data) > 0:
                invoice_category, invoice_number, invoice_date, payment_method, total_amount, company_name, supplier_name, location_name = data["invoice_category"], data["invoice_number"], data["invoice_date"], data["payment_method"], data["total_amount"], data["company_name"], data["supplier_name"], data["location_name"]
                # call daidalous api to push
                url = 'http://localhost:5003/invoice/insertinvoiceviadummy'
                requestObj = {
                    'invoice_category':invoice_category,
                    'invoice_number': invoice_number,
                    'invoice_date': invoice_date,
                    'payment_method': payment_method,
                    'total_amount': total_amount,
                    'company_name': company_name,
                    'supplier_name': supplier_name,
                    'location_name': location_name
                }
                x = requests.post(url, json = requestObj)
                print(x)
                try:
                    newInvoice = Invoice(None, 
                                         data['invoice_category'], 
                                         data['invoice_number'],
                                         data['invoice_date'],
                                         data['payment_method'],
                                         data['total_amount'],
                                         data['company_name'],
                                         data['supplier_name']
                                        )
                    db.session.add(newInvoice)
                    db.session.commit()
                    return jsonify(
                        {
                            "code": 200,
                            "data": "Success"
                        }
                    )
                except Exception as error:
                    return jsonify(
                        {
                            "code": 500,
                            "data": "insert error",
                            "error": str(error)
                        }
                    )
        else:
            data = request.get_data()
            print(data)
            return jsonify(
                {
                    "code": 400,
                    "data": str(data),
                    "message": "Invalid input type. pls input as json"
                }
            )

    # def updateShipper(request):

    #     if request.is_json:
    #         data = request.get_json()
    #         shipper_id = data['shipper_id']
    #         company_name = data['company_name']
    #         phone_number = data['phone_number']
    #         try:
    #             shipper = Shipper.query.filter_by(ShipperID=shipper_id).first()
    #             shipper.CompanyName = company_name
    #             shipper.Phone = phone_number
    #             db.session.commit()
    #             return jsonify(
    #                 {
    #                     "code": 200,
    #                     "message": f'Successfully updated shipper {shipper_id}'
    #                 }
    #             )
    #         except Exception as error:
    #             return jsonify(
    #                 {
    #                     "code": 500,
    #                     "message": "Error updating shipper"
    #                 }
    #             )
    #     else:
    #         return jsonify(
    #             {
    #                 "code": 400,
    #                 "data": str(data),
    #                 "message": "Invalid input type. pls input as json"
    #             }
    #         )


    def deleteInvoice(request):
        if request.is_json:
            invoice_id = request.get_json()['invoice_id']
            try:
                invoice = Invoice.query.filter_by(InvoiceID=invoice_id).first()
                db.session.delete(invoice)
                db.session.commit()
                return jsonify(
                    {
                        "code": 200,
                        "message": f'Invoice with ID {invoice_id} is deleted'
                    }
                )
            except Exception as error:
                return jsonify(
                    {
                        "code": 500,
                        "message": "Error deleting invoice"
                    }
                )

        return jsonify(
            {
                "code": 400,
                "data": str(request.get_data()),
                "message": "Invalid input type. Please input as json format"
            }
        )