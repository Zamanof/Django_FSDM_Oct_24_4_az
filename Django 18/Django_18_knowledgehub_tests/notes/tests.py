from django.contrib.auth.models import User
from django.test import TestCase, SimpleTestCase
from django.urls import reverse

from notes.forms import NoteForm
from notes.models import Note


class NoteFormTests(SimpleTestCase):
    def test_valid_data_passes_validation(self):
        # arrange
        form = NoteForm(data={
            "title": "First Note",
            "content": "First Note content",
        })

        # Act       - form.isValid()
        # Assert    assertTrue()
        self.assertTrue(form.is_valid())

    def test_empty_title_id_rejected(self):
        # arrange
        form = NoteForm(data={
            "title": "",
            "content": "First Note content",
        })

        # Act       - form.isValid()
        # Assert    assertTrue()
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)



class NoteCreateAccessTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testuser",
            password="P@ss123456",
        )
        cls.create_url = reverse("notes:note_create")
        cls.login_url = reverse("accounts:login")

    def test_guest_is_redirected_to_login(self):
        response = self.client.get(self.create_url)

        self.assertRedirects(response, f"{self.login_url}?next={self.create_url}")


    def test_authenticated_user_can_open_create(self):
        self.client.force_login(self.user)

        response = self.client.get(self.create_url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Create Note")
        self.assertTemplateUsed(response, "notes/note_create.html")



class NoteCreatePostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create_user(
            username="testuser",
            password="P@ss123456",
        )

    def setUp(self):
        self.client.force_login(self.author)


    def test_post_creates_note_for_current_user(self):
        before = Note.objects.count()

        response = self.client.post(
            reverse("notes:note_create"),
            data={
                "title": "New Note",
                "content": "Lorem ipsum dolor sit amet.",
            }
        )

        self.assertEqual(Note.objects.count(), before + 1)
        note = Note.objects.get(title="New Note")
        self.assertEqual(note.content, "Lorem ipsum dolor sit amet.")
        self.assertEqual(note.author, self.author)
        self.assertRedirects(
            response,
            reverse("notes:note_detail", kwargs={"note_id": note.id}),
        )


class NoteOwnerShipTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create_user(
            username="testuser",
            password="P@ss123456",
        )

        cls.intruder = User.objects.create_user(
            username="intruder",
            password="Password!",
        )
        cls.note = Note.objects.create(
            title="New Note",
            content="Lorem ipsum dolor sit amet.",
            author=cls.author,
        )

    def test_author_can_edit_own_note(self):
        self.client.force_login(self.author)
        response = self.client.post(
            reverse("notes:note_edit", kwargs={"note_id": self.note.id}),
            {
                "title": "Edited Note",
                "content": "Lorem ipsum dolor sit amet.",
            }
        )

        self.assertRedirects(
            response,
            reverse("notes:note_detail", kwargs={"note_id": self.note.id}),
        )
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Edited Note")


    def test_other_user_cannot_edit_note(self):
        original_title = self.note.title
        original_content = self.note.content
        self.client.force_login(self.intruder)
        response = self.client.post(
            reverse("notes:note_edit", kwargs={"note_id": self.note.id}),
            {
                "title": "Intruder Note",
                "content": "Intruder content",
            }
        )

        self.assertEqual(response.status_code, 403)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, original_title)
        self.assertEqual(self.note.content, original_content)