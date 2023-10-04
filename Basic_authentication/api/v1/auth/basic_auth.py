#!/usr/bin/env python3
""" BasicAuth module """
from .auth import Auth
from base64 import b64decode
from models.user import User
from typing import TypeVar


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """ Decode the base64 part of @base64_authorization_header """

        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None

        try:
            encode = base64_authorization_header.encode('utf-8')
            decode = b64decode(encode).decode('utf*8')
            return decode
        except Exception:
            return None

    def extract_user_credentials(
                                self, decoded_base64_authorization_header: str
                                ) -> (str, str):
        """
        returns the use email and password
        from base64 decoded values
        """

        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None

        decode_this = decoded_base64_authorization_header.split(':')
        return decode_this[0], decode_this[1]

    def user_object_from_credentials(
                                    self, user_email: str,
                                    user_pwd: str
                                    ) -> TypeVar('User'):
        """
        returns User instance based on email and password.
        """

        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None

        try:
            users = User.search({"email": user_email})
            for item in users:
                if item.is_valid_password(user_pwd):
                    return item
        except Exception:
            return None
