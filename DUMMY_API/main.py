from config import *
from controller.invoice_controller import *

    
@app.route("/monitoring")
def test_api():
    return jsonify(
        {
            "code": 200,
            "data": "API monitoring is working"
        }
    )

@app.route('/dummy/getall', methods=['GET'])
def getAllInvoice():
    return InvoiceController.getAllInvoice()

@app.route('/dummy/addInvoice', methods=['POST'])
def addInvoice():
    return InvoiceController.addInvoice(request)

@app.route('/dummy/deleteInvoice', methods=['POST'])
def deleteInvoice():
    return InvoiceController.deleteInvoice(request)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004, debug=True)