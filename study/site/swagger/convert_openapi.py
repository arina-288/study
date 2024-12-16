import json
import yaml

def convert_json_to_yaml(json_file_path, yaml_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    with open(yaml_file_path, 'w') as yaml_file:
        yaml.dump(data, yaml_file, default_flow_style=False)

if __name__ == "__main__":
    input_json_file = 'openapi.json'
    output_yaml_file = 'openapi.yaml'

    convert_json_to_yaml(input_json_file, output_yaml_file)
    print(f"Conversion complete. Output saved to {output_yaml_file}")