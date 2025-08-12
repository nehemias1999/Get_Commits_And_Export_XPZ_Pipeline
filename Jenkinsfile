pipeline {

    agent any

    environment{

        TeamDevExePath = "C:\\Program Files (x86)\\GeneXus\\GeneXus18U7\\TeamDev.exe"
        GXServerURL = "https://gxserver18.accionpoint.com"
        KBName = "SigaV5"
        KBVersion = "SigaV5"
        GXServerUser = "local\\sa_jenkins_genexus"
        GXServerPassword = "567NTb0L4L4wjK4hZkAl"
        DateFrom = "2025-08-11T09:00:00"
        DateTo = "2025-08-11T18:00:00"
        ResultsXMLFilePath = "${WORKSPACE}\\ResultCommits.xml"

        PythonEXEPath = "C:\\Users\\nsalazar\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"
        ParseXMLFilePath = "${WORKSPACE}\\ps1\\parseXMLFile.ps1"

        GeneXus18U7Path = "C:\\Program Files (x86)\\GeneXus\\GeneXus18U7"
        MSBuildPath = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\BuildTools\\MSBuild\\Current\\Bin"
        ExportFilePath = "${WORKSPACE}\\ExportedObjects.xpz"

    }

    stages {

        stage('Obtener commits de la KB en un intervalo de tiempo') {

            steps {

                script {

                    bat("echo. > ${env.ResultsXMLFilePath}")
                    
                    bat"""
                        "${env.TeamDevExePath}" history /s:${env.GXServerURL} /kb:${env.KBName} /ServerKbVersion:${env.KBVersion} /u:${env.GXServerUser} /p:${env.GXServerPassword} /from:${env.DateFrom} /to:${env.DateTo} -x >> ${env.ResultsXMLFilePath} 
                    """

                }

            }

        }

        stage('Procesar archivo XML para obtener objetos modificados de Commit') {

            steps {

                script {

                    // Ejecutar el script de PowerShell y capturar el resultado en una variable
                    def objectList = bat(script: '''
                        powershell -ExecutionPolicy Bypass -File "${env.ParseXMLFilePath}"
                    ''', returnStdout: true).trim()

                    // Mostrar el valor de la variable en los logs de Jenkins
                    echo "Lista de objetos: ${objectList}"

                    // bat label: 'Exportar objetos en archivo XPZ', 
                    // script: """
                    //     "${env.MSBuildPath}\\msbuild.exe" "msbuild\\Export.msbuild" /p:GX_PROGRAM_DIR=${env.GeneXus18U7Path} /t:Export /p:ExportFileName="${env.ExportFilePath}" /p:ObjectList="${objectList}"
                    // """

                }

            }

        }

    }        
       
}

