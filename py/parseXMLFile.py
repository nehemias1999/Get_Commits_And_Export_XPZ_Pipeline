import xml.etree.ElementTree as ET

def parse_xml(file_path):
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
                objects.append(f"{object_type}/{object_name}({object_guid})")

    # Retornar los objetos como una cadena separada por punto y coma
    return ";".join(objects)

def main():
    # Ruta al archivo XML
    xml_file_path = "C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Get_Commits_And_Export_XPZ_Pipeline\\ResultCommits.xml"
    
    # Parsear el archivo XML y obtener la lista de objetos
    objects_list = parse_xml(xml_file_path)
    
    # Crear una variable para utilizar posteriormente
    # Esta variable puede ser usada en el pipeline o exportada a un archivo
    return objects_list

if __name__ == "__main__":
    objects_list = main()
    print(objects_list)  # Esto imprime el valor de la lista de objetos generada