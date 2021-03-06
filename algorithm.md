## pyfu_k algorithm version 0.2.0 (latest)

### Basics

- `True` => `()==()`

- `False` => `()==(True)` => `()==(()==())`

### Numbers

- `0` => `(False)` => `()==(()==())`

- `1` => `(True)` => `()==()`

- `2` => `(1)+(1)`

- `3` => `(1)+(1)+(1)`

- `4` => `(1)+(1)+(1)+(1)`

- `5` => `(1)+(1)+(1)+(1)+(1)`

- `6` => `(2)*(3)` => `((1)+(1))*((1)+(1)+(1))`

- `7` => `(1)+(6)` => `(1)+((1)+(1))*((1)+(1)+(1))`

- `8` => `(2)*(3)` => `((1)+(1))**((1)+(1)+(1))`

- `9` => `(3)**(2)` => `((1)+(1)+(1))**((1)+(1))`

- `10` => `(1)+(9)` => `(1)+((1)+(1)+(1))**((1)+(1))`

- `xy` => `(y)+(x)*(10)` => `(y)+(x)*((1)+((1)+(1)+(1))**((1)+(1)))`

- `xyz` => `(z)+((y)+(x)*(10))*(10)` => `(z)+((y)+(x)*((1)+((1)+(1)+(1))**((1)+(1))))*((1)+((1)+(1)+(1))**((1)+(1)))`

### Others

- `character` => `chr(number)`

- `string` => `character+...+character`

- `evaluate_value` => `eval(string)`

---

## pyfu_k algorithm version 0.1.1

### Basics

- `True` => `()==()`

### Numbers

- `-2` => `~(True)` => `~(()==())`

- `2` => `-(-2)` => `-~(()==())`

- `number` => `-~(number-1)` => `-~-~...-~(2)` => `-~-~...-~-~(()==())`

### Others

- `character` => `chr(number)` => `chr(-~-~...-~-~(()==()))`

- `string` => `character+...+character` => `chr(-~-~...-~-~(()==()))+...+chr(-~-~...-~-~(()==()))`

- `evaluate_value` => `eval(string)` => `eval(chr(-~-~...-~-~(()==()))+...+chr(-~-~...-~-~(()==())))`

---

## pyfu_k algorithm version 0.1.0

### Basics

- `True` => `()==()`

- `False` => `(True)==()` => `(()==())==()`

### Numbers

- `-1` => `-(True)` => `-(()==())`

- `-2` => `~(True)` => `~(()==())`

- `0` => `-~(-1)` => `-~-(()==())`

- `1` => `-(-1)` => `--(()==())`

- `2` => `-(-2)`  == `-~(()==())`

- `number` => `-~(number-1)` => `-~-~...-~(2)` => `-~-~...-~-~(()==())`

- `-number` => `~-(-number+1)` => `~-~-...~-(-2)` => `~-~-...~-~(()==())`

### Others

- `character` => `chr(number)` => `chr(-~-~...-~-~(()==()))`

- `string` => `character+...+character` => `chr(-~-~...-~-~(()==()))+...+chr(-~-~...-~-~(()==()))`

- `evaluate_value` => `eval(string)` => `eval(chr(-~-~...-~-~(()==()))+...+chr(-~-~...-~-~(()==())))`
