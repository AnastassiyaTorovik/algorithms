from file_io import Io, FileIo


def reverse_file_in_memory(io: Io, name: str, buf_size: int):
    """Reverse a content of the file `name` using no more than buf_size of additional memory"""
    assert buf_size >= 2, "Minimum allowed buf_size is 2"

    length = io.file_length(name)
    chunk = buf_size//2
    output_buff = bytearray(chunk*2)
    mid = length//2
    left_offset = 0
    right_offset = length - left_offset - min(chunk, mid - left_offset)


    while left_offset < right_offset or 0 < min(chunk, mid - left_offset) < chunk:
        if length <= chunk:
            chunk = length
            output_buff = bytearray(chunk)
            io.read_file(name, left_offset, chunk, output_buff, 0)
            reversed_output_buff = output_buff[::-1]
            io.write_file(reversed_output_buff, 0, chunk, name, left_offset)
            break
        else:
            io.read_file(name, left_offset, chunk, output_buff, 0)
            io.read_file(name, right_offset, chunk, output_buff, chunk)

            reversed_output_buff = output_buff[::-1]

            io.write_file(reversed_output_buff, 0, chunk, name, left_offset)
            io.write_file(reversed_output_buff, chunk, chunk, name, right_offset)

            left_offset += chunk
            right_offset -= chunk


if __name__ == "__main__":
    reverse_file_in_memory(FileIo(), name='test.txt', buf_size=20)