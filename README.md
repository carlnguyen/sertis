PART 1: Kubernetes
=======
* Create namespace
```bash
kubectl create ns internal-tools
```

* Deploy frontend pod
```bash
helm install frontend kubernetes/charts/internal-frontend \
--values manifests/frontendi.yml \
--namespace internal-tools \
--set BACKEND_PATH=backend
```

* Deploy posgresql db

	Install postgresql chart
	
```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm install internal-db oci://registry-1.docker.io/bitnamicharts/postgresql --values manifests/postgresql.yml
```

PostgreSQL can be accessed via port 5432 on the following DNS names from within your cluster:
	
	internal-db-postgresql.internal-tools.svc.cluster.local - Read/Write connection

To get the password for "postgres" run:

    export POSTGRES_ADMIN_PASSWORD=$(kubectl get secret --namespace internal-tools internal-db-postgresql -o jsonpath="{.data.postgres-password}" | base64 -d)

To get the password for "admin" run:

    export POSTGRES_PASSWORD=$(kubectl get secret --namespace internal-tools internal-db-postgresql -o jsonpath="{.data.password}" | base64 -d)

To connect to your database run the following command:

    kubectl run internal-db-postgresql-client --rm --tty -i --restart='Never' --namespace internal-tools --image docker.io/bitnami/postgresql:15.4.0-debian-11-r10 --env="PGPASSWORD=$POSTGRES_PASSWORD" \
      --command -- psql --host internal-db-postgresql -U admin -d internal -p 5432

    > NOTE: If you access the container using bash, make sure that you execute "/opt/bitnami/scripts/postgresql/entrypoint.sh /bin/bash" in order to avoid the error "psql: local user with ID 1001} does not exist"

To connect to your database from outside the cluster execute the following commands:

    kubectl port-forward --namespace internal-tools svc/internal-db-postgresql 5432:5432 &
    PGPASSWORD="$POSTGRES_PASSWORD" psql --host 127.0.0.1 -U admin -d internal -p 5432

* Deploy backend pod

Get IP of db pod:

```bash
echo $PODIP=$(k get pod internal-db-postgresql-0 --template '{{.status.podIP}}')
```

```bash
helm install backend kubernetes/charts/internal-backend \
--values manifests/backend.yml \
--namespace internal-tools \
--set DB_USER=dbadmin \
--set DB_PASSWORD=P@ssword123 \
--set DB_HOST=$PODIP \
--set DB_DATABASE=dbinternal
```


* Deploy reverse Proxy/Ingress

Install nginx controller with reverse proxy option:

```bash
	helm install internal-ingress stable/nginx-ingress \
	--set controller.publishService.enabled=true \
	--set-string controller.config.use-forward-headers=true,controller.config.compute-full-forward-for=true,controller.config.use-proxy-protocol=true  \
	--set controller.service.annotations."service\.beta\.kubernetes\.io/do-loadbalancer-enable-proxy-protocol=true"
```
* Deploy prometheus/alertmanager

Install dependencies component

```bash
	helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
	helm repo update
	helm install prometheus-node-exporter prometheus-community/prometheus-node-exporter
	helm install alertmanager prometheus-community/alertmanager
```

Install prometheus charts
```bash
	helm install prometheus-internal prometheus-community/alertmanager --set prometheus-pushgateway=false 
```

PART 2: Python programming
=======

Run the tool:

```bash
	python3 main.py
```
