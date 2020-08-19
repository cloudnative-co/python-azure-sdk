# -*- coding: utf-8 -*-
# import module snippets
import datetime
import http.cookiejar
import io
import json
import os
import sys
import urllib.request
import urllib.parse

from .exception import APIException


class Base(object):
    __client: urllib.request.OpenerDirector = None
    __cookie: http.cookiejar.CookieJar = None
    __lasturl: str = None
    __header: dict = dict()
    __tenant: str = None
    __client_id: str = None
    __client_secret: str = None
    __expires_on: dict = dict()
    __tokens: dict = dict()
    schema = "https"
    host = "management.core.windows.net"

    def __init__(
        self,
        app_id: str = None,
        tenant: str = None,
        password: str = None,
        client: object = None,
    ):
        if client is not None:
            self.__client = client.__client
            self.__header = client.__header
            self.__cookie = client.__cookie
            self.__tenant = client.__tenant
            self.__client_id = client.__client_id
            self.__client_secret = client.__client_secret
            self.__expires_on = client.__expires_on
        else:
            self.__tenant = tenant
            self.__client_id = app_id
            self.__client_secret = password
            self.__cookie = http.cookiejar.CookieJar()
            self.__client = urllib.request.build_opener(
                urllib.request.HTTPCookieProcessor(self.__cookie)
            )
            urllib.request.install_opener(self.__client)

    def autholization(self, resource):

        if resource in self.__expires_on:
            expire_on = self.__expires_on[resource]
            now = datetime.datetime.now()
            if expire_on > now:
                self.__header["Authorization"] = self.__tokens[resource]
                self.__header["Content-Type"] = "application/json"
                return

        url = "https://login.microsoftonline.com/{}/oauth2/token"
        url = url.format(self.__tenant)

        payload = {
            "grant_type": "client_credentials",
            "resource": resource,
            "client_id": self.__client_id,
            "client_secret": self.__client_secret,
        }
        boundary = '----------lImIt_of_THE_fwIle_eW_$'
        charset = "utf-8"
        bf = io.BytesIO()
        for key, value in payload.items():
            bf.write(('--%s\r\n' % boundary).encode(charset))
            bf.write((
                'Content-Disposition: form-data; name="%s"' % key
            ).encode(charset))
            bf.write(b'\r\n\r\n')
            value = value.encode(charset)
            bf.write(value)
            bf.write(b'\r\n')
        bf.write(('--' + boundary + '--\r\n\r\n').encode(charset))
        bf = bf.getvalue()
        content_type = 'multipart/form-data; boundary=%s' % boundary

        args = {
            "url": url,
            "method": "POST",
            "data": bf,
            "headers": {
                "Content-Type": content_type
            }
        }
        req = urllib.request.Request(**args)
        try:
            with self.__client.open(req) as res:
                body = res.read()
                body = body.decode("utf-8")
                body = json.loads(body)
                auth = "{token_type} {access_token}".format(**body)
                self.__tokens[resource] = auth
                expires_on = int(body["expires_on"])
                self.__expires_on[resource] = datetime.datetime.fromtimestamp(expires_on)
                self.__header["Authorization"] = auth
                self.__header["Content-Type"] = "application/json"
        except urllib.error.HTTPError as e:
            raise e

    def http_request(
        self,
        method: str, path: str = None, headers: dict = {},
        query: dict = None, payload: dict = None, url: str = None,
        files: dict = None, is_read: bool = True, with_header: bool = False,
        charset: str = "utf-8"
    ):

        if url is None:
            url = "{}://{}/{}".format(self.schema, self.host, path)
        if query is None:
            query = dict()
        if "?" in url:
            q = url.split("?")
            if query is None:
                query = dict()
            for q1 in q[1].split("&"):
                q1 = q1.split("=")
                query[q1[0]] = q1[1]
        if method == "get":
            query["token"] = self.token
        elif method == "post":
            headers["Authorization"] = "Bearer {}".format(self.token)
        if len(query) > 0:
            url = "{}?{}".format(url, urllib.parse.urlencode(query))

        parsed_url = urllib.parse.urlparse(url)
        resource = "{}://{}".format(parsed_url.scheme, parsed_url.netloc)
        self.autholization(resource)

        args = {
            "url": url,
            "method": method.upper()
        }
        ctype = headers.get('Content-Type', None)
        if ctype == "multipart/form-data":
            ctype, payload = self.encode_multipart(payload, files, charset)
            headers["Content-Type"] = ctype
            args["data"] = payload
        elif ctype == "application/octet-stream":
            args["data"] = payload
        elif payload is not None:
            try:
                payload = json.dumps(payload).encode('utf-8')
                headers["Content-Type"] = "application/json; charset=UTF-8"
            except TypeError as e:
                try:
                    payload = urllib.parse.urlencode(payload).encode()
                except Exception as e:
                    pass
            args["data"] = payload
        else:
            payload = b""
        args["headers"] = dict(self.__header, **headers)
        req = urllib.request.Request(**args)
        try:
            with self.__client.open(req) as res:
                head = dict(res.info())
                if is_read:
                    body = res.read()
                    try:
                        body = body.decode("utf-8")
                    except UnicodeDecodeError:
                        if with_header:
                            return body, head
                        return body
                    try:
                        body = json.loads(body)
                        if with_header:
                            return body, head
                        return body
                    except Exception as e:
                        if with_header:
                            return body, head
                        return body
                return res
        except urllib.error.HTTPError as e:
            raise APIException(e)
