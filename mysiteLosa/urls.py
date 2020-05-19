from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')), #questi 2 bisgna inserirli nell'url dopo http://127.0.0.1:8000/ e ti fanno visualizzare varie scelte
    path('admin/', admin.site.urls),
]
"""
python manage.py makemigrations polls dice a Django che ci sono stati dei cambiamenti all'inerno dei models
ed i cambiamenti li troviamo nei file polls/migrations/0001_initial.py che possiamo anche editare a mano.
python manage.py sqlmigrate polls 0001 crea l'SQL per creare la tabella con tutti i suoi attributi nel db
"""