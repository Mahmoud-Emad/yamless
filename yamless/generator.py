import argparse
import os
import yaml

def generate_dockerfiles(yaml_path):
    # Check if the file exists
    if not os.path.exists(yaml_path):
        print(f'Error: File {yaml_path} not found')
        return

    # Load the YAML file
    with open(yaml_path, 'r') as file:
        data = yaml.safe_load(file)

    # Generate the backend Dockerfile
    backend_requirements = '\n'.join(data['backend']['requirements'])
    backend_port = data['backend']['port']
    with open('Dockerfile.backend', 'w') as file:
        file.write(f'FROM python:3\n\nRUN pip install {backend_requirements}\n\nEXPOSE {backend_port}')

    # Generate the frontend Dockerfile
    frontend_requirements = '\n'.join(data['frontend']['requirements'])
    frontend_port = data['frontend']['port']
    with open('Dockerfile.frontend', 'w') as file:
        file.write(f'FROM node:14\n\nRUN npm install {frontend_requirements}\n\nEXPOSE {frontend_port}')

    print('Dockerfiles generated successfully')

if __name__ == '__main__':
    # Define the command line arguments
    parser = argparse.ArgumentParser(description='Generate Dockerfiles from a YAML file')
    parser.add_argument('yaml_path', help='Path to the YAML file')

    # Parse the command line arguments
    args = parser.parse_args()

    # Call the generate_dockerfiles function with the YAML file path
    generate_dockerfiles(args.yaml_path)
