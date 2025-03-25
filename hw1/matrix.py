from typing import Union
from tensor import Tensor

class Matrix(Tensor):
    def __init__(self, dimension: tuple[int,int], data):
        if not isinstance(dimension, tuple) or len(dimension) != 2:
            raise ValueError('dimension must be tuple[int, int]')
        
        super().__init__(dimension, data)

        self.rows_cnt, self.columns_cnt = dimension
    
    def conv_rc2i(self, row: int, column: int) -> int:
        if not (0 <= row < self.rows_cnt and 0 <= column < self.columns_cnt):
            raise ValueError('Invalid arguments')
        
        return row * self.columns_cnt + column
    
    def conv_i2rc(self, index: int) -> tuple[int, int]:
        if not 0 <= index < len(self.data):
            raise ValueError('Invalid index')
        
        return (index // self.rows_cnt, index % self.rows_cnt)
    
    def __str__(self):
        d = max(len(str(value)) for value in self.data)
        rows = []
        for row in range(self.rows_cnt):
            row_str = "  ".join(f"{self.data[self.conv_rc2i(row, i)]:>{d}}" for i in range(self.columns_cnt))
            rows.append(" " + row_str)
        return "[\n" + "\n\n".join(rows) + "\n]"
    
    def __getitem__(self, key: Union[int, list[int], slice, tuple[Union[int, list, slice], Union[int, list, slice]]]) -> any:

        def convert_key(key, size) -> list[int]:
            if isinstance(key, int):
                return [key] if key > 0 else [key + size]
            if isinstance(key, slice):
                return list(range(*key.indices(size)))
            if isinstance(key, list):
                return key
            raise TypeError('Invalid key')

        if isinstance(key, (int, list, slice, tuple)):
            row_key, column_key = None, None
            if isinstance(key, tuple):
                if len(key) != 2:
                    raise TypeError('Invalid key') 
            
                if isinstance(key[0], int) and isinstance(key[1], int):
                    return self.data[self.conv_rc2i(key[0], key[1])]
            
                row_key = convert_key(key[0], self.rows_cnt)
                column_key = convert_key(key[1], self.columns_cnt)
            else:
                row_key = convert_key(key, self.rows_cnt)
                column_key = convert_key(slice(None), self.columns_cnt)

            selected = []
            for row in row_key:
                selected.extend(self.data[self.conv_rc2i(row, column)] for column in column_key)
            return Matrix((len(row_key), len(column_key)), selected)
        
        raise TypeError('Invalid key') 