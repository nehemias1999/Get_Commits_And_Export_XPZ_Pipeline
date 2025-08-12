import xml.etree.ElementTree as ET

def clean_xml(file_path):
    """ Limpia el archivo XML de caracteres no deseados antes de la declaración XML """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Eliminar caracteres no visibles antes de la declaración XML
    content = content.lstrip()  # Elimina los espacios en blanco al principio
    
    # Escribir el contenido limpio de vuelta en el archivo temporal
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def parse_xml(file_path):
    # Limpiar el archivo XML de caracteres no deseados antes de procesarlo
    clean_xml(file_path)
    
    # Parsear el archivo XML
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    objects = []  # Lista de objetos que fueron modificados/agregados

    # Recorrer cada logentry
    for logentry in root.findall('logentry'):
        # Recorrer cada acción dentro de <actions>
        for action in logentry.findall('.//action'):
            action_type = action.get('type')
            object_guid = action.find('objectGuid').text
            object_type = action.find('objectType').text
            object_name = action.find('objectName').text
            
            # Filtrar solo objetos modificados o agregados
            if action_type in ['Modified', 'Added']:
                # Asegurarse de que el objeto esté entre comillas para evitar errores de comando
                objects.append(f'"{object_type}/{object_name}({object_guid})"')

    # Retornar los objetos como una cadena separada por punto y coma
    return ";".join(objects)

def main():
    # Ruta al archivo XML
    xml_file_path = r"C:\ProgramData\Jenkins\.jenkins\workspace\Get_Commits_And_Export_XPZ_Pipeline\ResultCommits.xml"
    
    # Parsear el archivo XML y obtener la lista de objetos
    objects_list = parse_xml(xml_file_path)
    
    # Crear una variable para utilizar posteriormente
    return objects_list

if __name__ == "__main__":
    objects_list = main()
    print(objects_list)  # Esto imprime el valor de la lista de objetos generada
