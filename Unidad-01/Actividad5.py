import json

class JSONFileHandler:
    def read_json(self, file_path):
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print("Error leyendo JSON: ", e)
    

    def write_json(self, file_path, data):
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
                print("JSON escrito correctamente.")
        except Exception as e:
            print("Error escribiendo JSON: " , e)


json_handler = JSONFileHandler()

data_to_write = {
    "DNI": "77934336D",
    "fecha_de_nacimiento": "28/12/02"
}

json_handler.write_json('data.json', data_to_write)

data = json_handler.read_json('data.json')
print(data)

