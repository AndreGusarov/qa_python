from gc import collect
from ipaddress import collapse_addresses
from tkinter.messagebox import NO
from main import BooksCollector
import pytest


class TestBooksCollector:

    #Тест для конструктора __init__пше
    def test_all_genres_is_true(self):
        collector = BooksCollector()
        
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    #Проверка длины списка книг
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        
        assert len(collector.get_books_genre()) == 2

    #Проверка добавления  и получения жанра книги
    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Три поросенка')
        collector.set_book_genre('Три поросенка','Мультфильмы')
        
        assert collector.get_book_genre('Три поросенка') == 'Мультфильмы'

    #Проверка получения книги без жанра
    def test_get_book_with_empty_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Полет над гнездом кукушки')
        
        assert collector.get_book_genre('Полет над гнездом кукушки') == ''

    #Проверка вывода книг по жанру
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга_1')
        collector.set_book_genre('Книга_1', 'Фантастика')
        collector.add_new_book('Книга_2')
        collector.set_book_genre('Книга_2', 'Комедии')
        collector.add_new_book('Книга_3')
        collector.set_book_genre('Книга_3', 'Фантастика')
        
        assert collector.get_books_with_specific_genre('Фантастика') == ['Книга_1', 'Книга_3']

    #Проверка получения словаря
    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга_1')
        collector.set_book_genre('Книга_1', 'Фантастика')
        collector.add_new_book('Книга_2')
        collector.set_book_genre('Книга_2', 'Комедии')
        
        assert collector.get_books_genre() == {
        'Книга_1': 'Фантастика',
        'Книга_2': 'Комедии'
    }

    #Проверка книг, подходящих детям
    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Книга_1')
        collector.set_book_genre('Книга_1', 'Фантастика')
        collector.add_new_book('Книга_2')
        collector.set_book_genre('Книга_2', 'Ужасы')

        assert collector.get_books_for_children() == ['Книга_1']

    #Проверка добавления книги в Избранное и просмотр списка
    @pytest.mark.parametrize('book_title', [
        'Книга_1',
        'Книга_2',
        'Книга_3'
])
    def test_add_multiple_books_in_favorites(self, book_title):
        collector = BooksCollector()
        collector.add_new_book(book_title)
        collector.set_book_genre(book_title, 'Фантастика')
        collector.add_book_in_favorites(book_title)
        assert book_title in collector.get_list_of_favorites_books()
    
    #Проверка добавления книги, которой нет в books_genre
    def test_add_book_not_in_dict_in_favorites(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Книга_1')
        
        assert collector.get_list_of_favorites_books() ==  []

    #Проверка удаления книги из Избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга_1')
        collector.add_book_in_favorites('Книга_1')
        collector.delete_book_from_favorites('Книга_1')

        assert collector.get_list_of_favorites_books() == []
