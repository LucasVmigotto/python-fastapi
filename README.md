# [Python](https://www.python.org/) with [FastAPI](https://fastapi.tiangolo.com/) template

A template repository with an API developed in [Python](https://www.python.org/) using [FastAPI](https://fastapi.tiangolo.com/) framework

## Pre-requisites

### Mandatory

* [Docker CE](https://docs.docker.com/engine/)

### Optional

* [Visual Studio Code](https://code.visualstudio.com/)
* [Docker Compose](https://docs.docker.com/compose/)

## Development

1. Clone the repository

    * With `HTTP`

        ```bash
        # With HTTPS
        git clone https://github.com/LucasVmigotto/python-fastapi.git
        ```

    * With `SSH`

        ```bash
        git clone git@github.com:LucasVmigotto/python-fastapi.git
        ```

2. Open the project with [Visual Studio Code](https://code.visualstudio.com/):

    ```bash
    code <project folder>
    ```

    > If the project not already open inside a container, use `CTRL` + `Shift` + `P` and run the _Dev Containers: Rebuild Container Without Cache command_

3. Happy coding 😁

### Useful Docker commands

#### Containers

* List all Docker containers

    ```bash
    docker ps -a
    ```

* Remove Docker Compose containers

    ```bash
    docker compose rm --stop -f
    ```

* Prune containers

    ```bash
    docker container prune --force
    ```

#### Images

* List all Docker images

    ```bash
    docker ls -a
    ```

* Remove Docker _dangling_ images

    ```bash
    docker image rm -f $(docker image ls --filter "dangling=true" -aq)
    ```

    > **WARNING**: If you want to remove **ALL** Docker images, just remove the `--filter` flag and argument
    >
    > `docker image rm -f $(docker image ls -aq)`

#### Volumes

* List all Docker volumes

    ```bash
    docker volume ls
    ```

* Prune Docker volumes

    ```bash
    docker volume prune --force
    ```

## Running the application

### Inside the Visual Studio Code

* Run the following command, **inside the Visual Studio Code terminal**, to start the application:

    ```bash
    poetry run python \
        -m uvicorn \
        --host 0.0.0.0 \
        --port 8001 \
        --log-level debug \
        --reload
    ```

    > Be careful after running this command with the port in use to not get any conflict using the Docker Compose service
    >
    > To make sure, run the application only with the Docker Compose service, and use the Visual Studio Code dev container exclusive as code environment.

### Inside a separate container (with Docker Compse)

* Run the following command to start the container service:

    ```bash
    docker compose up api
    ```

    > You can use `docker compose -d up api` to run in detached mode. Although, to be able to see any server logs, you will need to run `docker compose logs -f api`
    >
    > Once successfully started, the service will be available in [localhost:8000](http://localhost:8000)

## Deployment

### Build the Docker container for Production environment

* Run the following command in the first level of the project's folder:

    ```bash
    docker build \
    -f Dockerfile
    --tag python-fastapi \
    --no-cache \
    .
    ```

    > If necessary, add the --progress plain to see all build output

  * You can test the container with:

    ```bash
    docker run \
        --publish 8000:80 \
        --rm \
        python-fastapi
    ```

    > Give it a try in [localhost:8000](http://localhost:8000/docs)

## References

* [Python 3.x](https://docs.python.org/3/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Docker](https://docs.docker.com/)
* [Docker Compose](https://docs.docker.com/reference/cli/docker/compose/)
* [Poetry](https://python-poetry.org/)
