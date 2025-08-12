import xml.etree.ElementTree as ET
from collections import defaultdict

def parse_xml(file_path):
    # Parsear el archivo XML
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # Usamos un defaultdict para agrupar objetos por type
    object_groups = defaultdict(list)
    
    # Recorrer cada logentry en el XML
    for logentry in root.findall('logentry'):
        # Recorrer todas las acciones (action) dentro de cada logentry
        for action in logentry.findall('.//action'):
            action_type = action.get('type')
            object_type = action.find('objectType').text
            object_name = action.find('objectName').text
            
            # Agrupar objetos por tipo de objeto (objectType) solo si son modificados o agregados
            if action_type in ['Modified', 'Added']:
                object_groups[object_type].append(object_name)
    
    # Crear el formato requerido
    formatted_objects = []
    for object_type, object_names in object_groups.items():
        formatted_objects.append(f"{object_type}:{','.join(object_names)}")
    
    # Unir todas las partes con ";"
    return ';'.join(formatted_objects)

def main():
    # Ruta al archivo XML (asegúrate de poner la ruta correcta)
    xml_file_path = r"C:\ProgramData\Jenkins\.jenkins\workspace\Get_Commits_And_Export_XPZ_Pipeline\ResultCommits.xml"
    
    # Parsear el XML y obtener la lista formateada
    object_list = parse_xml(xml_file_path)
    
    return object_list

if __name__ == "__main__":
    result = main()
