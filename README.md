# Protocol Buffer - Python Example

Based on [this](https://developers.google.com/protocol-buffers/docs/pythontutorial) tutorial.

## Install

- [Download](https://github.com/protocolbuffers/protobuf/releases) protobuf for your platform
  - e.g. protoc-3.17.3-win64.zip for Windows
- Extract it and add the binary to your $PATH
  - e.g. C:\protoc-3.17.3-win64\bin on Windows
- Make sure it is installed
```sh
protoc --version
```
- Install protobuf's Python package

```sh
conda install protobuf
```

- Run protobuf's compiler (protoc)

```sh
protoc -I=$SRC_DIR --python_out=$DST_DIR $SRC_DIR/addressbook.proto
```
where $SRC_DIR is the repository directory and $DST_DIR in where the new Python file will be created.

Example:

```sh
protoc -I=C:\repos\protobuf-example --python_out=C:\repos\protobuf-example C:\repos\protobuf-example\addressbook.proto
```

## Run

```sh
python test_addressbook.py ADDRESS_BOOK_FILE
```

where ADDRESS_BOOK_FILE is the protobuf file that will be created / used for serialization.