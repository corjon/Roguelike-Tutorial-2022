from typing import Tuple

import numpy as np # type: ignore

# dtype creates data type which numpy can use
graphic_dt = np.dtype(
    [
        ("ch", np.int32), # char
        ("fg", "3B"), # foreground color
        ("bg", "3B"), # background color
    ]
)

# dtype used in actual tile
tile_dt = np.dtype(
    [
        ("walkable", np.bool), 
        ("transparent", np.bool), 
        ("dark", graphic_dt),
    ]
)

# helper function to define tile types
# creates numpy array of one tile_dt and returns it
def new_tile(
    *, # enfoce the use of keywords
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    return np.array((walkable, transparent, dark), dtype = tile_dt)

#actual tile types
floor = new_tile(
    walkable = True, transparent = True, dark = (ord(" "), (255, 255, 255), (50, 50, 150)),
)
wall = new_tile(
    walkable = False, transparent = False, dark = (ord(" "), (255, 255, 255), (0, 0, 100)),
)