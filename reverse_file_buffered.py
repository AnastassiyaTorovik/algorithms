from file_io import Io, FileIo


def reverse_file_in_memory(io: Io, name: str, buf_size: int):
    """Reverse a content of the file `name` using no more than buf_size of additional memory"""
    assert buf_size >= 2, "Minimum allowed buf_size is 2"

    length = io.file_length(name)
    chunk_size = buf_size//2
    output_buff = bytearray(chunk_size*2)
    left_offset = 0
    right_offset = length - chunk_size
    remaining_to_reverse = length

    while left_offset < right_offset:
        io.read_file(name, left_offset, chunk_size, output_buff, 0)
        io.read_file(name, right_offset, chunk_size, output_buff, chunk_size)

        reversed_output_buff = output_buff[::-1]

        io.write_file(reversed_output_buff, 0, chunk_size, name, left_offset)
        io.write_file(reversed_output_buff, chunk_size, chunk_size, name, right_offset)

        left_offset += chunk_size
        right_offset -= chunk_size
        remaining_to_reverse -= chunk_size * 2

    if remaining_to_reverse > 1:
        output_buff = bytearray(remaining_to_reverse)
        io.read_file(name, left_offset, remaining_to_reverse, output_buff, 0)
        reversed_output_buff = output_buff[::-1]
        io.write_file(reversed_output_buff, 0, remaining_to_reverse, name, left_offset)


if __name__ == "__main__":
    reverse_file_in_memory(FileIo(), name='test.txt', buf_size=4)