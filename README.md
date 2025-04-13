# HexDeal

**HexDeal** is a Python script that simplifies the process of encoding, decoding, and editing hexadecimal ASCII strings. It provides a command-line interface to transform strings to hex and vice versa, with options for reversing, chunking, and inline commenting.

## Features

- Convert ASCII text to hexadecimal (`hex` mode)
- Decode hexadecimal to ASCII text (`unhex` mode)
- Format or re-chunk hex strings (`edit` mode)
- Reverse byte order of hex strings
- Annotate hex chunks with ASCII representation
- Customize comment symbols
- Remove `0x` prefix if desired

## Installation

Ensure you have Python 3 installed. Then either run the script directly or make it executable:

```bash
chmod +x hexdeal.py
./hexdeal.py ...
```

Or:

```bash
python3 hexdeal.py ...
```

## Usage

```bash
hexdeal.py MODE DATA [OPTIONS]
```

### Modes

- `hex` – Convert text to hex
- `unhex` – Convert hex to text
- `edit` – Format/edit an existing hex string

### Options

| Option             | Description                                                            |
|--------------------|------------------------------------------------------------------------|
| `-rev`             | Reverse the input or byte order                                        |
| `-cut N`           | Split output into chunks of N character bytes                          |
| `-comment`         | Annotate output with corresponding ASCII strings                       |
| `-comment-symbol`  | Specify a symbol for comments (default: `;`)                           |
| `-no-prefix`       | Do not add the `0x` prefix in output                                   |

## Examples

### Convert text to hex

```bash
./hexdeal.py hex 'Hello World!'
```

```
0x48656c6c6f20576f726c6421
```

### Reverse text before converting to hex

```bash
./hexdeal.py hex 'Hello World!' -rev
```

```
0x21646c726f57206f6c6c6548
```

### Chunk and annotate reversed hex

```bash
./hexdeal.py hex 'Hello World!' -rev -cut 4 -comment -comment-symbol ";"
```

```
0x21646c72 ; !dlr
0x6f57206f ; oW o
0x6c6c6548 ; lleH
```

### Decode a hex string

```bash
./hexdeal.py unhex "0x48656c6c6f20576f726c6421"
```

```
Hello World!
```

### Reverse-decode a hex string

```bash
./hexdeal.py unhex "21646c726f57206f6c6c6548" -rev
```

```
Hello World!
```

### Reformat a hex string

```bash
./hexdeal.py edit "0x21646c726f57206f6c6c6548" -cut 4 -no-prefix
```

```
21646c72
6f57206f
6c6c6548
```

## Notes

- This script does **not** handle conversion to or from integer values.
- Supports piped input if `DATA` is omitted in interactive shell.
- Use `-comment` only with `hex` and `edit` modes (not `unhex`).

## License

MIT License
