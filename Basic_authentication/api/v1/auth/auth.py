#!/usr/bin/env python3
""" Module for Auth class """
from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Do something
        Returns:
          False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Do something
        Returns:
          None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Do something
        Returns:
          None
        """
        return None
