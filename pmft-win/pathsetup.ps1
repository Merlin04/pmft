setx PYTHONHOME c:\Python27
setx PYTHONPATH c:\Python27\Lib

$path2add = ';C:\Python27;C:\Program Files (x86)\pmft;'
$systemPath = [Environment]::GetEnvironmentVariable('Path', 'machine');

If (!$systemPath.contains($path2add)) {
    $systemPath += $path2add
    $systemPath = $systemPath -join ';'
    [Environment]::SetEnvironmentVariable('Path', $systemPath, 'Machine');
    write-host "Added to path!"
    write-host $systemPath
}