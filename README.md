# Deploy Project
### Start Run
- Command to Landing Folder
```
    cd Homework/
```
You will see docker-compose.yml this path
```
.
├── django
│   ├── backend
│   │   ├── api
│   │   ├── backend(Project)
│   │   ├── Dockerfile
│   │   ├── manage.py
│   │   ├── requirements.txt
│   │   ├── runserver.sh
│   │   └── student(App)
│   ├── docker-compose.yml
│   ├── .env
│   └── start-django.sh
└── README.md
```

Command to django/ Folder
```
    cd django/
```
Command.. Run Docker Compose **First Time
```
    docker compose up --build
```
Command Run docker compose **Next Time
```
    docker compose up 
```

### Open new terminal

- Command exec to service
```
    docker compose exec backend bash
```
- Create SuperUser (admin)
```
    python manage.py creatsuperuser
```

### Add data to database 

- Open browser to localhost ,You will see routers endpoint.
```
    http://localhost:8000/api/v1/
```
