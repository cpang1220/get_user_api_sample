from flask import Flask, request
import app.search_users as search_users
import app.const as const
from app import app
from app.helper import user_result_response, error_response


@app.route('/users/live/city', methods=['GET'])
def list_user_by_live_place():
    user_result = search_users.get_user_data_by_live_place()
    if not const.HTTP_ERROR:
        return user_result_response(user_result)
    else:
        return error_response('HTTP error', user_result['message'], user_result['status_code'])


@app.route('/users/current/vicinity', methods=['GET'])
def list_user_by_vicinity():
    user_result = search_users.get_user_data_by_vicinity()
    if not const.HTTP_ERROR:
        return user_result_response(user_result)
    else:
        return error_response('HTTP error', user_result['message'], user_result['status_code'])
