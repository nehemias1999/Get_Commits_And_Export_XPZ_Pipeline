@echo off
setlocal enabledelayedexpansion

:: Ruta al archivo XML
set "xmlFilePath=C:\ProgramData\Jenkins\.jenkins\workspace\Get_Commits_And_Export_XPZ_Pipeline\ResultCommits.xml"

:: Inicializar la variable de lista de objetos
set "objectList="

:: Leer el archivo XML línea por línea
for /f "delims=" %%a in ('findstr /i "<action type=\"Modified\"\\|<action type=\"Added\"" "%xmlFilePath%"') do (
    :: Extraer los valores del objeto de la línea
    for /f "tokens=2 delims=<>" %%b in ("%%a") do (
        set "line=%%b"
        set "objectGuid="
        set "objectType="
        set "objectName="
        for /f "tokens=1,2,3 delims=;" %%x in ("!line!") do (
            set "objectGuid=%%x"
            set "objectType=%%y"
            set "objectName=%%z"
        )
        :: Construir la lista de objetos
        set "objectString=!objectType!/!objectName!(!objectGuid!)"
        :: Agregar el objeto a la lista si no existe
        echo !objectList! | findstr /i /c:"!objectString!" > nul || (
            if defined objectList (
                set "objectList=!objectList!;!objectString!"
            ) else (
                set "objectList=!objectString!"
            )
        )
    )
)

:: Retornar el valor final si lo deseas
exit /b