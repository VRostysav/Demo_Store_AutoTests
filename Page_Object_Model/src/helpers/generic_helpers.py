import random
import string


def generate_random_email_and_password(domain=None, email_prefix=None):
    if not domain:
        domain = 'supersqa.com'
    if not email_prefix:
        email_prefix = 'testuser'

    random_email_string_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))

    email = email_prefix + '_' + random_string + '@' + domain
    random_password_length = 12
    password = ''.join(random.choices(string.ascii_letters, k=random_password_length))

    random_info = {"email": email, 'password': password}
    return random_info
