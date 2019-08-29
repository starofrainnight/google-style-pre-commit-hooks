#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Console script for google-style-pre-commit-hooks."""

import os
import os.path
import click
import fnmatch
import shlex
from subprocess import run


@click.group()
def main():
    """Console script for google-style-pre-commit-hooks."""
    pass


@main.command()
@click.argument("files", nargs=-1)
def java(files):
    """Format all changed java files by Google Java Format"""
    CACHE_DIR = ".cache"
    FORMATTER_VERSION = "1.7"
    FORMATTER_FILE_DIR = "google-java-format-%s" % FORMATTER_VERSION
    FORMATTER_FILE_NAME = (
        "google-java-format-%s-all-deps.jar" % FORMATTER_VERSION
    )
    FORMATTER_FILE_PATH = os.path.join(CACHE_DIR, FORMATTER_FILE_NAME)
    FORMATTER_URL = (
        "https://github.com/google/google-java-format/releases/download/%s/%s"
        % (FORMATTER_FILE_DIR, FORMATTER_FILE_NAME)
    )
    FORMATTER_EXEC_PREFIX = "google-java-format"

    click.echo("Checking if formatter exists ...")
    p = run("%s --version" % FORMATTER_EXEC_PREFIX, shell=True)
    if p.returncode != 0:
        os.makedirs(CACHE_DIR, exist_ok=True)

        if os.path.exists(os.path.join(CACHE_DIR, FORMATTER_FILE_NAME)):
            click.echo("Found local cached formatter!")
        else:
            click.echo(
                "Google java style formatter not exists, downloading..."
            )
            run(
                'wget -O %s "%s"' % (FORMATTER_FILE_PATH, FORMATTER_URL),
                shell=True,
            )

        FORMATTER_EXEC_PREFIX = "java -jar .cache/%s" % FORMATTER_FILE_NAME
    else:
        click.echo("Found global formatter!")

    click.echo("Checking changed files ...")

    changed_files = []
    for afile in files:
        afile = afile.strip()
        if not fnmatch.fnmatch(afile, "*.java"):
            continue

        changed_files.append(shlex.quote(afile))

    if len(changed_files) > 0:
        click.echo("%d files need to be parsed:" % len(changed_files))
        for afile in changed_files:
            click.echo("* %s" % afile)

        cmd_line_files = " ".join(changed_files)
        run(
            "%s --replace %s" % (FORMATTER_EXEC_PREFIX, cmd_line_files),
            shell=True,
        )

        run("git add %s" % cmd_line_files, shell=True)
    else:
        click.echo("No changed files!")

    click.echo("Done!")


if __name__ == "__main__":
    main()
