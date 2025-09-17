import json

from django.http import JsonResponse
from django.test import TestCase, RequestFactory
from django.utils import timezone

from .models import Question
from .views import experiment


class ExperimentViewTestCase(TestCase):
    def setUp(self):
        # Создаем фабрику запросов
        self.factory = RequestFactory()

        # Создаем тестовый вопрос
        self.question = Question.objects.create(
            id=1,
            question_text="Текст вопроса",
            pub_date=timezone.now()
        )

    def test_question_exists(self):
        # Создаем запрос
        request = self.factory.get(f'/experiment/{self.question.id}/')

        # Вызываем функцию
        response = experiment(request, self.question.id)

        # Проверяем статус ответа
        self.assertEqual(response.status_code, 200)

        # Проверяем содержимое JSON
        self.assertIsInstance(response, JsonResponse)
        data = json.loads(response.content)
        self.assertIn("id", data)
        self.assertEqual(data['id'], self.question.id)
        self.assertIn("question_text", data)
        self.assertEqual(data['question_text'], self.question.question_text)
        self.assertIn("pub_date", data)

    def test_question_not_found(self):
        # Создаем запрос с несуществующим ID
        request = self.factory.get('/experiment/99999/')

        # Вызываем функцию
        response = experiment(request, 99999)

        # Проверяем статус ответа
        self.assertEqual(response.status_code, 404)

        # Проверяем содержимое JSON
        self.assertIsInstance(response, JsonResponse)
        data = json.loads(response.content)
        self.assertEqual(data['error_message'], 'No such question_id: 99999')

    def test_invalid_question_id(self):
        # Создаем запрос с некорректным ID
        request = self.factory.get('/experiment/abc/')

        # Вызываем функцию
        response = experiment(request, 'abc')

        # Проверяем статус ответа
        self.assertEqual(response.status_code, 404)

        # Проверяем содержимое JSON
        self.assertIsInstance(response, JsonResponse)
        data = json.loads(response.content)
        self.assertEqual(data['error_message'], 'No such question_id: abc')
