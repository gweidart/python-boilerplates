
### Directory Tree

![GitHub last commit](https://img.shields.io/github/last-commit/gweidart/python-boilerplates?style=plastic&cacheSeconds=30)

```md
 
1. Django
Django Project/
├── manage.py
├── project_name/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── app_name/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    └── views.py

2. Flask
Flask Project/
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
└── requirements.txt

3. FastAPI
FastAPI Project/
├── main.py
├── routers/
│   └── items.py
├── models/
│   └── item.py
├── schemas/
│   └── item.py
└── requirements.txt

4. Pyramid
Pyramid Project/
├── development.ini
├── production.ini
├── project_name/
│   ├── __init__.py
│   ├── routes.py
│   ├── views.py
│   └── templates/
│       └── mytemplate.pt
└── setup.py

5. Tornado
Tornado Project/
├── app.py
├── handlers/
│   └── main.py
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js

6. Bottle
Bottle Project/
├── app.py
├── views/
│   └── index.tpl
└── static/
    ├── style.css
    └── script.js

7. CherryPy
CherryPy Project/
├── app.py
├── config/
│   └── server.conf
└── static/
    ├── style.css
    └── script.js

8. Falcon
Falcon Project/
├── app.py
├── resources/
│   └── item.py
└── requirements.txt

9. Hug
Hug Project/
├── app.py
└── requirements.txt

10. Sanic
Sanic Project/
├── app.py
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js

11. Dash
Dash Project/
├── app.py
├── assets/
│   ├── style.css
│   └── script.js
└── requirements.txt

12. Web2py
Web2py Project/
├── applications/
│   └── myapp/
│       ├── controllers/
│       │   └── default.py
│       ├── models/
│       │   └── db.py
│       ├── views/
│       │   └── default/
│       │       └── index.html
│       └── static/
│           ├── style.css
│           └── script.js
└── routes.py

13. TurboGears
TurboGears Project/
├── setup.py
├── development.ini
├── production.ini
├── project_name/
│   ├── __init__.py
│   ├── controllers/
│   │   └── root.py
│   ├── model/
│   │   └── models.py
│   └── templates/
│       └── welcome.html
└── README.md

14. Flask-RESTful
Flask-RESTful Project/
├── app.py
├── resources/
│   └── item.py
└── requirements.txt

15. Flask-SocketIO
Flask-SocketIO Project/
├── app.py
├── templates/
│   └── index.html
└── requirements.txt

16. Flask-WTF
Flask-WTF Project/
├── app.py
├── forms.py
├── templates/
│   └── form.html
└── requirements.txt

17. Flask-Admin
Flask-Admin Project/
├── app.py
├── models.py
├── templates/
│   └── admin/
│       └── index.html
└── requirements.txt

18. Flask-Security
Flask-Security Project/
├── app.py
├── models.py
├── templates/
│   └── security/
│       └── login_user.html
└── requirements.txt

19. Flask-Login
Flask-Login Project/
├── app.py
├── models.py
├── templates/
│   └── login.html
└── requirements.txt

20. Flask-Migrate
Flask-Migrate Project/
├── app.py
├── models.py
├── migrations/
│   ├── env.py
│   ├── README
│   └── versions/
└── requirements.txt

21. Flask-SQLAlchemy
Flask-SQLAlchemy Project/
├── app.py
├── models.py
└── requirements.txt

22. Flask-Bootstrap
Flask-Bootstrap Project/
├── app.py
├── templates/
│   └── base.html
└── requirements.txt

23. Flask-Mail
Flask-Mail Project/
├── app.py
├── templates/
│   └── email.html
└── requirements.txt

24. Flask-Babel
Flask-Babel Project/
├── app.py
├── translations/
│   └── en/
│       └── LC_MESSAGES/
│           └── messages.po
└── requirements.txt

25. Flask-Caching
Flask-Caching Project/
├── app.py
└── requirements.txt

26. Pylons
Pylons Project/
├── development.ini
├── production.ini
├── project_name/
│   ├── __init__.py
│   ├── controllers/
│   │   └── root.py
│   ├── model/
│   │   └── models.py
│   └── templates/
│       └── welcome.html
└── README.md

27. CubicWeb
CubicWeb Project/
├── cubicweb/
│   ├── __init__.py
│   ├── entities/
│   │   └── __init__.py
│   ├── views/
│   │   └── __init__.py
│   └── schemas/
│       └── schema.py
└── README.md

28. Growler
Growler Project/
├── app.py
└── requirements.txt

29. Morepath
Morepath Project/
├── app.py
└── requirements.txt

30. Eve
Eve Project/
├── app.py
└── requirements.txt

31. Klein
Klein Project/
├── app.py

32. Molten
Molten Project/
├── app.py
├── handlers/
│   └── item_handler.py
├── models/
│   └── item.py
└── requirements.txt

33. Masonite
Masonite Project/
├── wsgi.py
├── config/
│   ├── application.py
│   ├── database.py
│   └── mail.py
├── app/
│   ├── controllers/
│   │   └── WelcomeController.py
│   ├── models/
│   │   └── User.py
│   └── views/
│       └── welcome.html
└── requirements.txt

34. Vibora
Vibora Project/
├── app.py
├── routes/
│   └── items.py
├── models/
│   └── item.py
└── requirements.txt

35. Japronto
Japronto Project/
├── app.py
└── requirements.txt

36. BlackSheep
BlackSheep Project/
├── app.py
├── routes/
│   └── items.py
├── models/
│   └── item.py
└── requirements.txt

37. Starlette
Starlette Project/
├── app.py
├── routes/
│   └── items.py
├── models/
│   └── item.py
└── requirements.txt

38. Quart
Quart Project/
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
└── requirements.txt

39. Responder
Responder Project/
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
└── requirements.txt

40. Bocadillo
Bocadillo Project/
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
└── requirements.txt

41. Litestar
Litestar Project/
├── app.py
├── routes/
│   └── items.py
├── models/
│   └── item.py
└── requirements.txt

42. Robyn
Robyn Project/
├── app.py
├── routes/
│   └── items.py
├── models/
│   └── item.py
└── requirements.txt

43. Esmerald
Esmerald Project/
├── app.py
├── routes/
│   └── items.py
├── models/
│   └── item.py
└── requirements.txt

44. Falconry
Falconry Project/
├── app.py
├── routes/
│   └── items.py
├── models/
│   └── item.py
└── requirements.txt

45. TornadoFX
TornadoFX Project/
├── app.py
├── routes/
│   └── items.py
├── models/
│   └── item.py
└── requirements.txt

46. Cyclone
Cyclone Project/
├── app.py
├── routes/
│   └── items.py
├── models/
│   └── item.py
└── requirements.txt

47. Aiohttp
Aiohttp Project/
├── app.py
├── routes/
│   └── items.py
├── models/
│   └── item.py
└── requirements.txt

48. Vibora
Vibora Project/
├── app.py
├── routes/
│   └── items.py
├── models/
│   └── item.py
└── requirements.txt

49. Klein
Klein Project/
├── app.py

50. Flask-RESTPlus
Flask-RESTPlus Project/
├── app.py
├── routes/
│   └── items.py
├── models/
│   └── item.py
└── requirements.txt

```
## Authors

- [@gweidart](https://www.github.com/gweidart)
