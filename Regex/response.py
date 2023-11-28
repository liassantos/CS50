from validator_collection import validators, errors

def main():
    print(response(input("What's your email address? ")))

def response(email):
    try:
        valid_email_address = validators.email(email)
        return "Valid"
    except errors.EmptyValueError:
        return "Invalid"
    except errors.InvalidEmailError:
        return "Invalid"


if __name__ == "__main__":
    main()
