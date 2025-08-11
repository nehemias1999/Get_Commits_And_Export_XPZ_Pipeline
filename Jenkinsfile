pipeline {

    agent { label 'principal' }

    environment{

        TeamDevExePath = "C:\\Program Files (x86)\\GeneXus\\GeneXus18U7SIGA\\TeamDev.msbuild"
        GXServerURL = "https://gxserver18.accionpoint.com/"
        KBName = "SigaV7"
        KBVersion = "SigaV7"
        GXServerUser = "local\\sa_jenkins_genexus"
        GXServerPassword = "567NTb0L4L4wjK4hZkAl"
        DateFrom = "2025-08-08T09:00:00"
        DateTo = "2025-08-08T18:00:00"
        ResultsXMLFilePath = "C:\\Models\\ResultCommits.xml"
    
    }

    stages {

        stage('OBTENIENDO COMMITS GXSERVER') {

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

                    bat("echo. > ${env.ResultsXMLFilePath}")

                }

            }

        }

        stage('Exportar objetos en archivo XPZ') {

            steps {

                script {

                    bat("echo. > ${env.ResultsXMLFilePath}")

                    // <Export File="$(ExportFileName)" Objects="$(ObjectList)" DependencyType="$(depType)" ReferenceType="$(refType)" IncludeGXMessages="$(includeGXMsg)" IncludeUntranslatedMessages="$(includeUtMsg)" OnlyStructuresForTransactions="$(OnlyStructTrn)" />

                }

            }

        }

    }        
       
}

