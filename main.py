# HackerNews.py: A CLI for reading Hackernews in terminal.

# Idea
# Steps
# 1. Invoke the main file -> Fetch the Top board of HN.
# 2. User selects a post from the board -> Fetch the post from HN.

import click

import fetcher
import tui

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        main()

@cli.command()
def main():
    top()


@cli.command()
def top():
    tui.header()
    tui.top()

@cli.command()
@click.argument("selector", required=True)
def sel(selector):
    tui.header()
    tui.sel(selector)

if __name__ == '__main__':
    cli()
