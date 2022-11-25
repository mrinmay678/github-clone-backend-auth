from flask import request

def _check(params: dict, fields: list, extras: list = None, extra_fields: dict = None):
    for field in fields:
        if field not in params.keys():
            raise Exception("Required Fields are missing", 400)

    if extras and extra_fields:
        for field in extras:
            if field not in extra_fields.keys():
                raise Exception("Required Fields are missing", 400)


def check_fields(fields: list, extras: list=None, *args, **kwargs):
    """
    This Decorator is used to check required fields are present in request or not
    """

    # Check Method is present in request or not
    if method:=request.method:

        # Checks Query Params for GET and DELETE methods
        if method=="GET" or method=="get" or method=="delete" or method=="DELETE":
            if extras:
                _check(request.args, fields, extras, request.json)
            else:
                _check(request.args, fields)

        # Checks Data for POST and PUT methods
        elif method=="POST" or method=="post" or method=="put" or method=="PUT":
            if extras:
                _check(request.json, fields, extras, request.args)
            else:
                _check(request.json, fields, extras)

    def inner(func):
        func(*args, **kwargs)
    return inner