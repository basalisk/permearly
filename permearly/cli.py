import click

from . import __version__


@click.command()
@click.version_option(version=__version__)
def main():
    """ A simple template expander """
    click.echo("")
