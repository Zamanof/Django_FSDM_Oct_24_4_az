from auth import hash_password, verify_password, create_access_token, decode_token


def main():
    password = "P@ss123456"
    hashed = hash_password(password)
    print(hashed)
    print(f"Verify OK: {verify_password(password, hashed)}")
    print(f"Verify BAD: {verify_password("password", hashed)}")

    token = create_access_token(sub="zamanov@itstep.org", role="admin")
    print(f"Token: {token}")
    print(f"Payload: {decode_token(token)}")


if __name__ == '__main__':
    main()