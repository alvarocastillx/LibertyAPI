from flask import Blueprint
from flask import request, jsonify
from config.mongo import mongo
from db import db
from datetime import datetime
from bson import json_util
import json


liberty = Blueprint('liberty', __name__)

@liberty.route('/post', methods=['POST'])
def post_message():
    try:
        request_data = request.get_json()
        receivedMessage = request_data.get('message',None)
        receivedName = request_data.get('name',None)

        messageToAdd = {
                'message':receivedMessage,
                'name':receivedName,
                'created_at': datetime.now()
        }
        
        mongo.db.liberty.insert_one(messageToAdd)
        
        return 'Mensaje enviado correctamente',200
    except:
        return "Incorrect payload",400
    
    
@liberty.route('/get', methods=['GET'])
def get_messages():
    #try:
        messageList = list()
        found = mongo.db.liberty.find()
        for i in found:
            messageList.append(i)

        print(messageList)
        return jsonify(list=json.loads(json_util.dumps(messageList)), status=200, mimetype='application/json')
    #except:
        return "Error al recuperar mensajes. Inténtelo de nuevo en otro momento", 400

