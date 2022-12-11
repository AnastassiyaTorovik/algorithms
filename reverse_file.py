import os


def file_length(name: str) -> int:
    length = os.stat(name).st_size
    return length


def read_file(name: str, offset: int, size: int, output_buf_offset: int) -> bytearray:
    """
    Reads `size` bytes from file `name` starting from `offset` index and
    stores them into `output_buf` starting from `output_buf_offset`
  """
    with open(name, "rb") as f:
        f.seek(offset)
        chunk = f.read(size)
        output_buf = bytearray(chunk[output_buf_offset:])
        return output_buf


def write_file(buf: bytearray, buf_offset: int, size: int, output_file: str, output_file_offset: int) -> None:
    """
    Write `size` bytes from `buf` buffer starting from `buf_offset` into `output_file` starting from `output_file_offset`
  """
    with open(output_file, "r+b") as f:
        f.seek(output_file_offset)
        f.write(bytes(buf[buf_offset:size]))


def reverse_file_in_memory(name: str):
    byte_size = 2
    length = file_length(name)
    mid_index = length // 2
    left_offset = 0
    right_offset = length - byte_size

    while True:
        if left_offset >= mid_index:
            break

        left_chunk = read_file(name, left_offset, byte_size, 0)[::-1]
        right_chunk = read_file(name, right_offset, byte_size, 0)[::-1]

        left_chunk, right_chunk = right_chunk, left_chunk
        write_file(left_chunk, 0, byte_size, name, left_offset)
        write_file(right_chunk, 0, byte_size, name, right_offset)

        left_offset += byte_size
        right_offset -= byte_size


if __name__ == "__main__":
    file_length = reverse_file_in_memory('test.txt')
