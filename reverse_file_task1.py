from file_io import Io, FileIo


def reverse_file_in_memory(io: Io, name: str):
    """Reverse a content of the file `name`. Whole file is loaded into memory"""
    length = io.file_length(name)
    output_buff = bytearray(length)
    offset = 0
    io.read_file(name, offset, length, output_buff, offset)
    io.write_file(output_buff[::-1], offset, length, name, offset)


if __name__ == "__main__":
    reverse_file_in_memory(FileIo(), name='test.txt')
