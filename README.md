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
$ python pyfu_k.py
```

or

```python
from pyfu_k import pyfu_k

print(pyfu_k("print(1)"))  # print the result of conversion

exec(pyfu_k("print(1)", add_exec=False))  # execute the result of conversion
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
