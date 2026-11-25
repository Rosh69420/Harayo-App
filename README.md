# Harayo App – Lost and Found Website

A beginner-friendly BCA 4th Semester project built with Python, Django, HTML, CSS, JavaScript, and SQLite.

## Features
- User signup, login, and logout
- Create Lost and Found posts with optional photos
- Item categories and search/filter options
- Item detail pages
- Public messages on item posts
- Personal dashboard to manage your posts
- Mark your own posts as resolved or reopen them
- Django admin panel
- Responsive layout for desktop and mobile

## Run on Windows CMD
Open CMD in the folder containing `manage.py`, then run:

```cmd
python -m venv newenv
newenv\Scripts\activate.bat
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

To create an admin account:
```cmd
python manage.py createsuperuser
```
Then visit http://127.0.0.1:8000/admin/.

## Important note about messages
Messages on item detail pages are public. Do not post phone numbers, home addresses, passwords, or other private information. This feature is a simple public message board, not private messaging.

See `PROJECT_DOCUMENTATION.md` for the project report outline, requirements, ER diagram, use case diagram, DFD, and testing plan.
