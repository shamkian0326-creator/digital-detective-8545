# Mission 5 — Convert values and examine text encoding

## 1. Task / objective

Show seven conversions on paper, check the answers in Python, build a decimal converter and explain character encoding.

## 2. Work completed

Recorded seven worked conversions and checked them through the Python interactive interpreter. Tested the converter with three positive decimal values and one text input.

## 3. Commands / tools used

`python3 -q -i` evaluated the verification expressions. `input()` reads the typed string and `int(..., 10)` converts the decimal digits to an integer. `bin()` formats that integer in base two with `0b`, and `hex()` formats it in base sixteen with `0x`. `ord()` gives a character's code point.

## 4. My understanding

### 5.1 Manual working

| Conversion | Working | Answer |
| --- | --- | --- |
| Decimal 13 to binary | 13 = 8 + 4 + 1. In the places 8, 4, 2 and 1, mark 1, 1, 0 and 1. | `1101` |
| Decimal 25 to binary | 25 = 16 + 8 + 1. In the places 16, 8, 4, 2 and 1, mark 1, 1, 0, 0 and 1. | `11001` |
| Binary 1010 to decimal | 1×8 + 0×4 + 1×2 + 0×1 = 10. | `10` |
| Binary 1101 to decimal | 1×8 + 1×4 + 0×2 + 1×1 = 13. | `13` |
| Hexadecimal A to decimal | A means ten in the units place, so 10×16⁰ = 10. | `10` |
| Hexadecimal 1F to decimal | F means fifteen, so 1×16 + 15×1 = 31. | `31` |
| Binary 1111 to hexadecimal | 8 + 4 + 2 + 1 = 15. In hexadecimal, the single digit for fifteen is F. | `F` |

Each binary place represents a power of two. Each hexadecimal place represents a power of sixteen.

### 5.2 Python verification

| Expression | Result | Matches? |
| --- | --- | --- |
| `bin(13)` | `'0b1101'` | Yes |
| `bin(25)` | `'0b11001'` | Yes |
| `int('1010', 2)` | `10` | Yes |
| `int('1101', 2)` | `13` | Yes |
| `int('A', 16)` | `10` | Yes |
| `int('1F', 16)` | `31` | Yes |
| `hex(int('1111', 2))` | `'0xf'` | Yes |
| `hex(15)` | `'0xf'` | Yes |

### 5.3 Converter results

Run `python3 number_converter.py` from this mission directory. The converter parses the input once, then displays the binary and hexadecimal versions of the same value.

| Decimal input | Binary output | Hexadecimal output |
| --- | --- | --- |
| 7 | `0b111` | `0x7` |
| 16 | `0b10000` | `0x10` |
| 31 | `0b11111` | `0x1f` |

The input `abc` produced `Enter an integer in decimal digits.`

### 5.4 Text encoding

The ASCII decimal codes are **65** for `A` and **97** for `a`. An encoding defines which bytes represent a character so a saved file can be decoded consistently by another program. The rupee sign `₹` is outside basic ASCII and occupies three bytes in UTF-8.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

[number_converter.py](number_converter.py), the manual calculations, the Python results and the converter tests above.

## 8. Commit details

`Build the converter and check number representations`. The checkpoint is listed in [this mission's GitHub history](https://github.com/shamkian0326-creator/digital-detective-8545/commits/main/mission-05-numbers-data/README.md).
