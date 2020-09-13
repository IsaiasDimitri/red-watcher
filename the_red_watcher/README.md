# Red Watcher
> Currently in development. Some things I'm just testing and put here.  

Red Watcher is a platform that recieves information about disasters like fires, earthquakes, cats in trees.  
I'm using Django + GraphQL to handle requests and(soon) hosting html views.  
In the future, I'll use Postgres as database solution. For now, sqlite can hadle this for us.  
I also intend to create a mobile interface soon, maybe using Flutter.  
## Motivation  
Fireman are the best. 

## Requirements  
Python  
Some tool to call GraphQL API (suggestion: [Insomnia](https://insomnia.rest/download/))

## Steps to run

```
git clone https://github.com/IsaiasDimitri/red-watcher.git
cd red-watcher
python -m venv .env
. .env/bin/activate
pip install -r requirements.txt
python manage.py createsuperuser #to access admin's page
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
For a while, no view is provided(shame on me), but you can interact with:  
-- Django-Admin interface:  http://localhost:8000/admin/  
-- GraphQL interface:  http://localhost:8000/graphql/