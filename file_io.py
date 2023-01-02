import os
from abc import ABC, abstractmethod


class Io(ABC):
    """
    This interface provides access to the underlying IO library.
    Note that we implement it manually just for that task.
    Normal Python IO functions are more powerful.
    """

    @abstractmethod
    def file_length(self, name: str) -> int:
        pass

    @abstractmethod
    def read_file(self, name: str, offset: int, size: int, output_buf: bytearray, output_buf_offset: int) -> None:
        pass

    @abstractmethod
    def write_file(self, buf: bytearray, buf_offset: int, size: int, output_file: str, output_file_offset: int) -> None:
        pass


class FileIo(Io):

    def file_length(self, name: str) -> int:
        return _file_length(name)

    def read_file(self, name: str, offset: int, size: int, output_buf: bytearray, output_buf_offset: int) -> None:
        _read_file(name, offset, size, output_buf, output_buf_offset)

    def write_file(self, buf: bytearray, buf_offset: int, size: int, output_file: str, output_file_offset: int) -> None:
        _write_file(buf, buf_offset, size, output_file, output_file_offset)


def _file_length(name: str) -> int:
    length = os.stat(name).st_size
    return length


def _read_file(name: str, offset: int, size: int, output_buf: bytearray, output_buf_offset: int) -> None:
    """
    Reads `size` bytes from file `name` starting from `offset` index and
    stores them into `output_buf` starting from `output_buf_offset`
  """
    with open(name, "rb") as f:
        f.seek(offset)
        chunk = f.read(size)
        output_buf[output_buf_offset:] = chunk


def _write_file(buf: bytearray, buf_offset: int, size: int, output_file: str, output_file_offset: int) -> None:
    """
    Write `size` bytes from `buf` buffer starting from `buf_offset` into `output_file` starting from `output_file_offset`
  """
    with open(output_file, "r+b") as f:
        f.seek(output_file_offset)
        f.write(bytes(buf[buf_offset:buf_offset + size]))
