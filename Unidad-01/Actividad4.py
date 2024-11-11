import json
import csv

class JSONFileHandler:
    def read_json(self, file_path):
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error leyendo JSON: {e}")
    
    def write_json(self, file_path, data):
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
                print("JSON escrito correctamente.")
        except Exception as e:
            print(f"Error escribiendo JSON: {e}")
    
    def json_to_csv(self, json_file_path, csv_file_path):
        try:
            data = self.read_json(json_file_path)
            
            if data:
                with open(csv_file_path, 'w', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    
                    writer.writerow(data.keys())
                    
                    writer.writerow(data.values())
                
                print(f"JSON convertido a CSV correctamente en {csv_file_path}.")
        except Exception as e:
            print(f"Error convirtiendo JSON a CSV: {e}")
            
json_handler = JSONFileHandler()

data_to_write = {
    "DNI": "77934336D",
    "fecha_de_nacimiento": "28/12/02"
}

json_handler.write_json('data.json', data_to_write)
json_handler.json_to_csv('data.json', 'data.csv')
