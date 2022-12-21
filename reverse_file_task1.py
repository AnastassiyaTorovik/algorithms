import os


def file_length(name: str) -> int:
    length = os.stat(name).st_size
    return length


def read_file(name: str, offset: int, size: int, output_buf: bytearray, output_buf_offset: int) -> None:
    """
    Reads `size` bytes from file `name` starting from `offset` index and
    stores them into `output_buf` starting from `output_buf_offset`
  """
    with open(name, "rb") as f:
        f.seek(offset)
        chunk = f.read(size)
        output_buf[output_buf_offset:] = chunk


def write_file(buf: bytearray, buf_offset: int, size: int, output_file: str, output_file_offset: int) -> None:
    """
    Write `size` bytes from `buf` buffer starting from `buf_offset` into `output_file` starting from `output_file_offset`
  """
    with open(output_file, "r+b") as f:
        f.seek(output_file_offset)
        f.write(bytes(buf[buf_offset:buf_offset+size]))


def reverse_file_in_memory(name: str):
    """Reverse a content of the file `name`. Whole file is loaded into memory"""
    length = file_length(name)
    output_buff = bytearray(length)
    offset = 0
    read_file(name, offset, length, output_buff, offset)
    write_file(output_buff[::-1], offset, length, name, offset)


if __name__ == "__main__":
    reverse_file_in_memory(name='test.txt')
