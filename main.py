import re


"""
TODO: 
Шаблон для почты:
    локальная часть :
        dot ., provided that it is not the first or last character and provided also that it does not appear consecutively (e.g., John..Doe@example.com is not allowed)
    имя домена:
        hyphen -, provided that it is not the first or last character
    ПРОХОДЯТ ДАЖЕ НЕВАЛИДНЫЕ АДРЕСА
"""


names = """
И. И. Иванов
Дмитрий Ёж Дмитриевич 
Сухово-Кобылин Александр В. 
"""

emails = """
simple@example.com
very.common@example.com
disposable.style.email.with+symbol@example.com
another.email-with-hyphen@and.subdomains.example.com
fully-qualified-domain@example.com
user.name+tag+sorting@example.com
x@example.com
example-indeed@strange-example.com
test/test@test.com
admin@mailserver1
example@s.example
" "@example.org
"john..doe"@example.org
mailhost!username@example.org
user%example.com@example.org
user-@example.org
postmaster@[123.123.123.123]
postmaster@[IPv6:2001:0db8:85a3:0000:0000:8a2e:0370:7334]
"very.(),:;<>[]\".VERY.\"very@\\ \"very\".unusual"@strange.example.com
"""

phone_numbers = """
+981 982 912-81-12
+1 910 712-91-28
+9 713 891-19-12
+82 019 019-12-21
"""

text = """
Питонов Вася И.
+7 992 981-91-13
vasya.3.14tonov@yandex.ru
"""

phone_number_pattern = r"\+[0-9]+ [0-9]{3} [0-9]{3}-[0-9]{2}-[0-9]{2}"
name_pattern = r"[А-Яа-яёЁ\-.]+ [А-Яа-яёЁ.]+ [А-Яа-яЁё.]+"
email_pattern = r"[A-Za-z0-9!#$%&'*+-/=?^_`{|}~;:\"<>.()\[\]@\\ ]+@[A-Za-z0-9\[\].]+.[a-zA-Z0-9:.\[\]]+"


print(f"\nФИО: {re.findall(name_pattern, text)}\n")
print(f"Почтовые ящики: {re.findall(email_pattern, text)}\n")
print(f"Номера телефона: {re.findall(phone_number_pattern, text)}\n")
