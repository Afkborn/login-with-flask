import hashlib

def toMD5(string):
    return hashlib.md5(string.encode('utf-8')).hexdigest()