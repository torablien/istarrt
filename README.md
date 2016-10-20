Run Server

    $ python manage.py runserver $IP:$PORT
    
Install Required Tools

    sudo pip install -r requirements.txt
    
Adding New Template

 - Make sure to go to workspace/istarrt/settings.py and add   
  `os.path.join(BASE_DIR, 'APP-NAME-HERE/templates')`     
    to     
  `TEMPLATES['DIRS']`

Adding Stylesheets and Scripts to Templates
 - When putting the tags, make sure to set   
 `src="{% static 'REL-FILEPATH-HERE' %}"`

Superuser:  

    User: root   
    Password: istarrtpassword

Running on Django 1.9
