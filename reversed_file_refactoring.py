import os


class FileReverser:
    def __init__(self, file_name: str, memory_constraint: int):
        self.name = file_name
        self.size = memory_constraint // 2  # divided by two as we will be traversing the file from both ends
        self.output_buff = bytearray(memory_constraint)
        self.left_offset = 0
        self.right_offset = self.file_length() - self.size

    def file_length(self) -> int:
        length = os.stat(self.name).st_size
        return length

    def read_file(self, read_offset: int, output_buf_offset: int) -> None:
        """
        Reads `size` bytes from file `name` starting from `offset` index and
        stores them into `output_buf` starting from `output_buf_offset`
      """
        with open(self.name, "rb") as f:
            f.seek(read_offset)
            chunk = f.read(self.size)
            self.output_buff[output_buf_offset:] = chunk

    def write_file(self, buf_offset: int, output_file_offset: int) -> None:
        """
        Write `size` bytes from `buf` buffer starting from `buf_offset` into `output_file` starting from `output_file_offset`
      """
        with open(self.name, "r+b") as f:
            f.seek(output_file_offset)
            f.write(bytes(self.output_buff[buf_offset:buf_offset + self.size]))

    def reverse_file_in_memory(self):
        """Reverse a content of the file `name` holding in memory no more than n bytes
        from the file at each given time."""

        while self.left_offset < self.right_offset:
            self.read_file(self.left_offset, 0)
            self.read_file(self.right_offset, self.size)

            self.output_buff = self.output_buff[::-1]

            self.write_file(0, self.left_offset)
            self.write_file(self.size, self.right_offset)

            self.left_offset += self.size
            self.right_offset -= self.size


if __name__ == "__main__":
    FileReverser(file_name='test.txt', memory_constraint=2).reverse_file_in_memory()