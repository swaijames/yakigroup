# yakigroup
### 1: You need to install these library before yoou run the project such as
```bash
   pip install django==4.1.1
   pip install djangorestframework
   pip install pillow
   pip install python-decouple
   pip install psycopg2   
   pip install psycopg2-binary 
   pip install django-cors-headers
   pip install whitenoise 
   pip install dj-database-url  
```
### 2: You need to install ```requirements.txt``` file by running
 ```bash
    pip install requirements.txt
    pip freeze > requirements.txt
```    

### 3: In your ```setting.py``` file should put 
```
rest_framework

```  
in ```installed_app```


#### 4: Configure static files
  Make sure below settings are available in your `settings.py` files
  ```python

  STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

  STATIC_URL = '/static/'

  # Extra places for collectstatic to find static files.
  STATICFILES_DIRS = (
      os.path.join(BASE_DIR, 'static'),
  )

  STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

  ```
  then run ```python manage.py collectstatic``` 
  
  If you want to run django migrations or any other pre-scripts on startup, use as below;
```bash
 python manage.py makemigrations
 python manage.py migrate
 python manage.py runserver
```
 
