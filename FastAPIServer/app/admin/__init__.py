import jwt
if __name__ == '__main__':
    encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
    print(encoded_jwt)
    print("#####")
    print(jwt.decode(encoded_jwt, "secret", algorithms=["HS256"]))