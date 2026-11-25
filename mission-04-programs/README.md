# Mission 4 — Run a Python program

## 1. Task / objective

Create and run a one-line Python script, then compare compiler and interpreter behavior.

## 2. Work completed

Created `hello.py`, ran it with Python 3 and checked the exact line it printed.

## 3. Commands / tools used

`python3 hello.py` ran the file from the mission folder. Python's `print()` function sent one line to the terminal.

```text
$ python3 hello.py
Hello from Python
```

## 4. My understanding

| Point | Compiler | Interpreter |
| --- | --- | --- |
| When it acts | Translates the source before the translated instructions run. | Carries out program instructions at runtime. |
| Common result | Produces machine code, bytecode or another representation. | Produces the effects of the program, such as printed text. |
| Example | GCC translating a C program to machine code. | The CPython virtual machine executing Python bytecode. |
| Advantage | The translated result can be optimized and reused. | Interactive execution lets you test a short expression quickly. |

A compiler prepares a different representation of the code for execution. An interpreter uses instructions to perform the program's work at runtime. CPython combines the two approaches by producing bytecode and then executing it in its virtual machine.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

[hello.py](hello.py) and the verified output in this README.

## 8. Commit details

`Run hello.py and compare execution models`. The checkpoint is listed in [this mission's GitHub history](https://github.com/shamkian0326-creator/digital-detective-8545/commits/main/mission-04-programs/README.md).
