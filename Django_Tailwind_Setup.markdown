# Setting Up a Django Project with Tailwind CSS

## Aim
Setup a Django project which utilizes Tailwind CSS for styling.

## Steps

### 1. Setup Virtual Environment
```bash
python -m venv venv
```

### 2. Activate Virtual Environment
```bash
venv\Scripts\activate
```

### 3. Install Django
```bash
pip install django
```

### 4. Initialize Django Project
#### a. Create Project
```bash
django-admin startproject pracprj
```

#### b. Navigate to Project Directory
```bash
cd pracprj
```

### 5. Configure Project Components
- **views.py**: Create for routing functions.
- **urls.py**: Declare URL paths.
- **templates folder**: Create for maintaining templates.
- **settings.py**: Add templates directory to `TEMPLATES['DIRS'] = ['templates']`.

### 6. Create a New App
#### a. Create App
```bash
python manage.py startapp <app_name>
```

#### b. Register App
Add the new app to `INSTALLED_APPS` in `settings.py`.

#### c. Configure App Components
Repeat steps from 5 for views, URLs, and templates in the new app.

### 7. Setup Tailwind CSS
#### a. Install Tailwind Packages
```bash
pip install django-tailwind
pip install django-browser-reload
pip install 'django-tailwind[reload]'
```
Also add this line in `urls.py`:
```python
path('__reload__/', include('django_browser_reload.urls')),
```

#### b. Register Tailwind App
Add `'tailwind'` to `INSTALLED_APPS` in `settings.py`.

#### c. Initialize Tailwind
```bash
python manage.py tailwind init
```

#### d. Navigate to Project Directory
```bash
cd pracprj
```

#### e. Configure Tailwind Settings
Add the following to `settings.py`:
```python
TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = ['127.0.0.1']
```

#### f. Install Tailwind
##### i. Set NPM Path
Find the npm location using:
```bash
where npm
```
Add to `settings.py`:
```python
NPM_BIN_PATH = "location_for_npm"
```

##### ii. Install Tailwind Dependencies
```bash
python manage.py tailwind install
```

#### g. Configure Base Template
Check the `theme` app for a `base.html` file. If using an existing `base.html`, include:
```html
{% load static tailwind_tags %}
{% tailwind_css %}
```

#### h. Add Middleware
Add the following to `settings.py`:
```python
INSTALLED_APPS = [
    ...
    'django_browser_reload',
]

MIDDLEWARE = [
    ...
    'django_browser_reload.middleware.BrowserReloadMiddleware',
]
```

#### i. Run Django Server
```bash
python manage.py runserver
```

#### j. Run Tailwind (in a new terminal)
```bash
python manage.py tailwind start
```

### 8. Create a Sample Model and add this to Handle Media `settings.py`

```python
# Media Folders
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### 9. Make some Configurations in `urls.py`
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your url patterns
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 10. Make Migrations and Migrate
```bash
python manage.py makemigrations
python manage.py migrate
```
#### Install Sqlite Viewer for viewing the database in VsCode here's the link [SQLite Viewer](https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer).

### 11. Adding the Model's to Admin Panel
In your app's `admin.py`, register your models:
```python
from django.contrib import admin
from .models import YourModel
admin.site.register(YourModel)
```
### 12. Create a Superuser
```bash
python manage.py createsuperuser
```
Now access the admin panel at `http://127.0.0.1:8000/admin` with the superuser credentials.

In case you forgot the superuser password, you can reset it using:
```bash
python manage.py changepassword <username>
```


> **Your Django project is now set up with Tailwind CSS for styling!  
> Start building your application using Tailwind's powerful utility-first CSS framework.  
> For advanced configurations and customizations, refer to the [Tailwind documentation](https://tailwindcss.com/docs).**
>
> **With a data model and media handling (like image uploads), you can easily manage media files in your Django app.**