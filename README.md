Minimales Beispiel für eine Phython (Flask) - Applikation in OpenShift:   
(läuft auf jedem OpenShift Cluster)   

HalloPython for OpenShift s2i insprired by the [Docker Example](https://docs.docker.com/compose/gettingstarted/)    

# features

Python Flask Application with HTML templating and Layout based on Bootstrap.   
Redis Cache Backend with persistent Storage.  


OpenShift erstellt für die Python-Applikation automatisch eine BuildConfig und DeploymentConfig (etc.), baut ein Docker-Image in der internen Registry und lässt es laufen.   
Der Redis-Cache wird in diesem Set-Up von Hand mit einem Template von OpenShift erstellt. 


# OpenShift 

## set up OpenShift Project 

    oc new-project py


## set up Redis 

Apply the template [redis-persistent](https://github.com/openshift/origin/blob/master/examples/db-templates/redis-persistent-template.json) 
(Do this with the button "Add to project -> import from json" hand or by `oc create -f...`) - or by just 
selection Redis from the Catalog.  



## set up Python Applikation 
    
    oc new-app openshift/python~https://github.com/rschumm/hallopython.git 
    optional: --source-secret='rs-password'


## Finishing: 

- in the generated build-config of the Phyton-Application, add an environment-variable with name `REDIS_PW` with the value `database-password` from the `redis` secret (this will be read by the Python Application via `os.getenv('REDIS_PW')`)
- make sure the generated service points to port 5000
- add a route to port 5000 to the generated service 
- voilà... should work. 


# Goodie: Job and CronJob

The little script `job.py` will be packed in the same image by the builder image.  
As a demo, `job.py` can be started by a Kubernetes Job or CronJob: 

    oc apply -f job.yml
    oc apply -f cronjob.yml

respectively.  



## Doku

Documentation for the `oc new app` [command](https://docs.openshift.com/container-platform/3.11/dev_guide/application_lifecycle/new_app.html).   


# Local run

to run the application locally: (needs a redis cache of course...) 

    pip install -r requirements.txt
    python app.py 
