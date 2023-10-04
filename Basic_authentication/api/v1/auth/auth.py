#!/usr/bin/env python3
""" Module for Auth class """
from flask import request
from typing import List, TypeVar


class Auth:
    """ Class for manage the API authentication.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Returns a bool saying if path require auth
        """
        if path is None:
            return True

        if excluded_paths is None or excluded_paths == []:
            return True

        if not path.endswith('/'):
            path = f"{path}/"

        for item in excluded_paths:
            if not item.endswith('/'):
                item = f"{item}/"

        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ Do something
        Returns:
          None
        """
        if request is None:
            return None

        if not request.headers.get('Authorization'):
            return None
        else:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Do something
        Returns:
          None
        """
        return None


class BasicAuth(Auth):
    """ Empty fot the moment """
