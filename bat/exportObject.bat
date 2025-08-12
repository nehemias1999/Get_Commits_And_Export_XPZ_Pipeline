echo "MSBUILDPath: " %1
echo "File MSBUILD: " %2
echo "GX_PROGRAM_DIR: " %3
echo "WorkingVersion: " %4
echo "WorkingDirectory: " %5
echo "SourceVersion: " %6
echo "SinceDate: " %7

%1 /t:MergeVersions  /p:GX_PROGRAM_DIR=%3 /p:WorkingVersion=%4 /p:WorkingDirectory=%5 /p:SourceVersion=%6 /p:TargetVersion=%4 /p:KBPath=%5 %2 /p:SinceDate=%7