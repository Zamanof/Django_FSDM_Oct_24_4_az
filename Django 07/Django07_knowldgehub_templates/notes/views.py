from django.middleware.csrf import get_token
from django.shortcuts import redirect, render
from django.utils.html import escape
from django.urls import reverse
from django.http import HttpResponse, HttpRequest

from . import data

def html_shell(title: str, body: str) -> str:
    safe_title = escape(title)

    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{safe_title}</title>

    <style>
        * {{
            box-sizing: border-box;
        }}

        body {{
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
            background: #f4f7fb;
            color: #1f2937;
            line-height: 1.6;
        }}

        .container {{
            max-width: 900px;
            margin: 0 auto;
            padding: 0 24px 40px;
        }}

        .nav {{
            background: #ffffff;
            border-bottom: 1px solid #e5e7eb;
            padding: 16px 24px;
            margin-bottom: 32px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
        }}

        .nav-inner {{
            max-width: 900px;
            margin: 0 auto;
            display: flex;
            gap: 12px;
        }}

        .nav a {{
            text-decoration: none;
            color: #374151;
            font-weight: 600;
            padding: 8px 14px;
            border-radius: 8px;
            transition: 0.2s;
        }}

        .nav a:hover {{
            background: #eaf2ff;
            color: #0b57d0;
        }}

        h1 {{
            color: #111827;
            margin-bottom: 20px;
        }}

        p {{
            margin: 10px 0;
        }}

        a {{
            color: #0b57d0;
            text-decoration: none;
        }}

        a:hover {{
            text-decoration: underline;
        }}

        .muted {{
            color: #6b7280;
            font-size: 0.95rem;
        }}

        code {{
            background: #eef2f7;
            color: #374151;
            padding: 3px 7px;
            border-radius: 5px;
            font-family: Consolas, monospace;
        }}

        ul.notes {{
            list-style: none;
            padding: 0;
            margin-top: 20px;
        }}

        ul.notes li {{
            background: #ffffff;
            padding: 16px 18px;
            margin-bottom: 12px;
            border: 1px solid #e5e7eb;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.04);
            transition: transform 0.15s, box-shadow 0.15s;
        }}

        ul.notes li:hover {{
            transform: translateY(-2px);
            box-shadow: 0 5px 14px rgba(0, 0, 0, 0.08);
        }}

        ul.notes li > a {{
            font-size: 1.05rem;
            font-weight: bold;
            margin-right: 8px;
        }}

        form {{
            background: #ffffff;
            padding: 28px;
            border-radius: 12px;
            border: 1px solid #e5e7eb;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
            max-width: 650px;
        }}

        form label {{
            display: block;
            font-weight: 600;
            margin-top: 16px;
            margin-bottom: 6px;
        }}

        form input[type="text"],
        form input:not([type]),
        form textarea {{
            display: block;
            width: 100%;
            padding: 10px 12px;
            border: 1px solid #d1d5db;
            border-radius: 7px;
            font-size: 1rem;
            font-family: inherit;
            outline: none;
            transition: border 0.2s, box-shadow 0.2s;
        }}

        form input:focus,
        form textarea:focus {{
            border-color: #0b57d0;
            box-shadow: 0 0 0 3px rgba(11, 87, 208, 0.12);
        }}

        textarea {{
            resize: vertical;
        }}

        button {{
            background: #0b57d0;
            color: white;
            border: none;
            padding: 10px 18px;
            border-radius: 7px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.2s, transform 0.1s;
        }}

        button:hover {{
            background: #0847ad;
        }}

        button:active {{
            transform: scale(0.98);
        }}

        .actions {{
            display: flex;
            gap: 10px;
            margin-top: 20px;
        }}

        .actions a {{
            display: inline-block;
            padding: 8px 14px;
            background: #ffffff;
            border: 1px solid #d1d5db;
            border-radius: 7px;
            text-decoration: none;
        }}

        .actions a:hover {{
            background: #f3f4f6;
            text-decoration: none;
        }}

        @media (max-width: 600px) {{
            .container {{
                padding-left: 15px;
                padding-right: 15px;
            }}

            .nav-inner {{
                flex-wrap: wrap;
            }}

            form {{
                padding: 20px;
            }}
        }}
    </style>
</head>

<body>

    <nav class="nav">
        <div class="nav-inner">
            <a href="{escape(reverse('home'))}">Home</a>
            <a href="{escape(reverse('about'))}">About</a>
            <a href="{escape(reverse('notes_list'))}">Notes</a>
        </div>
    </nav>

    <main class="container">
        {body}
    </main>

</body>
</html>
"""

# CSRF -> Cross-Site Request Forgery
def _csrf_field(request:HttpRequest)-> str:
    token = get_token(request)
    return f"<input type='hidden' name='csrfmiddlewaretoken' value='{escape(token)}'/input>"

def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'notes/home.html', {
        "page_title": "Knowledge Hub",
        'welcome_text': "Welcome to Knowledge Hub",
    }
                  )

def about(request: HttpRequest) -> HttpResponse:
    context = {
        "project_name": "Knowledge Hub Super Pupper",
        "author": "Nadir Zamanov",
    }
    return render(request, 'notes/about.html', context)

def notes_list(request: HttpRequest) -> HttpResponse:
    notes = data.list_notes()
    return render(request, 'notes/notes_list.html', {"notes": notes})


def note_detail(request: HttpRequest, note_id:int) -> HttpResponse:
    note = data.get_note(note_id)
    return render(request, 'notes/note_detail.html', {"note": note})


def note_create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        title = request.POST.get("title", "")
        note_body = request.POST.get("body", "")
        tag = request.POST.get("tag", "")
        category = request.POST.get("category", "")

        if not title.strip():
            err = "<p style='color:red;'>Title cannot be empty</p>"
        else:
            created = data.create_note(
                title=title,
                body=note_body,
                tag = tag or "misc",
                category = category or "general"
            )
            list_url = escape(reverse("notes_list"))
            return HttpResponse(
                f"""
                    <h1>Note created</h1>
                    <p>id = {created["id"]}, title={escape(created['title'])}</p>
                    <p><a href= "{list_url}">Return to list</a></p>
                """
            )
    else:
        err = ""

    action = escape(reverse("note_create"))
    form = (
        f"""
        <form method="POST" action="{action}">
            <h1> New note </h1>
            {err}
            {_csrf_field(request)}
            <p>
                <label>Title:</label>
                <p>
                    <input name="title" required>
                </p>  
            </p>
            <p>
                <label>Text:</label>
                <p>
                    <textarea name="body" rows=4></textarea>
                </p> 
            </p>
            
            <p>
                <label>Tag:</label>
                <p>
                    <input name="tag">
                </p> 
            </p>
            <p>
                <label>Category:</label>
                <p>
                    <input name="category">
                </p> 
            </p>
            
             <p>
                <button type="submit">Create</button>                
            </p>
        </form>            
        """
    )
    return HttpResponse(form)

def note_edit(request: HttpRequest, note_id: int) -> HttpResponse:
    note = data.get_note(note_id)
    if note is None:
        return HttpResponse(
            html_shell(
                "404 — Not Found",
                f"""
  <h1>Cannot edit</h1>
  <p class="muted">Note with id={escape(str(note_id))} does not exist.</p>
  <p><a href="{escape(reverse("notes_list"))}">Back to list</a></p>
""",
            ),
            status=404,
        )

    if request.method == "POST":
        title = request.POST.get("title", "")
        note_body = request.POST.get("body", "")
        tag = request.POST.get("tag", "")
        category = request.POST.get("category", "")

        if not title.strip():
            err = '<p class="muted" style="color:#b00020;">Title cannot be empty.</p>'
            note = {
                **note,
                "title": title,
                "body": note_body,
                "tag": tag,
                "category": category,
            }
        else:
            data.update_note(
                note_id,
                title=title,
                body=note_body,
                tag=tag or "misc",
                category=category or "general",
            )
            return redirect("note_detail", note_id=note_id)

    else:
        err = ""

    title_e = escape(note["title"])
    body_e = escape(note["body"])
    tag_e = escape(note["tag"])
    category_e = escape(note["category"])

    form = f"""
  <h1>Edit Note</h1>
  {err}
  <form method="post" action="{escape(reverse("note_edit", kwargs={"note_id": note_id}))}">
    {_csrf_field(request)}
    <label>Title<br /><input type="text" name="title" value="{title_e}" required /></label>
    <label>Text<br /><textarea name="body" rows="6">{body_e}</textarea></label>
    <label>Tag<br /><input type="text" name="tag" value="{tag_e}" /></label>
    <label>Category<br /><input type="text" name="category" value="{category_e}" /></label>
    <p style="margin-top:1rem;">
      <button type="submit">Save</button>
      <a class="muted" href="{escape(reverse("note_detail", kwargs={"note_id": note_id}))}">Cancel</a>
    </p>
  </form>
"""
    return HttpResponse(html_shell("Edit Note", form))


def note_delete(request: HttpRequest, note_id: int) -> HttpResponse:
    note = data.get_note(note_id)
    if note is None:
        return HttpResponse(
            html_shell(
                "404 — Not Found",
                f"""
  <h1>Cannot delete</h1>
  <p class="muted">Note with id={escape(str(note_id))} does not exist.</p>
  <p><a href="{escape(reverse("notes_list"))}">Back to list</a></p>
""",
            ),
            status=404,
        )

    if request.method == "POST":
        data.delete_note(note_id)
        return redirect("notes_list")

    body = f"""
  <h1>Delete Note?</h1>
  <p>{escape(note["title"])}</p>
  <form method="post" action="{escape(reverse("note_delete", kwargs={"note_id": note_id}))}">
    {_csrf_field(request)}
    <button type="submit">Yes, delete</button>
    <a class="muted" href="{escape(reverse("note_detail", kwargs={"note_id": note_id}))}">Cancel</a>
  </form>
"""
    return HttpResponse(html_shell("Delete Note", body))