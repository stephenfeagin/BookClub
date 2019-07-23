from django.test import TestCase

from books.models import Author, Book, Genre


class TestAuthorModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(given_name="Agatha", last_name="Christie",
                              date_of_birth="1890-09-15", date_of_death="1976-01-12")
        Author.objects.create(given_name="Noam", last_name="Chomsky",
                              date_of_birth="1928-12-07")
        Author.objects.create(last_name="Homer")

    def test_given_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field("given_name").max_length
        self.assertEqual(max_length, 100)

    def test_last_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field("last_name").max_length
        self.assertEqual(max_length, 100)

    def test_object_name_with_full_details(self):
        author = Author.objects.get(id=1)
        string = "Christie, Agatha (1890-1976)"
        self.assertEqual(str(author), string)

    def test_object_name_with_no_death_date(self):
        author = Author.objects.get(id=2)
        string = "Chomsky, Noam (1928-)"
        self.assertEqual(str(author), string)

    def test_object_name_with_only_last_name(self):
        author = Author.objects.get(id=3)
        string = "Homer"
        self.assertEqual(str(author), string)


class TestBookModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        murder = Book(title="Murder on the Orient Express", subtitle="A Hercule Poirot Mystery")
        murder.save()
        murder.author.create(given_name="Agatha", last_name="Christie",
                             date_of_birth="1890-09-15", date_of_death="1976-01-12")
        murder.genre.create(name="Mystery")
        murder.save()

        omens = Book(title="Good Omens",
                     subtitle="The Nice and Accurate Prophecies of Agnes Nutter, Witch",
                     pub_year=1990)
        omens.save()
        omens.author.create(given_name="Terry", last_name="Pratchett",
                            date_of_birth="1948-04-28", date_of_death="2015-03-12")
        omens.author.create(given_name="Neil", last_name="Gaiman", date_of_birth="1960-11-10")
        omens.genre.create(name="Science Fiction")
        omens.genre.create(name="Fantasy")
        omens.save()

    def test_name_without_pub_year(self):
        murder = Book.objects.get(title__exact="Murder on the Orient Express")
        self.assertEqual(str(murder), "Murder on the Orient Express")

    def test_name_with_pub_year(self):
        murder = Book.objects.get(title__exact="Murder on the Orient Express")
        murder.pub_year = 1934
        self.assertEqual(str(murder), "Murder on the Orient Express (1934)")

    def test_single_author(self):
        murder = Book.objects.get(title__exact="Murder on the Orient Express")
        christie = Author.objects.get(last_name__exact="Christie")
        self.assertEqual(murder.author.first(), christie)

    def test_verbose_title_without_year(self):
        murder = Book.objects.get(title__exact="Murder on the Orient Express")
        verbose_title = "Murder on the Orient Express: A Hercule Poirot Mystery"
        self.assertEqual(murder.verbose_title, verbose_title)

    def test_verbose_title_with_year(self):
        omens = Book.objects.get(title__exact="Good Omens")
        verbose_title = "Good Omens: The Nice and Accurate Prophecies of Agnes Nutter, Witch (1990)"
        self.assertEqual(omens.verbose_title, verbose_title)

    def test_multiple_authors(self):
        omens = Book.objects.get(title__exact="Good Omens")
        authors = [au for au in omens.author.all()]
        gaiman = Author.objects.get(last_name__exact="Gaiman")
        pratchett = Author.objects.get(last_name__exact="Pratchett")
        self.assertEqual(authors, [gaiman, pratchett])

    def test_multiple_genres(self):
        omens = Book.objects.get(title__exact="Good Omens")
        genres = [genre for genre in omens.genre.all()]
        scifi = Genre.objects.get(name__exact="Science Fiction")
        fantasy = Genre.objects.get(name__exact="Fantasy")
        self.assertEqual(genres, [scifi, fantasy])


class TestGenreModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(name="Mystery")

    def test_genre_max_length(self):
        genre = Genre.objects.first()
        max_len = genre._meta.get_field("name").max_length
        self.assertEqual(max_len, 100)
