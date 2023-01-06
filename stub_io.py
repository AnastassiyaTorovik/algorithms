import logging

from file_io import Io

_logger = logging.getLogger(__name__)


class _StubIoHandler:
    def __init__(self, name: str, data: bytearray):
        self.name = name
        self.data = data

    def file_length(self) -> int:
        return len(self.data)

    def read_file(self, offset: int, size: int, output_buf: bytearray, output_buf_offset: int) -> None:
        assert offset >= 0
        assert offset + size <= self.file_length()
        assert output_buf_offset >= 0
        assert output_buf_offset + size <= len(output_buf)
        output_buf[output_buf_offset:output_buf_offset+size] = self.data[offset:offset+size]
        _logger.info(f'read({self.name}, {offset}, {size}) -> "{self.data[offset:offset+size].decode()}"')

    def write_file(self, buf: bytes, buf_offset: int, size: int, output_file_offset: int) -> None:
        assert buf_offset >= 0
        assert buf_offset + size <= len(buf)
        assert output_file_offset >= 0
        assert output_file_offset + size <= len(self.data)
        data_before = self.data.decode()
        self.data[output_file_offset:output_file_offset + size] = buf[buf_offset:buf_offset + size]
        _logger.info(f'write({self.name}, {output_file_offset}, {size})\n'
                     f'    before     "{data_before}"\n'
                     f'    new data   {" " * output_file_offset}"{buf[buf_offset:buf_offset + size].decode()}"\n'
                     f'    after      "{self.data.decode()}"')


class StubIo(Io):
    def __init__(self):
        self._files = {}

    def register_file(self, name: str, size: int):
        assert name not in self._files
        self._files[name] = _StubIoHandler(name, bytearray(size))
        _logger.info(f'register_file({name}, {size})')

    def file_length(self, name: str) -> int:
        return self._get_handler(name).file_length()

    def read_file(self, name: str, offset: int, size: int, output_buf: bytearray, output_buf_offset: int) -> None:
        self._get_handler(name).read_file(offset, size, output_buf, output_buf_offset)

    def write_file(self, buf: bytes, buf_offset: int, size: int, output_file: str, output_file_offset: int) -> None:
        self._get_handler(output_file).write_file(buf, buf_offset, size, output_file_offset)

    def get_file_content(self, name: str) -> bytearray:
        return self._get_handler(name).data

    def _get_handler(self, name: str) -> _StubIoHandler:
        try:
            return self._files[name]
        except KeyError:
            raise FileNotFoundError(f'Unknown file {name}') from None


def main():
    logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.DEBUG)
    io = StubIo()
    io.register_file('a', 10)
    data = '01234567'.encode()
    io.write_file(data, 2, 4, 'a', 0)
    io.write_file(data, 0, 8, 'a', 2)
    b = bytearray(5)
    io.read_file('a', 4, 3, b, 2)


if __name__ == '__main__':
    main()
