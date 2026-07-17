# grpc

Repository for experimenting with gRPC.

## Prerequisites

- Python 3
- [uv](https://docs.astral.sh/uv/) for managing the virtual environment

## Setup

Create a virtual environment and install the gRPC tools:

```bash
uv venv
uv pip install grpcio-tools
```

## Compile the .proto File

Use the `grpc_tools.protoc` module (it bundles the gRPC Python plugin, so no
separate `protoc` installation is required):

```bash
uv run python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. mmo.proto
```

