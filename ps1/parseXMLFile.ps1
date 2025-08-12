# Ruta del archivo XML
$xmlFilePath = "C:\ProgramData\Jenkins\.jenkins\workspace\Get_Commits_And_Export_XPZ_Pipeline\ResultCommits.xml"

# Leer el archivo XML y limpiarlo de cualquier espacio en blanco antes de la declaración XML
$content = Get-Content -Path $xmlFilePath -Raw

# Eliminar cualquier espacio en blanco antes de la declaración XML
$content = $content.TrimStart()

# **No se sobrescribe el archivo XML**
# Set-Content -Path $xmlFilePath -Value $content   <-- Eliminar o comentar esta línea

# Cargar el archivo XML limpio
[xml]$xmlDoc = Get-Content -Path $xmlFilePath

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
Write-Host "El valor de la variable OBJECT_LIST es: $objectListString"

# Retornar el valor final si lo deseas
return $objectListString