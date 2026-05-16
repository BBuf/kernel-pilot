from quack.cute_dsl_utils import ArgumentsBase
from typing import Optional
from dataclasses import dataclass
from cutlass.cute import Tensor


@dataclass
class VarlenArguments(ArgumentsBase):
    mCuSeqlensM: Optional[Tensor] = None
    mTensormaps: Optional[Tensor] = None
