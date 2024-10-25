# Docker

* [Containers](#containers)
  * [List all containers](#list-all-containers)
  * [Get container id by its name](#get-container-id-by-its-name)
  * [Run commands in a container](#run-commands-in-a-container)
  * [Remove unused data](#remove-unused-data)
* [Composition](#composition)
  * [Start composition](#start-composition)
  * [Restart composition](#restart-composition)
  * [List containers in composition](#list-containers-in-composition)
* [Services](#services)
  * [Display logs of a service](#display-logs-of-a-service)
  * [Run commands in a service](#run-commands-in-a-service)
  * [Copy a file into a service](#copy-a-file-into-a-service)
* [Tools](#tools)
  * [Copy a file into a container](#copy-a-file-into-a-container)
  * [Copy a file from a container](#copy-a-file-from-a-container)
* [Network](#network)
  * [List networks](#list-networks)
  * [Inspect network](#inspect-network)
* Compose files
  * [PostGIS and pgAdmin](../code/docker/postgis-pgadmin/docker-compose.yml)

## Containers

### List all containers

```
docker ps
```

### Get container id by its name

```
docker ps -qf "name=<container-name>"
```

### Run commands in a container

```
docker exec -it <container-id> bash
```

Or directly with its name

```
docker exec -it `docker ps -qf "name=<container-name>"` bash
```

### Remove unused data

```
docker system prune -a
```

## Composition

### Start composition

```
docker compose up -d
```

### Restart composition

```
docker compose down --remove-orphans && docker compose up -d
```

### List containers in composition

```
docker compose ps
```

## Services

### Display logs of a service

```
docker compose logs -tf --tail=10 <service>
```

### Run commands in a service

```
docker compose exec <service> bash
```

### Copy a file into a service

```
docker compose cp <source-file> <service>:<destination-file>
```

## Tools

### Copy a file into a container

```
docker cp <source-file> <container-id>:<destination-file>
```

### Copy a file from a container

```
docker cp <container-id>:<source-file> <destination-file>
```

## Network

### List networks

```
docker network ls
```

### Inspect network

```
docker network inspect <network-name>
```
