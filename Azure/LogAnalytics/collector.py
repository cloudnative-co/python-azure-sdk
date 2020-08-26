import json
import urllib.request
import urllib.parse
import datetime
import hashlib
import hmac
import base64
import http
import datetime


class Collector(object):
    _shared_key: str = None
    _workspace_id: str = None
    _api_version: str = None
    _headers: dict = dict()
    _host = 'https://{}.ods.opinsights.azure.com/api/logs?api-version={}'

    def __init__(
        self, workspace_id: str = None, shared_key: str = None,
        api_version = '2016-04-01', client: object = None
    ) -> object:
        if client is not None:
            self._headers = client._headers
            self._shared_key = client._shared_key
            self._workspace_id = client._workspace_id
            self._api_version = client._api_version
        else:
            self._shared_key = shared_key
            self._workspace_id = workspace_id
            self._api_version = api_version
            self._host = self._host.format(workspace_id, api_version)


    def create_auth(self, length: str, pdate: str) -> str:
        sigs= "POST\n{}\napplication/json\nx-ms-date:{}\n/api/logs".format(
            str(length),pdate
        )
        bytes_to_hash  = sigs.encode('utf-8')
        decoded_key = base64.b64decode(self._shared_key)
        hmac_sha256_sigs = hmac.new(
                decoded_key,
                bytes_to_hash,
                digestmod=hashlib.sha256
        ).digest()
        encoded = base64.b64encode(hmac_sha256_sigs).decode('utf-8')
        authorization = "SharedKey {}:{}".format(self._workspace_id, encoded)
        return authorization

    def post(
        self, payload: dict, log_type: str,
        time_generated: str = None, azure_resource_id: str = None
    ) -> dict:
        payload = json.dumps(payload).encode('utf-8')
        p_date = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
        content_length = len(payload)
        signature = self.create_auth(content_length, p_date)
        headers = {
            "Content-Type": "application/json",
            "Authorization": signature,
            "Log-Type": log_type,
            "x-ms-date": p_date
        }
        if azure_resource_id is not None:
            headers["x-ms-AzureResourceId"] = azure_resource_id
        if time_generated is not None:
            headers["time-generated-field"] = time_generated
        args = {
            "url": self._host,
            "headers": headers,
            "method": "POST",
            "data": payload
        }
        req = urllib.request.Request(**args)
        try:
            with urllib.request.urlopen(req) as res:
                body = res.read().decode("utf-8")
                if body is "" or body is None:
                    return {}
                body = json.loads(body)
                return body
        except urllib.error.HTTPError as e:
            raise e
