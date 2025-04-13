# HexDeal

**HexDeal** is a Python script for encoding, decoding, and editing hexadecimal ASCII strings. It provides a flexible way to convert strings to hex (and vice versa), with optional transformations like reversing, splitting, and adding human-readable annotations.

## Features

- Encode plain text into hexadecimal.
- Decode hexadecimal strings into ASCII.
- Reverse byte order.
- Split hex data into specified character-length chunks.
- Annotate hex values with ASCII comments.
- Customize comment symbols.
- Choose to exclude `0x` prefixes.

## Installation

No installation needed — just make sure you have Python 3 installed. Then, make the script executable:

```bash
chmod +x hexdeal.py
```

Or run it with Python directly:

```bash
python3 hexdeal.py ...
```

## Usage

```bash
hexdeal.py MODE DATA [OPTIONS]
```

### Modes

- `hex`: Convert text to hexadecimal.
- `unhex`: Convert hexadecimal back to text.
- `edit`: Modify the format of hexadecimal strings.

### Options

| Option             | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| `-rev`             | Reverse the input (for decoding or reversing byte order in chunks).         |
| `-cut N`           | Cut output into chunks of N character bytes.                                |
| `-comment`         | Annotate output with ASCII string representation.                           |
| `-comment-symbol`  | Symbol to use for comments (default: `;`).                                  |
| `-no-prefix`       | Omit the `0x` prefix in output.                                             |

## Examples

### Encode to Hex

```bash
./hexdeal.py hex "Hello World!"
```

```
0x48656c6c6f20576f726c6421
```

### Encode with Reverse

```bash
./hexdeal.py hex "Hello World!" -rev
```

```
0x1246c627f67502f6c6c65684
```

### Encode with Multiple Options

```bash
./hexdeal.py hex "Hello World!" -rev -cut 4 -comment -comment-symbol ";" -rev-bytes
```

```
0x1246c627 ; !dlr
0xf67502f6 ; oW o
0xc6c65684 ; lleH
```

### Decode from Hex

```bash
./hexdeal.py unhex "0x48656c6c6f20576f726c6421"
```

```
Hello World!
```

### Decode with Reverse

```bash
./hexdeal.py unhex "1246c627f67502f6c6c65684" -rev
```

```
Hello World!
```

### Edit an Existing Hex String

```bash
./hexdeal.py edit "0x1246c627f67502f6c6c65684" -cut 4 -no-prefix
```

```
1246c627
f67502f6
c6c65684
```

## Notes

- HexDeal does **not** deal with converting hexadecimal to integer values.
- Works with piped data if no direct input is given.

## License

MIT License
