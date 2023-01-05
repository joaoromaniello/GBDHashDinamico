import struct

class FileManager:
    def __init__(self, main_file: str, index_file: str):
        self.main_file = main_file
        self.index_file = index_file

    def insert_record(self, record: str, key: int):
        with open("dataFiles/"+self.main_file, 'a') as f:
            f.write(str(record))
        with open("dataFiles/"+self.index_file, 'a') as f:
            offset = f.tell()
            f.write(str(struct.pack('iQ', key, offset)))
    def delete_record(self, key: int):
        with open(self.index_file, 'rb') as f:
            while True:
                data = f.read(12)
                if not data:
                    break
                key_read, offset = struct.unpack('iq', data)
                if key_read == key:
                    f.seek(-12, 1)
                    f.write(b'\x00' * 12)
                    with open(self.main_file, 'rb+') as main_f:
                        main_f.seek(offset)
                        main_f.write(b'\x00' * len(record))
                    return
        print('Key not found.')

    def update_record(self, key: int, new_record: str):
        with open(self.index_file, 'rb') as f:
            while True:
                data = f.read(12)
                if not data:
                    break
                key_read, offset = struct.unpack('iQ', data)
                if key_read == key:
                    with open(self.main_file, 'rb+') as main_f:
                        main_f.seek(offset)
                        main_f.write(new_record.encode())
                    return
        print('Key not found.')

    def search_record(self, key: int) -> str:
        with open(self.index_file, 'rb') as f:
            while True:
                data = f.read(12)
                if not data:
                    break
                key_read, offset = struct.unpack('iQ', data)
                if key_read == key:
                    with open(self.main_file, 'rb') as main_f:
                        main_f.seek(offset)
                        return main_f.read().decode()
        return 'Key not found.'