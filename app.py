# import liblary
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

# inisiasi object flask

app = Flask(__name__)

# inisiasi object flask_restful
api = Api(app)

# inisiasi object flask__cors
CORS(app)

# inisiasi variabel kosong bertipe dictianory
identitas = {}

# membuat class resource
class ContohResource(Resource):
    def get(self):
        # response = {"msg": "Hallo Dunia, Test api"}
        return identitas
    
    def post(self):
        data = request.get_json(force=True)
        nama = data.get("nama")
        umur = data.get("umur")
        identitas["nama"] = nama
        identitas["umur"] = umur
        response = {"msg": "Data berhasil dimasukan"}
        return response
    
api.add_resource(ContohResource, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)