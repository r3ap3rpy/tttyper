import typer

url = "https://google.com"

def main():
    typer.echo(f"Launching app for url: {url}")
    typer.launch(url)

if __name__ == '__main__':
    typer.run(main)