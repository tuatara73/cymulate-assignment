# cymulate-assignment

## Create secrets in github for authenticating with dockerhub `secrets.DOCKER_USERNAME` `secrets.DOCKER_PASSWORD`
## docker-push.yml will build the app and push it to docker hub

## init-kubernetes.yml will install kind kubernetes on the runner,
## make it available at port 5000 and expose it via nodePort,
## install the helm chart and test the app on its endpoints with `curl`



