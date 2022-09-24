from werkzeug.exceptions import HTTPException


def get_exc(error: Exception):
    if isinstance(error, HTTPException):
        details = getattr(error, "description")
        code = error.code
    else:
        args = error.args
        if len(args) == 2:
            if isinstance(args[0], str) and isinstance(args[1], int):
                details = args[0]
                code = args[1]
            elif isinstance(args[0], int) and isinstance(args[1], str):
                details = args[1]
                code = args[0]
        elif len(args) == 1:
            if isinstance(args[0], str):
                details = args[0]
                code = 500
            if isinstance(args[0], int):
                details = "Add Exception Message"
                code = args[0]
        else:
            details = "Internal Server Error"
            code = 500
    return details, code
