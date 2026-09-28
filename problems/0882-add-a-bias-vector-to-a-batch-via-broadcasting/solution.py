import torch

def add_bias(x: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    # TODO: add b to every row of x using broadcasting
    for t in x:
        t += b;
    return x;
    pass
