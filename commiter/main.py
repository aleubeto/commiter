import typer

from typing import Optional
from typing_extensions import Annotated

from commiter.commands.config import config_command
from commiter.commands.commit import commit_command


commiter_cli = typer.Typer()


@commiter_cli.command()
def commit():
    """"""
    commit_command()


@commiter_cli.command()
def config(list: Optional[bool] = False):
    """"""
    config_command(list)


if __name__ == "__main__":
    commiter_cli()

