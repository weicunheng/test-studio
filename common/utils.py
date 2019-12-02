# -*- coding: utf-8 -*-

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


def load_private_key(file):
    with open(file, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    return private_key


def load_public_key(file):
    with open(file, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    return public_key
