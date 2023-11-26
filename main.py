import sys
import click
from pathlib import Path
from dataclasses import dataclass


@click.command()
@click.argument(
    "file",
    required=False,
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        path_type=Path,
    ),
)
@click.option("-c", "--bytes", help="print bytes count", is_flag=True)
@click.option("-l", "--lines", help="print lines count", is_flag=True)
@click.option("-w", "--words", help="print words count", is_flag=True)
@click.option("-m", "--characters", help="print characters count", is_flag=True)
def main(file, bytes, lines, words, characters):
    if not any([bytes, lines, words, characters]):
        bytes, lines, words = True, True, True
    if file:
        with open(file, "rb") as f:
            counts = get_count(f)
    else:
        counts = get_count(sys.stdin.buffer)
        file = ""
    result = []
    if lines:
        result.append(counts.lines)
    if characters:
        result.append(counts.characters)
    if words:
        result.append(counts.words)
    if bytes:
        result.append(counts.bytes)

    # append file to print at last
    result.append(str(file))
    click.echo(" ".join(map(str, result)))


def get_count(file):
    bytes = 0
    lines = 0
    words = 0
    characters = 0
    for line in file:
        bytes += len(line)
        lines += 1
        words += len(line.split())
        characters += len(line.decode())
    return CountResult(bytes, lines, words, characters)


@dataclass
class CountResult:
    bytes: int
    lines: int
    words: int
    characters: int


if __name__ == "__main__":
    main()
