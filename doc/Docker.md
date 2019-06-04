# Docker

* [Containers](#containers)
  * [Build and start containers](#build-and-start-containers)
  * [Restart containers](#restart-containers)
  * [List containers](#list-containers)
* [Services](#services)
  * [Display logs of a service](#display-logs-of-a-service)
  * [Run commands in a service](#run-commands-in-a-service)

## Containers

### Build and start containers

```
docker-compose up -d
```

### Restart containers

```
docker-compose down && docker-compose up -d
```

### List containers

```
docker-compose ps
```

## Services

### Display logs of a service

```
docker-compose logs -f --tail=10 <service>
```

### Run commands in a service

```
docker-compose exec <service> bash
```
