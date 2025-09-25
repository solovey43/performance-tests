from tkinter.font import names

from faker import Faker

fake=Faker('ru_RU')

user_data={
    "name": fake.name(),
    "email": fake.email(),
    "address": fake.address()
}

print(fake.name())
print(fake.address())
print(fake.email(domain="gmail.com"))