import torch
from typing import List


def transform_basis(B: List[List[float]], C: List[List[float]]) -> List[List[float]]:
    """Return the change-of-basis matrix **P = C⁻¹ B**.

    - *B*, *C* may be 2×2 or 3×3 nested lists.
    - Result is rounded to 4 decimals and returned as a nested list.
    """
    # Your implementation here
    C_inv = torch.linalg.inv(torch.tensor(C, dtype=torch.float64));
    ans = torch.matmul(C_inv, torch.tensor(B, dtype=torch.float64));
    return ans.tolist();
    pass
