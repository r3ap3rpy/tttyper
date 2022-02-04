import typer

def main():
    what_do_you_want = typer.prompt("What do you want?:")
    typer.echo(f"I want: {what_do_you_want}")
    do_you_really_want = typer.confirm(f"Do you areally want: {what_do_you_want}")
    if do_you_really_want:
        typer.echo("You shall have it!")
    else:
        typer.echo("No you shall not have it!")




    do_you_really_want_or_abort = typer.confirm(f"Do you really want: {what_do_you_want}", abort = True)
    typer.echo("Only yes reveals it!")
if __name__ == '__main__':
    typer.run(main)