import urllib.error
import json


class APIException(urllib.error.HTTPError):
    _code = None

    def __init__(self, e: urllib.error.HTTPError = None, message: str = None):
        super()
        if message is not None:
            self.state = False
            self.hdrs = None
            self.fp = None
            self.filename = None
            self.info = {}
            self.msg = message
            self.code = message
            return
        self.state = e.code
        self.hdrs = e.hdrs
        self.fp = e.fp
        self.filename = e.filename
        self.info = {}
        self.msg = ""
        self.code = ""
        body = e.read().decode("utf-8")
        try:
            body = json.loads(body)
            self.info = body.get("context_info", {})
            msg = body.get("message", None)
            desc = body.get("error_description", None)
            self.msg = msg or desc
            code = body.get("code", None)
            err = body.get("error", None)
            self.code = code or err
        except json.decoder.JSONDecodeError:
            pass

    def __str__(self):
        return json.dumps({
            "message": self.msg,
            "code": self.code,
            "status": self.state,
            "reason": self.reason,
            "url": self.filename,
            "info": self.info
        })
