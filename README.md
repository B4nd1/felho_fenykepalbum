# Album

### Install dependencies
```
pip install -r requirements.txt
```

### Run
```
python manage.py runserver
```

```python
print("Hello World")
```

# Functions of the app 
* Login, Register
* See details of the picture
* Upload pictures
* Delete pictures
* 

# Screenshots
![imagelist](assets/images_list.png)



# Useful Openshift commands
oc new-app postgresql POSTGRESQL_USER=admin POSTGRESQL_DATABASE=djangodb POSTGRESQL_PASSWORD=password

oc new-app https://github.com/B4nd1/felho_fenykepalbum --strategy=docker


oc delete svc felhofenykepalbum
oc delete bc felhofenykepalbum
oc delete deployments.apps felhofenykepalbum

oc expose service/felhofenykepalbum


oc create route edge --service=openshift