import subprocess
result = subprocess.check_output(['ls'])
print(result.decode())
