from typing import Optional

from rest_framework.response import Response
from rest_framework.views import exception_handler


def drf_exception_handler(exc, context) -> Optional[Response]:
    return exception_handler(exc, context)
