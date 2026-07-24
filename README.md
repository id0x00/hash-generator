# hash-generator
A Python tool that generates MD5, SHA-1, SHA-256 and SHA-512 hashes from user input.


## Features

- Generates MD5 hashes
- Generates SHA-1 hashes
- Generates SHA-256 hashes
- Generates SHA-512 hashes
- Supports generating all hashes at once
- Simple command-line interface

## Usage

Run:

```bash
python3 hash_generator.py
```

Example:

```text
Available algorithms:
1 = MD5
2 = SHA-1
3 = SHA-256
4 = SHA-512
5 = all of the above

Please enter desired hashing algorithm:
5

Please enter your text:
hello

MD5: 5d41402abc4b2a76b9719d911017c592
SHA1: aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
SHA-256: 2cf24dba5fb0a30e26e83b2ac5b9e29e...
SHA-512: 9b71d224bd62f3785d96d46ad3ea3d73...
```
