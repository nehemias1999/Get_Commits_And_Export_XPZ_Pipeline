import xml.etree.ElementTree as ET
from collections import defaultdict

def clean_xml(file_path):
    """Limpia el archivo XML de espacios y caracteres no visibles antes de la declaración XML."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Eliminar cualquier espacio en blanco antes de la declaración XML
    content = content.lstrip()  # Eliminar espacios al inicio del archivo

    # Asegurarse de que la declaración XML esté en la primera línea
    if not content.startswith('<?xml'):
        raise ValueError("El archivo XML no comienza con la declaración '<?xml ...'")

    # Escribir el contenido limpio en un archivo temporal
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def parse_xml(file_path):
    # Limpiar el archivo XML antes de procesarlo
    clean_xml(file_path)

    # Parsear el archivo XML
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Crear un defaultdict para agrupar objetos por type (usamos set para evitar duplicados)
    object_groups = defaultdict(set)

    # Recorrer cada logentry en el XML
    for logentry in root.findall('logentry'):
        # Recorrer todas las acciones (action) dentro de cada logentry
        for action in logentry.findall('.//action'):
            action_type = action.get('type')
            object_type = action.find('objectType').text
            object_name = action.find('objectName').text

            # Reemplazar 'Web Panel' por 'Panel' en el objectType
            if object_type == 'Web Panel':
                object_type = 'Panel'

            # Agrupar objetos por tipo de objeto (objectType) solo si son modificados o agregados
            if action_type in ['Modified', 'Added']:
                object_groups[object_type].add(object_name)  # Usamos un set para evitar duplicados

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
    
    print(object_list)

if __name__ == "__main__":
    main() # Solo imprime la lista de objetos sin otras informaciones
