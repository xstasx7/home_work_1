import re

VALID_EMAIL = re.compile(r'^\w*@\w*\.(com|ru|bk)$')


def email(any_email_address):
    result_dict = {}

    try:
        if VALID_EMAIL.match(any_email_address):
            result = re.split(r'@', any_email_address)
            result_dict['username'] = result[0]
            result_dict['domain'] = result[1]
        else:
            raise ValueError

    except ValueError:
        return print(f'ValueError: wrong email: {any_email_address}')

    return result_dict


if __name__ == '__main__':
    print(email(input('Введите email адрес: ')))


