from file_io import Io, FileIo


def reverse_file_in_memory(io: Io, name: str, buf_size: int):
    """Reverse a content of the file `name` using no more than buf_size of additional memory"""
    assert buf_size >= 2, "Minimum allowed buf_size is 2"

    length = io.file_length(name)
    chunk = min(buf_size//2, max(length-buf_size//2, 1))
    output_buff = bytearray(min(chunk*2, length))
    mid = length//2
    left_offset = 0
    right_offset = length - left_offset - min(chunk, max(mid - left_offset, max(length-buf_size//2, 1)))


    while left_offset < right_offset:
        io.read_file(name, left_offset, chunk, output_buff, 0)
        io.read_file(name, right_offset, chunk, output_buff, chunk)

        output_buff.reverse()

        io.write_file(output_buff, len(output_buff)-2*chunk, chunk, name, left_offset)
        io.write_file(output_buff, len(output_buff)-chunk, chunk, name, right_offset)

        left_offset += chunk
        chunk = min(chunk, max((mid - left_offset),1))
        right_offset -= chunk


if __name__ == "__main__":
    reverse_file_in_memory(FileIo(), name='test.txt', buf_size=3
                           )