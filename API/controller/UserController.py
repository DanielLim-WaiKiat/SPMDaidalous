from model.User import User
from flask import jsonify
from config import app, db

class UserController():

    def auth_user(request):
        data = request.get_json()
        try:
            if len(data) > 0:
                try:
                    user_data = User.query.filter_by(username=data["username"]).first()

                    if user_data == None:
                        return jsonify({
                            "code": 404,
                            "status": False,
                            "data": "User not found"
                        })
                    else:
                        if user_data.password == data["password"]:
                            return jsonify({
                                "code": 200,
                                "status": True
                            })
                        else:
                             return jsonify({
                                "code": 200,
                                "status": False
                            })

                except Exception as error:
                    print(error)
                    return jsonify(
                        {
                            "code": 500,
                            "data": "User Auth error. Please contact the administrator"
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
        
            
    