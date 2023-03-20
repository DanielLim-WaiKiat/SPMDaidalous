from model.Supplier import Supplier
from flask import jsonify
from config import app, db

class SupplierController():
    def get_supplier_id_by_name(name):
        try:
            if len(name) > 0:
                try:
                    supplier = Supplier.query.filter_by(supplier_name=name).first()
                    print(f'here {supplier.supplier_id}')
                    if supplier == None:
                        return jsonify({
                            "code": 404,
                            "status": False,
                            "data": "Supplier ID not found"
                        })
                    else:
                        return jsonify({
                            "code": 200,
                            "data": supplier.supplier_id
                        })

                except Exception as error:
                    print(error)
                    return jsonify(
                        {
                            "code": 500,
                            "data": "Supplier error. Please contact the administrator"
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