# Ruta del archivo XML
$xmlFilePath = "C:\ProgramData\Jenkins\.jenkins\workspace\Get_Commits_And_Export_XPZ_Pipeline\ResultCommits.xml"

# Leer el archivo XML y limpiarlo de cualquier espacio en blanco antes de la declaración XML
$content = Get-Content -Path $xmlFilePath -Raw

# Eliminar cualquier espacio en blanco antes de la declaración XML
$content = $content.TrimStart()

# Eliminar cualquier línea vacía antes de la declaración XML
$content = $content -replace '^\s*[\r\n]+', ''

# Asegurarnos de que la declaración XML esté en la primera línea
if ($content -notmatch "^<\?xml") {
    Write-Error "El archivo XML no comienza con la declaración XML '<?xml ...'"
    exit
}

# Guardar el contenido limpio de nuevo en el archivo (esto podría sobrescribir el archivo original)
# Set-Content -Path $xmlFilePath -Value $content  <-- Esta línea se omite si no deseas sobrescribir el archivo

# Cargar el archivo XML limpio
[xml]$xmlDoc = [xml]$content

# Crear un HashSet para almacenar objetos únicos (eliminando duplicados automáticamente)
$objectList = New-Object System.Collections.Generic.HashSet[System.String]

# Recorrer las entradas de log y obtener los objetos modificados o agregados
foreach ($logentry in $xmlDoc.log.logentry) {
    foreach ($action in $logentry.actions.action) {
        if ($action.type -in @("Modified", "Added")) {
            $objectGuid = $action.objectGuid
            $objectType = $action.objectType
            $objectName = $action.objectName

            # Formatear el objeto como "Tipo/Nombre(Guid)"
            $objectString = "$objectType/$objectName($objectGuid)"
            
            # Agregar el objeto al HashSet (esto evita duplicados automáticamente)
            $null = $objectList.Add($objectString)
        }
    }
}

# Unir los objetos en una cadena separada por punto y coma
$objectListString = $objectList -join ";"

# Mostrar el resultado (esto es lo que se puede usar en Jenkins)
Write-Host "El valor de la variable OBJECT_LIST es: $ob_
