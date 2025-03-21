import subprocess

runCommand = 'mkdir build\ncd build\ncmake -DCMAKE_BUILD_TYPE=Release ..\nmake -j 15'
subprocess.call([runCommand], shell=True)