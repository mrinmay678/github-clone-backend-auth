from werkzeug.exceptions import HTTPException

def get_exc(error: Exception):
    details: str
    code: int

    _ERROR_CODES: dict = {
        "DoesNotExist": 404,
    }

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
                details= args[0]
                error_type = type(error).__name__
                if error_type in _ERROR_CODES:
                    code = _ERROR_CODES[error_type]
                else:
                    code = 500
            if isinstance(args[0], int):
                details = "Add Exception Message"
                code = args[0]
        else:
            details = "Internal Server Error"
            code = 500
    return details, code
