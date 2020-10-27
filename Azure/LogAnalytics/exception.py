import json

class LogAnalyticsDataAccessException(Exception):
    inner = []
    msg = None
    code = None

    def json_default(self, o):
        return {
            "message": o.msg,
            "code": o.code,
            "inner": o.inner
        }

    def __init__(self, err):
        super()
        self.code = err.pop("code", None)
        self.msg = err.pop("message", None)
        self.inner= []
        if "details" in err:
            for detail in err["details"]:
                detail = LogAnalyticsDataAccessException(detail)
                self.inner.append(detail)
        if "innererror" in err:
             self.inner = LogAnalyticsDataAccessException(err["innererror"])

    def __str__(self):
        return json.dumps({
            "message": self.msg,
            "code": self.code,
            "inner": self.inner
        }, default=self.json_default)
