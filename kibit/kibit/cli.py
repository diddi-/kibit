import click
import yaml
from yaml import Loader

from kibit.spec.spec import Spec
from kibit.tasks.taskrunner import TaskRunner


@click.command()
@click.argument("spec")
def main(spec: str):
    """ Kibit tool"""
    try:
        with open(spec, "r") as y:
            data = yaml.load(y, Loader=Loader)
        runner = TaskRunner(Spec.load(data))
        runner.start()
    except Exception as e:
        print(e)
