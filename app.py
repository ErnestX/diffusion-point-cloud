from flask import Flask
# from werkzeug.utils import secure_filename
from flask import request
from flask import Response
from flask import json
from flask.json import jsonify
# from markupsafe import escape
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


############ Get JSON
@app.route('/generateFromLatentCode/', methods=['POST'])
def generateFromLatentCode():
    # set force to True to read it as JSON (ignore the content type set by client)
    try:
        content = request.get_json(force=True, silent=False, cache=True) 
    except:
        return "cannot parse JSON"
    
    requestId = content['id']
    latentCode = content['latentCode']

    return { 
        "id": requestId,
        "latentCode": latentCode,
        # "pointCloud": generatedPointCloud
    }
    


############ Return JSON
@app.route("/generateExamplePointClouds")
def sendTestPointCloud():
    testLatentCode = np.load(latentCode_path)
    testPointCloud = np.load(pointCloud_path)
    # examplePC = jsonify(id = 'exampleID', 
    #                    latentCode = testLatentCode.tolist(), 
    #                    pointCloud = testPointCloud.tolist())
    examplePC = json.dumps({'id': 'exampleID', 
                            'latentCode': testLatentCode.tolist(), 
                            'pointCloud': testPointCloud.tolist()})
                            
    r = Response(examplePC, mimetype='application/json')
    assert r.content_type == 'application/json'
    return r

# @app.route("/users")
# def users_api():
#     users = get_all_users()
#     return [user.to_json() for user in users]

