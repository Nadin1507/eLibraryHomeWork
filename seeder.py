# import os
# import django
# from faker import Faker
# from library.models import Book

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eLibrary.settings')
django.setup()

def populate(n=50):
    faker = Faker()
    for _ in range(n):
        title = faker.sentence(nb_words=3)
        author = faker.name()
        published_date = faker.date()
        isbn = faker.isbn13()

        Book.objects.create(title=title, author=author, published_date=published_date, isbn=isbn)

if __name__ == '__main__':
    populate(50)  # Создание 50 книг