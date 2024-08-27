# __iter__(self)
# __next__(self)

import sys
from itertools import repeat

ex_itertator = repeat('4', 100_000)
print(ex_itertator)
print(f'Размер интератора - {sys.getsizeof(ex_itertator)}')

ex_str = '4' * 100_100
print(f'Размер списка - {sys.getsizeof(ex_str)}')



