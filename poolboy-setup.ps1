# Check if Python is installed
$pythonInstalled = Get-Command python -ErrorAction SilentlyContinue

if ($pythonInstalled -eq $null) {
    # Python is not installed, so let's install it
    Write-Host "Installing Python..."
    Start-Process -Wait -FilePath "https://www.python.org/ftp/python/3.10.1/python-3.10.1-amd64.exe" -ArgumentList "/quiet", "InstallAllUsers=1", "PrependPath=1"
    Write-Host "Python installed successfully!"
} else {
    Write-Host "Python is already installed."
}

# Check if Flask is installed
$flaskInstalled = pip show Flask -ErrorAction SilentlyContinue

if ($flaskInstalled -eq $null) {
    # Flask is not installed, so let's install it
    Write-Host "Installing Flask..."
    python -m pip install Flask
    Write-Host "Flask installed successfully!"
} else {
    Write-Host "Flask is already installed."
}
