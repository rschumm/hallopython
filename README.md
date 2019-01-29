HalloPython for OpenShift s2i insprired by the [Docker Example](https://docs.docker.com/compose/gettingstarted/)   

Documentation for the `oc new app` [command](https://docs.openshift.com/container-platform/3.11/dev_guide/application_lifecycle/new_app.html).


    oc new-app .  
    or: 
    oc new-project python
    oc new-app openshift/python~https://github.com/rschumm/hallopython.git


then: 

- apply the template [redis-persistent](https://github.com/openshift/origin/blob/master/examples/db-templates/redis-persistent-template.json) (by hand or by `oc create -f...`)
- in the generated build-config, add an environment-variable with name `REDIS_PW` with the value `database-password` from the `redis` secret 
- make sure the generated service points to port 5000
- add a route to port 5000 to the generated service 
- voilà 




