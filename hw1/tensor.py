from typing import TypeVar, Union
from math import prod

T = TypeVar('T')

class Tensor:
    def __init__(self, dimension: Union[int, tuple[int, ...]], data: list[T]):
        if isinstance(dimension, int):
            if dimension <= 0:
                raise ValueError("dimension must be positive integer")
        elif isinstance(dimension,tuple):
            if not all(isinstance(value, int) and value > 0 for value in dimension):
                raise ValueError('dimension must consist of positive integers')
        else:
            raise ValueError("dimension must be int or tuple[int, ...]")
        if isinstance(data, list):
            if  (dimension if isinstance(dimension,int) else prod(list(dimension))) != len(data):
                raise ValueError('Size of data must match dimension')
            t = type(data[0])
            if not all(isinstance(value, t) for value in data):
                raise ValueError('All elements in data must be of the same type')
        else:
            raise ValueError('data must be a list')
        
        self.dimension = dimension
        self.data = data
        
    def __repr__(self):
        return str(self.data)
