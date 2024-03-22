from flask import Flask
from flask_restful import Api
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

#업로드용 폴더 설정
UPLOAD_ROOT=os.getcwd()
app.config['UPLOAD_FOLDER']=os.path.join(UPLOAD_ROOT, 'uploads')
#최대 파일 업로드 용량 1M로 설정v
app.config['MAX_CONTENT_LENGTH']= 1* 1024 * 1024
api = Api(app)

from api.mask_detection import MaskDetection
api.add_resource(MaskDetection,'/mask')
if __name__ == '__main__':
    app.run(debug=True)