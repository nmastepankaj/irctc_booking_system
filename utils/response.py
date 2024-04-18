import logging

from rest_framework.response import Response

logger = logging.getLogger(__name__)


def success_response(status, msg, data, *args, **kwargs):
    response = {
        "status_code": status,
        "status": "success",
        "detail": msg,
        "data": data,
    }
    return Response(data=response, status=status)


def error_response(status, msg, data, *args, **kwargs):
    response = {
        "status_code": status,
        "status": "failure",
        "detail": msg,
        "data": data
    }
    caller_func = kwargs.get("caller_func", None)
    logger.warning(f"Caller Function: {caller_func} DATA: {data}")
    return Response(data=response, status=status)