from django.core.management.base import BaseCommand
from blog.models import User, Post
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Добавляет тестовые данные на тему "Задания/Задачи"'

    def handle(self, *args, **kwargs):
        # Создание тестовых пользователей
        taskmaster = User.objects.create(
            username='taskmaster',
            email='taskmaster@example.com',
            password=make_password('password123'),
            phone='1111111111'
        )
        taskdoer = User.objects.create(
            username='taskdoer',
            email='taskdoer@example.com',
            password=make_password('password123'),
            phone='2222222222'
        )
        projectmanager = User.objects.create(
            username='projectmanager',
            email='pm@example.com',
            password=make_password('password123'),
            phone='3333333333'
        )
        developer = User.objects.create(
            username='developer',
            email='dev@example.com',
            password=make_password('password123'),
            phone='4444444444'
        )

        # Создание тестовых заданий
        Post.objects.create(
            title='Написать отчет',
            content='Подготовить подробный отчет о проделанной работе за месяц.',
            author=taskmaster
        )
        Post.objects.create(
            title='Провести встречу',
            content='Организовать и провести встречу с командой для обсуждения текущих задач.',
            author=taskmaster
        )
        Post.objects.create(
            title='Изучить Django',
            content='Пройти обучающий курс по Django и создать тестовый проект.',
            author=taskdoer
        )
        Post.objects.create(
            title='Оптимизировать базу данных',
            content='Провести анализ и оптимизацию запросов к базе данных.',
            author=taskdoer
        )
        Post.objects.create(
            title='Разработать API',
            content='Создать REST API для управления задачами.',
            author=projectmanager
        )
        Post.objects.create(
            title='Протестировать приложение',
            content='Написать unit-тесты для основного функционала приложения.',
            author=developer
        )
        Post.objects.create(
            title='Обновить документацию',
            content='Дописать и обновить документацию проекта.',
            author=projectmanager
        )
        Post.objects.create(
            title='Провести код-ревью',
            content='Провести ревью кода для последнего пул-реквеста.',
            author=developer
        )

        self.stdout.write(self.style.SUCCESS('Тестовые данные успешно добавлены!'))