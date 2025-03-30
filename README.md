# Album

### Install dependencies
```
pip install -r requirements.txt
```

### Run
```
python manage.py runserver
```

# Functions of the app 
* Login, Register
* See details of the picture
* Upload pictures
* Delete pictures

# Screenshot
![imagelist](assets/images_list.png)



# Useful Openshift commands
```
oc new-app https://github.com/B4nd1/felho_fenykepalbum --strategy=docker

oc delete svc felhofenykepalbum
oc delete bc felhofenykepalbum
oc delete deployments.apps felhofenykepalbum
```