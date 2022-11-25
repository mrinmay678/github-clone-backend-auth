class Response:

    @classmethod
    def success(cls, data: dict = None):
        res: dict = {
            "status": True,
            "message": "Success"
        }
        if data:
            res["data"] = data
        return res

    @classmethod
    def error(cls, message: str, code: int):
        return {
            "status": False,
            "message": message
        }, code
