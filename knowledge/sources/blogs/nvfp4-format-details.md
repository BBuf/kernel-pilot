---
id: blog-nvfp4-format-details
title: "NVFP4 Format Details"
author: Harold Benoit
url: https://haroldbenoit.com/notes/ml/engineering/precision/nvfp4-format
source_category: community-note
architectures: [sm100, sm100a]
tags: [nvfp4, fp4, block-scale, fine-grained-quantization, quantization]
retrieved_at: 2026-04-17
---

# NVFP4 Format Details (Harold Benoit)

## Overview

Harold Benoit's detailed technical note on the NVFP4 (NVIDIA FP4) numeric format specification, covering the E2M1 bit layout, block-level scaling with E4M3 scale factors, quantization and dequantization procedures, and comparison with the MXFP4 standard. This is one of the most accessible references for understanding the exact NVFP4 data representation used in Blackwell tensor cores.

## Bit Layout: E2M1 Format

Each NVFP4 element is encoded in 4 bits using the E2M1 format:
- 1 sign bit
- 2 exponent bits
- 1 mantissa bit

### Representable Values

The E2M1 format can encode exactly 16 values:
- Positive: 0, 0.5, 1, 1.5, 2, 3, 4, 6
- Negative: -0, -0.5, -1, -1.5, -2, -3, -4, -6
- Maximum magnitude: 6

## Block Structure

NVFP4 uses a two-level microscaling architecture:

### Block-Level Scale
- **Block size**: 16 contiguous FP4 elements (half of MXFP4's 32)
- **Scale format**: E4M3 (8-bit floating point), covering range [-448, 448]
- Smaller blocks provide finer-grained scaling, better fitting values into the FP4 representable range

### Tensor-Level Scale
- **Format**: FP32 (single-precision floating point)
- Provides dynamic range extension across the entire tensor
- Computed once per tensor, shared by all blocks

## Quantization Process

The two-level microscaling quantization works as follows:

1. **Per-block maximum**: amax(b) = max|x_i| within each 16-element block
2. **Global FP32 scale**: s_m = max_b(amax(b)) / (6 * 448)
3. **Block E4M3 scale**: s_b = cast_E4M3((amax(b) / s_m) / 6)
4. **Element quantization**: q_i = cast_FP4(x_i / (s_m * s_b))

## Dequantization Formula

Reconstruction applies the scaling hierarchy in reverse:

```
x_hat_i = s_m * s_b * deq_FP4(q_i)
```

Where s_m is the FP32 tensor-level scale, s_b is the E4M3 block-level scale, and deq_FP4 maps the 4-bit code back to the corresponding floating-point value.

## NVFP4 vs MXFP4 Comparison

| Aspect | MXFP4 | NVFP4 |
|--------|-------|-------|
| Element format | E2M1 | E2M1 (same) |
| Block size | 32 elements | 16 elements |
| Scale format | UE8M0 (power-of-2 only) | E4M3 (mantissa bits) |
| Scale range | 2^-127 to 2^127 | [-448, 448] |
| Tensor-level scale | None | FP32 |
| Precision | All FP4 | ~6.25% near-FP8 (amax values) |

### Key Advantages of NVFP4

- **Smaller blocks**: 16 vs 32 elements narrows the dynamic range within each block, better fitting values into the FP4 range
- **E4M3 scale format**: Unlike MXFP4's power-of-two-only UE8M0 scales, E4M3 has mantissa bits that enable non-power-of-two scale factors for finer granularity
- **Tensor-level FP32 scale**: Provides an additional level of dynamic range adjustment that MXFP4 lacks
- **Hardware native**: Direct support in Blackwell tensor cores (tcgen05) without software emulation

## Memory Layout

In memory, NVFP4 data is stored as:
- FP4 data tensor: packed 2 elements per byte (4 bits each)
- Scale tensor: one E4M3 value per 16 FP4 elements
- Global scale: single FP32 value per tensor

The overhead of scale factors is 1 byte per 16 elements = 6.25% overhead, compared to MXFP4's 1 byte per 32 elements = 3.125% overhead. The trade-off is better quantization accuracy from finer-grained scaling.
