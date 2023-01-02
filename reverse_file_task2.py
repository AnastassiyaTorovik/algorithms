from file_io import Io, FileIo


def reverse_file_in_memory(io: Io, name: str):
    """Reverse a content of the file `name` holding in memory no more than 2 bytes from the file at each given time. As
     chunks are loaded from the beginning of the file and from the end, each of these chunks must be just 1 byte"""
    memory_constraint = 2
    length = io.file_length(name)
    byte_size = int(memory_constraint/2)
    output_buff = bytearray(memory_constraint)
    left_offset = 0
    right_offset = length - byte_size

    while left_offset < right_offset:
        io.read_file(name, left_offset, byte_size, output_buff, 0)
        io.read_file(name, right_offset, byte_size, output_buff, byte_size)

        reversed_output_buff = output_buff[::-1]

        io.write_file(reversed_output_buff, 0, byte_size, name, left_offset)
        io.write_file(reversed_output_buff, byte_size, byte_size, name, right_offset)

        left_offset += byte_size
        right_offset -= byte_size


if __name__ == "__main__":
    reverse_file_in_memory(FileIo(), name='test.txt')