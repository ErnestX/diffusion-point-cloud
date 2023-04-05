from flask import Flask
from werkzeug.utils import secure_filename
from markupsafe import escape
import numpy as np


app = Flask(__name__)
latentCode_path = './latentCode/latentCode.npy'
pointCloud_path = './results/GEN_Ours_chair_1680652639/out.npy'

########### Load the Model





@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# ############ file upload
# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         file = request.files['the_file']
#         file.save(f"/var/www/uploads/{secure_filename(file.filename)}")


# ############ Get JSON
# @app.route('/api/add_message/<uuid>', methods=['GET', 'POST'], mimetype='application/json')
# def add_message(uuid):
#     # set force to True to read it as JSON (ignore the content type set by client)
#     content = request.get_json(force=True) 
#     print(content)
#     #return uuid


############ Return JSON
@app.route("/generateFromCode")
def me_api():
    testLatentCode = np.load(latentCode_path)
    testPointCloud = np.load(pointCloud_path)
    return {
        "id": "requestID",
        "latentCode": testLatentCode.tolist(),
        "pointCloud": testPointCloud.tolist()
    }

# @app.route("/users")
# def users_api():
#     users = get_all_users()
#     return [user.to_json() for user in users]

