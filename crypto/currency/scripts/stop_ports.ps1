# Iterate over port numbers
for ($port = 5000; $port -le 5003; $port++) {
    # Find the process listening on the port
    $processId = Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess

    # If a process is found, stop it
    if ($processId) {
        Stop-Process -Id $processId -Force
        Write-Host "Stopped process listening on port $port"
    } else {
        Write-Host "No process found listening on port $port"
    }
}
