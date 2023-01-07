import logging
import string

import pytest

from reverse_file_task2 import reverse_file_in_memory
from stub_io import StubIo

_logger = logging.getLogger(__name__)


def _get_data(size: int) -> bytes:
    values = string.digits + string.ascii_letters
    n_copies = (size + len(values) + 1) // len(values)
    values = (values * n_copies)[:size]
    buf = values.encode()
    assert len(buf) == size
    return buf


@pytest.mark.parametrize('size', [0, 1, 2, 3, 10, 30, 150])
def test_task_2(size):
    data = _get_data(size)
    io = StubIo()
    io.register_file('abc', len(data))
    io.write_file(data, 0, len(data), 'abc', 0)
    _logger.info('Reversing started')
    reverse_file_in_memory(io, 'abc')
    _logger.info('Reversing completed')
    assert io.get_file_content('abc') == bytes(reversed(data))
