#!/usr/bin/python3
"""
Main Documentation
"""


def validUTF8(data):
    """ Valid UTF Function code Documentation"""
    cleanByte = [sData & 0b11111111 for sData in data]
    byte = bytes(cleanByte)
    try:
        byte.decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False
