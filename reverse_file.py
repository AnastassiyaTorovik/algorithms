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
        output_buf[:output_buf_offset] = chunk


def write_file(buf: bytearray, buf_offset: int, size: int, output_file: str, output_file_offset: int) -> None:
    """
    Write `size` bytes from `buf` buffer starting from `buf_offset` into `output_file` starting from `output_file_offset`
  """
    with open(output_file, "r+") as f:
        f.seek(output_file_offset)
        f.write(bytes(buf[buf_offset:size]).decode())


def reverse_file_in_memory(name: str):
    length = file_length(name)
    byte_size = length
    output_buff = bytearray()
    offset = 0
    output_buff_offset = 0
    read_file(name, offset, byte_size, output_buff, output_buff_offset)
    write_file(output_buff[::-1], 0, byte_size, name, output_buff_offset)


if __name__ == "__main__":
    file_length = reverse_file_in_memory('test.txt')
