from docker.client import Client
from docker.utils import kwargs_from_env

import click
import json
import random

@click.command()
def world_of_docker():
    """Pulls and starts a container from a random Docker image in the top 100."""

    with open('repos.json') as data_file:    
        repos = json.load(data_file)

    client = Client(**kwargs_from_env())

    random_repo = random.choice(repos)['name']

    click.echo('Hmmmmmm.... how about %s? Everybody likes %s!' % (random_repo, random_repo))

    for line in client.pull(random_repo, stream=True):
        click.echo(json.loads(line)['status'])

    click.echo('Now let\'s just start up a container here...')

    container = client.create_container(image=random_repo)
    client.start(container=container.get('Id'))

    container_name = client.inspect_container(container['Id'])['Name'].strip('/')

    click.echo('Up and running! Enjoy your new %s container, %s' % (random_repo, container_name))

if __name__ == '__main__':
    world_of_docker()
