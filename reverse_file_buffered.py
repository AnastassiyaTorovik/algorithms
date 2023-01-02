from file_io import Io, FileIo


def reverse_file_in_memory(io: Io, name: str, buf_size: int):
    """Reverse a content of the file `name` using no more than buf_size of additional memory"""
    assert buf_size >= 2, "Minimum allowed buf_size is 2"

    length = io.file_length(name)
    byte_size = buf_size//2
    output_buff = bytearray(buf_size)
    left_offset = 0
    right_offset = length - byte_size if length >= byte_size else length
    remaining_to_reverse = length

    while left_offset <= right_offset:
        io.read_file(name, left_offset, byte_size, output_buff, 0)
        io.read_file(name, right_offset, byte_size, output_buff, byte_size)

        reversed_output_buff = output_buff[::-1]

        io.write_file(reversed_output_buff, 0, byte_size, name, left_offset)
        io.write_file(reversed_output_buff, byte_size, byte_size, name, right_offset)

        left_offset += byte_size
        right_offset -= byte_size
        remaining_to_reverse -= byte_size * 2
    else:
        # reverse remaining characters
        if remaining_to_reverse > 1:
            io.read_file(name, left_offset, remaining_to_reverse, output_buff, 0)
            reversed_output_buff = output_buff[::-1]
            io.write_file(reversed_output_buff, 0, remaining_to_reverse, name, left_offset)


if __name__ == "__main__":
    reverse_file_in_memory(FileIo(), name='test.txt', buf_size=5)