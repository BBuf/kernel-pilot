# 🦆 QuACK: A Quirky Assortment of CuTe Kernels 🦆

Kernels are written in the [CuTe-DSL](https://docs.nvidia.com/cutlass/media/docs/pythonDSL/cute_dsl_general/dsl_introduction.html).

## Installation

``` bash
pip install quack-kernels
```

## Requirements

- H100 or B200 GPU
- CUDA toolkit 12.9+
- Python 3.12

## Kernels 🐥

- 🦆 RMSNorm forward
- 🦆 Softmax forward + backward
- 🦆 Cross entropy forward + backward
- 🦆 Layernorm forward

Upcoming:
- 🦆 RMSNorm backward
- 🦆 Rotary forward + backward

## Usage

```
from quack import rmsnorm, softmax, cross_entropy
```

## Caveats 🦆⚠️

**Tensor Size Limitation**: We currently only support tensors ≤ 4GB due to CuTe-DSL using int32 for indexing.

🦆 **Workaround**: For larger tensors, split your input tensors into chunks of
size ≤ 4GB each. We will implement this automatic chunking in the pytorch part
of the code in the near future, but if you need it in the meantime, we welcome contributions!

## Development

To set up the development environment:

```bash
pip install -e '.[dev]'
pre-commit install
```
