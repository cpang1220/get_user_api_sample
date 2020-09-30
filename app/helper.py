from flask import jsonify, make_response


def user_result_response(users):
    """
    Get the user results
    :return: Http Json response
    """
    return make_response(jsonify({
        'status': 'success',
        'users': users
    })), 200


def error_response(status, message, status_code):
    """
    :param status: Status message
    :param message: Response Message
    :param status_code: Http response code
    :return: Http Json response
    """
    return make_response(jsonify({
        'status': status,
        'message': message
    })), status_code


def error_obj(message, status_code):
    """
    :param message: Response Message
    :param status_code: Http response code
    :return: Http Json response
    """
    return jsonify({
        'message': message,
        'status_code': status_code,
    })
