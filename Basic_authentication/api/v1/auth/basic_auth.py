#!/usr/bin/env python3
""" BasicAuth module """
from .auth import Auth
import base64


class BasicAuth(Auth):
    """ Create basic authentication for requests """

    def extract_base64_authorization_header(self, authorization_header: str
                                            ) -> str:
        """ Returns the Base64 for @authorization_header """

        if authorization_header is None:
            return None

        if type(authorization_header) is not str:
            return None

        if not authorization_header.startswith('Basic '):
            return None

        base_this = authorization_header.split(' ')

        return base_this[1]
