
# Logic Gates in Python

This document explains how different logic gates (used in electronics and programming) can be represented in Python using logical operators.

## 1. NOT Gate
The **NOT gate** inverts the input. If the input is `True`, the output is `False`, and vice versa.

- In Python, the `not` operator is used.

#### Example:
```python
not True  # Outputs: False
not False # Outputs: True
```

#### Truth Table:
| Input  | Output (NOT) |
|--------|--------------|
| True   | False        |
| False  | True         |

---

## 2. AND Gate
The **AND gate** outputs `True` only if **both** inputs are `True`. Otherwise, it outputs `False`.

- In Python, the `and` operator is used.

#### Example:
```python
True and True   # Outputs: True
True and False  # Outputs: False
False and True  # Outputs: False
```

#### Truth Table:
| Input 1 | Input 2 | Output (AND) |
|---------|---------|--------------|
| True    | True    | True         |
| True    | False   | False        |
| False   | True    | False        |
| False   | False   | False        |

---

## 3. NAND Gate
The **NAND gate** (NOT AND) outputs the **opposite** of the AND gate. It outputs `True` unless **both** inputs are `True`.

- In Python, you can use `not` with `and`.

#### Example:
```python
not (True and True)  # Outputs: False
not (True and False) # Outputs: True
```

#### Truth Table:
| Input 1 | Input 2 | Output (NAND) |
|---------|---------|---------------|
| True    | True    | False         |
| True    | False   | True          |
| False   | True    | True          |
| False   | False   | True          |

---

## 4. NOR Gate
The **NOR gate** (NOT OR) is the opposite of the OR gate. It outputs `True` only if **both** inputs are `False`.

- In Python, you can use `not` with `or`.

#### Example:
```python
not (True or True)  # Outputs: False
not (False or False) # Outputs: True
```

#### Truth Table:
| Input 1 | Input 2 | Output (NOR) |
|---------|---------|--------------|
| True    | True    | False        |
| True    | False   | False        |
| False   | True    | False        |
| False   | False   | True         |

---

## 5. XOR Gate
The **XOR gate** (exclusive OR) outputs `True` if **only one** of the inputs is `True`. If both are the same (both true or both false), it outputs `False`.

- In Python, you can simulate this using `!=` (not equal).

#### Example:
```python
True != True   # Outputs: False
True != False  # Outputs: True
```

#### Truth Table:
| Input 1 | Input 2 | Output (XOR) |
|---------|---------|--------------|
| True    | True    | False        |
| True    | False   | True         |
| False   | True    | True         |
| False   | False   | False        |

---

## 6. XNOR Gate
The **XNOR gate** (exclusive NOR) is the opposite of XOR. It outputs `True` if **both inputs are the same**.

- In Python, you can simulate this using `==`.

#### Example:
```python
True == True   # Outputs: True
True == False  # Outputs: False
```

#### Truth Table:
| Input 1 | Input 2 | Output (XNOR) |
|---------|---------|---------------|
| True    | True    | True          |
| True    | False   | False         |
| False   | True    | False         |
| False   | False   | True          |
```

---

## Summary of Logic Gates:
- **NOT**: Inverts the input.
- **AND**: Both inputs must be true for a true output.
- **NAND**: Opposite of AND.
- **OR**: At least one input must be true.
- **NOR**: Opposite of OR.
- **XOR**: One input must be true, but not both.
- **XNOR**: Both inputs must be the same.
