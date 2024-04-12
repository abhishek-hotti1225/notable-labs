import flask
from flask import Flask, request
from flask_restx import Api, Resource, fields

app = flask.Flask(__name__)
api = Api()
api.init_app(
    app,
    title="Abhi Notable REST APIs",
    description="Rest API for the Notable Labs project",
)
abhi_default = api.default_namespace
ns_notable = api.namespace("", description="Notable Labs Name Space")

findUserBody = ns_notable.model(
    "UserModel",
    {
        "user": fields.String(description="UserName", required=True, default="abhi"),
        "company": fields.String(
            description="CompanyName", required=True, default="notbal"
        ),
    },
)


@ns_notable.route("/findUser")
class KubeHunt(Resource):
    @ns_notable.doc(params={"ipaddress": "The User Of Company"}, required=True)
    def get(self):
        ipaddress = request.args.get("ipaddress")
        if ipaddress:
            print(ipaddress)
        else:
            print("Not Passed")
        return {"Doc": "124"}

    @ns_notable.doc(body=findUserBody)
    def post(self):
        content = request.json
        com = content["company"]
        user = content["user"]

        return com + user


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
