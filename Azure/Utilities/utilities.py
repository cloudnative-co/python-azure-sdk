import json
import datetime
import inspect
from .maps import Maps

def normalization(args):
    result = {}
    for ky, value in args.items():
        if ky == "self":
            continue
        if value is None:
            value = "null"
        elif isinstance(value, str):
            value = '"{}"'.format(value)
        elif isinstance(value, datetime.datetime):
            value = value.timestamp()
        elif isinstance(args[ky], list):
            value = ",".join(value)
        result[ky] = value
    return result


def remove_none(params: dict):
    result = {}
    for k, v in params.items():
        if v is None:
            continue
        if isinstance(v, dict):
           v = remove_none(v)
           if v is None:
               continue
        elif isinstance(v, list):
            tmp_lst = []
            for v1 in v:
                if isinstance(v1, dict):
                    v1 = remove_none(v1)
                    if v1 is None:
                        continue
                tmp_lst.append(v1)
            if len(tmp_lst) == 0:
                continue
            v = tmp_lst
        result[k] = v
    if len(result) == 0:
        return None
    return result


def request_parameter(args: dict):
    m_name = args["self"].__module__
    c_name = "{}.{}".format(m_name, args["self"].__class__.__name__)
    m_name = inspect.stack()[1].function
    if c_name not in Maps:
        return None
    if m_name not in Maps[c_name]:
        return None
    req_map = Maps[c_name][m_name]
    method = req_map["method"]
    url = req_map["url"]
    url = url.format(**args)
    params = normalization(args)
    query = None
    payload = None
    if "query" in req_map:
        query = Maps[c_name][m_name]["query"]
        query = query.format(**params)
        query = json.loads(query)
        query = remove_none(query)
    return {
        "method": method,
        "url": url,
        "query": query,
        "payload": payload
    }



def get_arguments(args: dict, keys: list = None, ignores: list = None):
    def snake_to_kebab(key):
        ret = []
        for key in key.split("_"):
            ret.append(key.capitalize())
        return "-".join(ret)

    ret = {}
    for ky in args:
        if ky == "self":
            continue
        if keys is not None:
            if ky not in keys:
                continue
        if ignores is not None:
            if ky in ignores:
                continue
        if args[ky] is None:
            continue
        if args[ky] is not None:
            if isinstance(args[ky], datetime.datetime):
                ret[ky] = args[ky].timestamp()
            elif isinstance(args[ky], list):
                ret[ky] = ",".join(args[ky])
            else:
                ret[ky] = args[ky]
    return ret


def parse_values(value):
    if value is None:
        value = "null"
    elif isinstance(value, bool):
        value = "true" if value else "false"
    elif isinstance(value, str):
        value = '"{}"'.format(value)
    elif isinstance(value, datetime.datetime):
        value = value.timestamp()
        value = '"{}"'.format(value)
    elif isinstance(value, dict):
        value = json.dumps(value)
    elif isinstance(value, list):
        if len(value) == 1:
            value = parse_values(value[0])
        else:
            try:
                value = json.dumps(value)
            except TypeError as e:
                value = "null"
    return value


def formation(f):
    def remove_none(params: dict):
        result = {}
        for k in params:
            v = params.get(k, None)
            if v is None:
                continue
            if isinstance(v, dict):
                v = remove_none(v)
                if v is None:
                    continue
            if isinstance(v, list):
                tmp_lst = []
                for v1 in v:
                    if isinstance(v1, dict):
                        v1 = remove_none(v1)
                        if v1 is None:
                            continue
                    tmp_lst.append(v1)
                if len(tmp_lst) == 0:
                    continue
                v = tmp_lst
            result[k] = v
        if len(result) == 0:
            return None
        return result

    def wrapper(*args, **kwargs):
        if "payload" in kwargs:
            return f(*args, **kwargs)
        m = inspect.getmembers(f)
        a, member = m[0]
        lst_args = list(member.keys())
        _kwargs = {}
        for arg_name in lst_args:
            arg_value = "null"
            if arg_name in kwargs:
                arg_value = kwargs.get(arg_name)
                arg_value = parse_values(arg_value)
            _kwargs[arg_name] = arg_value
        method_name = f.__qualname__
        maps = Maps[method_name]
        str_params = maps.format(**_kwargs)
        payload = json.loads(str_params)
        payload = remove_none(payload)
        kwargs["payload"] = payload
        return f(*args, **kwargs)
    return wrapper
