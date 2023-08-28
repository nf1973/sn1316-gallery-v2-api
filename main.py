from flask import Flask
from flask_cors import CORS
from bson import json_util
from bson.objectid import ObjectId
import db_connect
import json


def parse_json(data):
    return json.loads(json_util.dumps(data))


galleries = db_connect.connect_galleries()

app = Flask(__name__)
CORS(app)


@app.route('/list-galleries/', methods=['GET'])
def list_galleries():
    projection = {"_id": 1, "gallery_date": 1,
                  "gallery_name": 1, "thumbnail": 1, "thumbnail_x": 1, "thumbnail_y": 1}
    gallery_list = galleries.find({}, projection)
    return parse_json(gallery_list)


@app.route('/get-gallery/<string:gallery_id>/', methods=['GET'])
def get_gallery(gallery_id):
    _id = ObjectId(gallery_id)
    gallery = galleries.find_one({"_id": _id})
    return parse_json(gallery)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
