# Yamless

Yamless is a command-line tool that generates Docker images based on the requirements defined in a YAML file. It currently supports Python and Node.js projects.

## Installation

Yamless requires [Docker](https://docs.docker.com/get-docker/) and [Poetry](https://python-poetry.org/docs/) to be installed on your machine.

To install Yamless, run:

```bash
poetry install
```

## Usage

To use Yamless, navigate to your project directory and run the following command:

```bash
yamless generate
```

This will generate two Dockerfiles, one for the backend and one for the frontend, based on the requirements defined in your project's requirements.txt or package.json file.

To build the Docker images, run:

```bash
docker build -t <backend_image_name> -f Dockerfile.backend .
docker build -t <frontend_image_name> -f Dockerfile.frontend .
```

Replace <host_port> and <container_port> with the ports you want to use for your Docker image.

### YAML Configuration

Yamless reads the configuration from a yamless.yaml file in the root directory of your project.

### Example YAML Configuration

```yaml
project_name: My Project
backend_image_name: myproject_backend
frontend_image_name: myproject_frontend
backend_port: 8000
backend_packages:
  - Django==3.1.7
  - djangorestframework==3.12.2
frontend_port: 8080
frontend_packages:
  - vue@2.6.12
```

The project_name field is a string that will be used as the name of the project in the generated Dockerfiles.

The backend_image_name and frontend_image_name fields are strings that will be used as the names of the generated Docker images.

The backend_port and frontend_port fields are integers that specify the ports that will be exposed by the Docker images.

The backend_packages and frontend_packages fields are lists of strings that specify the packages that will be installed in the backend and frontend Docker images, respectively. The format of the packages depends on the language used in the project.

### Supported Packages Formats

- Python projects: packages should be listed in a requirements.txt file.
- Node.js projects: packages should be listed in a package.json file under the dependencies field.

### Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

### License
