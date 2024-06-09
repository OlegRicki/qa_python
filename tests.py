import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        quantity_books = collector.get_books_genre()
        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(quantity_books) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize('name', ['1', 'нйгщётжэцдсггмайиючвжжсуэаяотзщглеызеуэы'])
    def test_add_new_book_add_book_with_max_and_min_number_characters(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        quantity_books = collector.get_books_genre()
        assert len(quantity_books) == 1

    @pytest.mark.parametrize('name', ['Том и джерри'])
    def test_test_add_new_book_add_one_book_twice(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.add_new_book(name)
        quantity_books = collector.get_books_genre()
        assert len(quantity_books) == 1

    def test_set_book_genre_and_two_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre(name='Гордость и предубеждение и зомби', genre='Фантастика')
        collector.set_book_genre(name='Что делать, если ваш кот хочет вас убить', genre='Детективы')
        assert collector.get_book_genre(name='Гордость и предубеждение и зомби') == 'Фантастика'
        assert collector.get_book_genre(name='Что делать, если ваш кот хочет вас убить') == 'Детективы'

    @pytest.mark.parametrize('name, genre', [['Том и Джерри', 'Комедийный мульт-сериал'], ['Гарри Поттер', '123']])
    def test_set_book_genre_when_genre_not_listed(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name=name, genre=genre)
        assert collector.get_book_genre(name=name) == ''

    @pytest.mark.parametrize('name, genre', [['Том и Джерри', 'Комедии'], ['Гарри Поттер', 'Фантастика']])
    def test_get_book_genre_when_one_book(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name=name, genre=genre)
        assert collector.get_book_genre(name=name) == genre

    def test_get_books_with_specific_genre_with_genre_horror(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre(name='Гордость и предубеждение и зомби', genre='Ужасы')
        collector.set_book_genre(name='Что делать, если ваш кот хочет вас убить', genre='Ужасы')
        check_list = ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']
        assert collector.get_books_with_specific_genre(genre='Ужасы') == check_list

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Том и Джерри')
        collector.set_book_genre(name='Гордость и предубеждение и зомби', genre='Ужасы')
        collector.set_book_genre(name='Том и Джерри', genre='Мультфильмы')
        check_list = ['Том и Джерри']
        assert collector.get_books_for_children() == check_list

    def test_add_book_in_favorites_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Том и Джерри')
        collector.add_book_in_favorites(name='Том и Джерри')
        assert collector.get_list_of_favorites_books() == ['Том и Джерри']

    @pytest.mark.parametrize('name', ['Том и джерри'])
    def test_add_book_in_favorites_one_book_twice(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name)
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_all_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites(name='Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']
        collector.delete_book_from_favorites(name='Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == []
