<h1>
  <p align=center>
    <b>
      pyfu_k
    </b>
  </p>
</h1>

> Convert Python codes into 10 different characters: `cehrx()=+*`

The idea comes from [JSFuck](https://github.com/aemkei/jsfuck).

## Example

`print(1)` would be converted into the following source:

```python
exec(chr((()==())+(()==())+((()==())+(()==())*((()==())+((()==())+(()==())+(()
==()))**((()==())+(()==()))))*((()==())+((()==())+(()==())+(()==()))**((()==()
)+(()==()))))+chr((()==())+(()==())+(()==())+(()==())+((()==())+(()==())*((()=
=())+((()==())+(()==())+(()==()))**((()==())+(()==()))))*((()==())+((()==())+(
()==())+(()==()))**((()==())+(()==()))))+chr((()==())+(()==())+(()==())+(()==(
))+(()==())+((()==())+((()==())+(()==())+(()==()))**((()==())+(()==())))*((()=
=())+((()==())+(()==())+(()==()))**((()==())+(()==()))))+chr(((()==())+(()==()
)*((()==())+((()==())+(()==())+(()==()))**((()==())+(()==()))))*((()==())+((()
==())+(()==())+(()==()))**((()==())+(()==()))))+chr(((()==())+(()==()))*((()==
())+(()==())+(()==()))+((()==())+(()==())*((()==())+((()==())+(()==())+(()==()
))**((()==())+(()==()))))*((()==())+((()==())+(()==())+(()==()))**((()==())+((
)==()))))+chr(((()==())+(()==())+(()==())+(()==()))*((()==())+((()==())+(()==(
))+(()==()))**((()==())+(()==()))))+chr(((()==())+(()==())+(()==()))**((()==()
)+(()==()))+((()==())+(()==())+(()==())+(()==()))*((()==())+((()==())+(()==())
+(()==()))**((()==())+(()==()))))+chr((()==())+((()==())+(()==())+(()==())+(()
==()))*((()==())+((()==())+(()==())+(()==()))**((()==())+(()==())))))
```

So far, pyfu_k can convert any number into the 5 characters `()=+*`. However I havn't found a way to convert a string without `chr` or execute a piece of code without `exec` in Python.

## Usage

```sh
$ python pyfu_k.py -h
usage: pyfu_k.py [-h] [-v] [--no-exec] [code]

Convert Python codes into 10 different characters: cehrx()=+*

positional arguments:
  code           code for the conversion (interactive mode if not given)

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
  --no-exec      remove the 'exec' function call in the converted code
```

or

```python
from pyfu_k import pyfu_k

print(pyfu_k("print(1)"))  # print the result of conversion

exec(pyfu_k("print(1)", no_exec=True))  # remove 'exec' and execute manually
```

## How it works

```python
()                 # an empty tuple
()==()             # True
(()==())+(()==())  # True+True, which is 2
```

See the detailed conversion rules in [algorithm.md](./algorithm.md).

## License

MIT License.
