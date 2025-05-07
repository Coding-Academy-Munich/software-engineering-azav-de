valid_mail_addresses = [
    "joe@example.com",
    "jack@example.com",
    "jill@example.com",
]


def read_email_from_user():
    email = input("Enter your email address: ")
    if email not in valid_mail_addresses:
        raise ValueError("Invalid email address")
    return email


if __name__ == "__main__":
    mail = read_email_from_user()
    print(f"Accepted email address: {mail}")
