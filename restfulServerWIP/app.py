from flask import Flask
from flask_cors import CORS
# from werkzeug.utils import secure_filename
from flask import request
from flask import Response
from flask import json
from flask.json import jsonify
# from markupsafe import escape
import numpy as np


app = Flask(__name__)
CORS(app) # this enables cross-origin resource sharing

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


############ Get JSON
@app.route('/generateFromLatentCode/<requestId>', methods=['POST'])
def generateFromLatentCode(requestId):
    # set force to True to read it as JSON (ignore the content type set by client)
    try:
        content = request.get_json(force=True, silent=False, cache=True) 
    except:
        return "cannot parse JSON"
    
    # requestId = content['id']
    latentCode = content['latentCode']

    return { 
        "requestId": requestId,
        "latentCodes": latentCode,
        # "pointCloud": generatedPointCloud
    }
    


############ Return JSON
@app.route("/generateExamplePointClouds", methods=['GET'])
def sendTestPointCloud():
    testLatentCode = np.load(latentCode_path)
    testPointCloud = np.load(pointCloud_path)
    examplePC = json.dumps({'requestId': 'exampleID', 
                            'latentCodes': testLatentCode.tolist(), 
                            'pointClouds': testPointCloud.tolist()})

    r = Response(examplePC, mimetype='application/json')
    assert r.content_type == 'application/json'
    return r

# @app.route("/users")
# def users_api():
#     users = get_all_users()
#     return [user.to_json() for user in users]

