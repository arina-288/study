import yaml

def convert_yaml_to_asciidoc(yaml_file, adoc_file):
    try:
        with open(yaml_file, 'r', encoding='utf-8') as file:
            api_spec = yaml.safe_load(file)

        with open(adoc_file, 'w', encoding='utf-8') as file:
            # Заголовок
#            title = api_spec['info']['title']
#            version = api_spec['info']['version']
#            file.write(f"= {title}\n:version: {version}\n\n")

            # Описание
#            file.write("== Описание API\n*URL: <«Базис.Virtual Protect» controller URL>/<URL функции>*\n")
#            file.write(f"{api_spec['info'].get('description', 'Описание отсутствует.')}\n\n")

            # Пути и методы
            for path, methods in api_spec['paths'].items():
                file.write(f"=== URL: {path}\n")
                for method, details in methods.items():
                    file.write(f"\n==== Метод: {method.upper()}\n")
                    file.write(f"===== Описание\n{details.get('summary', 'Описание отсутствует.')}\n\n")

                    # Параметры
                    if 'parameters' in details:
                        file.write("===== Параметры\n\n[options=\"header\",cols=\"2,1,3,2\"]\n|===\n| Параметр | Тип | Описание | Значение по умолчанию\n")
                        for param in details['parameters']:
                            name = param['name']
                            param_type = param.get('type', 'Не указано')
                            default_value = param.get('default', '')
                            description = param.get('description', 'Описание отсутствует.')
                            required_text = "*_<обязательный параметр>_* +\n" if param.get('required', False) else "_<необязательный параметр>_ +\n"
                            full_description = f"{required_text} {description}"
                            file.write(f"| {name} | {param_type} | {full_description} | {default_value}\n")
                        file.write("|===\n")

                    # Ответы
                    file.write("===== Ответы\n\n[options=\"header\",cols=\"1,4\"]\n|===\n| Код | Описание\n")
                    for code, response in details.get('responses', {}).items():
                        file.write(f"| {code} | {response.get('description', 'Описание отсутствует.')}\n")
                    file.write("|===\n")

                    # Добавление типов возвращаемых значений
                    if '200' in details.get('responses', {}):
                        response = details['responses']['200']
                        response_schema = response.get('schema', {})
                        if response_schema:
                            file.write("*Тип возвращаемого значения:* ")
                            if '$ref' in response_schema:
                                schema_ref = response_schema['$ref']
                                schema_name = schema_ref.split('/')[-1]
                                file.write(f"{schema_name}\n")
                            else:
                                response_type = response_schema.get('type', 'Не указано')
                                file.write(f"{response_type}\n")
                            file.write("\n")

    except Exception as e:
        print(f"Ошибка при обработке файла: {e}")

# Пример вызова функции
convert_yaml_to_asciidoc('../study/docs/swagger/openapi.yaml', 'api_spec.adoc')
