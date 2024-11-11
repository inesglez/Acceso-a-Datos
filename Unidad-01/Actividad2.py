class FileHandler:
    def read_file(self, file_path, mode='r'):
        try:
            with open(file_path, mode) as f:
                content = f.read()
                return content
        except Exception as e:
            print(f"Error leyendo el archivo: {e}")
    def write_file(self, file_path, content, mode='w'):
        try:
            with open(file_path, mode) as f:
                f.write(content)
        except Exception as e:
            print(f"Error escribiendo en el archivo: {e}")

file = FileHandler()
file.write_file('77934336D.txt',"28/12/2002")

print(file.read_file('77934336D.txt'))
