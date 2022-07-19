from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Student(Resource):
    def get(self, name):
        return {"student_name": name}


api.add_resource(Student, "/student/<string:name>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
