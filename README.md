# pywc

`pywc` is a Unix `wc` command line tool clone in Python.

## Local Setup

- Clone the repository:
```sh
  git clone https://github.com/Jaspreet-singh-1032/pywc.git
```
- Navigate to the project directory:
```sh
cd pywc
```
- Ensure you have Python installed.

- Set up a virtual environment (optional but recommended).

- Install the tool using `setup.py`:
```sh
python setup.py install
```

Now you can use the `pywc` command from the terminal.

### Usage
To check available options, run:
```sh
pywc --help
```

### Options:

- `-c, --bytes`: Print bytes count
- `-l, --lines`: Print lines count
- `-w, --words`: Print words count
- `-m, --characters`: Print characters count


### Example:
```sh
pywc -l myfile.txt 
```
or, You can also provide standard input data using:
```sh
cat myfile.txt | pywc -l
```
