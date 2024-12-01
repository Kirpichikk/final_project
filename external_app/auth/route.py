from flask import Blueprint, request, jsonify

from auth.model import valid_authorization_request, decode_basic_authorization, find_userr

blueprint_auth = Blueprint('blueprint_auth', __name__)


@blueprint_auth.route('/find-user', methods=['GET'])
def find_user():
    if not valid_authorization_request(request):
        return jsonify({'status': 400, 'message': 'Bad request'})

    try:
        login, password = decode_basic_authorization(request)
    except Exception as e:
        return jsonify({'status': 400, 'message': f'Bad request. {str(e)}'})
    else:
        user = find_userr(login, password)
        if not user:
            return jsonify({'status': 404, 'message': 'user not found'})
        return jsonify({'status': 200, 'message': 'OK', 'user': user[0]})
