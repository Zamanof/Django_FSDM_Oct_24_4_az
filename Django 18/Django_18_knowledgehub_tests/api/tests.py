from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from notes.models import Note


class NoteApiOwnershipTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create_user(
            username='testuser',
            password='P@ss123456')
        cls.intruder = User.objects.create_user(
            username='intruder',
            password='Password!'
        )
        cls.note = Note.objects.create(
            title='Test Note',
            content='Test Content',
            author=cls.author,
            status='published'
        )

    def test_other_user_cannot_patch_note_via_api(self):
        self.client.force_authenticate(user=self.intruder)

        response = self.client.patch(
            reverse('note-detail', args=[self.note.pk]),
            {
                "title": "Intruder Note",
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Test Note')