# Ruta del archivo XML
$xmlFilePath = "C:\ProgramData\Jenkins\.jenkins\workspace\Get_Commits_And_Export_XPZ_Pipeline\ResultCommits.xml"

# Cargar el archivo XML
[xml]$xmlDoc = Get-Content -Path $xmlFilePath

# Inicializar una lista para los objetos
$objectList = @()

# Recorrer las entradas de log y obtener los objetos modificados o agregados
foreach ($logentry in $xmlDoc.log.logentry) {
    foreach ($action in $logentry.actions.action) {
        if ($action.type -in @("Modified", "Added")) {
            $objectGuid = $action.objectGuid
            $objectType = $action.objectType
            $objectName = $action.objectName

            # Formatear el objeto como "Tipo/Nombre(Guid)"
            $objectList += "$objectType/$objectName($objectGuid)"
        }
    }
}

# Unir los objetos en una cadena separada por punto y coma
$objectListString = $objectList -join ";"

# Mostrar el resultado (esto es lo que se puede usar en Jenkins)
Write-Host "El valor de la variable OBJECT_LIST es: $objectListString"

# Retornar el valor final si lo deseas
return $objectListString
