# cs61a-su26-lec20

CS 61A SU26 Lecture 20: Interpreters

## Installation

1. Clone this repository by downloading the .zip and unzipping it, or cloning via SSH in the terminal:
```sh
git clone git@github.com:phrdang/cs61a-su26-lec20.git
```
2. Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
3. `cd` into the repository root directory
4. Run `uv sync` to install dependencies

## Usage

First, `cd` into either the `blank` or `sol` directory, depending on if you're checking
your solution or interacting with the staff solution. Then run the command(s) below.

To run the Scheme Tokenizer, run:

```sh
uv run python3 scheme_tokens.py
```

To run the Scheme Reader, run:

```sh
uv run python3 scheme_reader.py
```

To run the Scheme Calculator, run:

```sh
uv run python3 calc.py
```

To exit any of these programs, press `Ctrl + C` or `Ctrl + D` (on both Mac and Windows).
