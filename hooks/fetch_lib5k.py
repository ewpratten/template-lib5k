import os
import re
import urllib.request

# Make a libs directory
os.mkdir("libs")

# Read the latest lib5k version number
lib5k_info = urllib.request.urlopen("https://api.github.com/repos/frc5024/lib5k/releases/latest").read()
lib5k_tag = re.findall(r'tag_name": "(.*)"', lib5k_info, re.M)[0]
lib5k_version = lib5k_tag.strip("v")

# Fetch the latest jar
lib5k_jar = urllib.request.urlopen(f"https://github.com/frc5024/lib5k/releases/download/{lib5k_tag}/lib5k-bundle-{lib5k_version}-monolithic.jar").read()

# Write jar to libs folder
with open(f"libs/lib5k-bundle-{lib5k_version}-monolithic.jar", "wb") as fp:
    fp.write(lib5k_jar)
    fp.close()

# Make a scripts directory
os.mkdir("scripts")

# Read the latest Lib5K python scripts
simulate_script = urllib.request.urlopen(f"https://github.com/frc5024/lib5k/releases/download/{lib5k_tag}/simulate.py").read()
logreader_script = urllib.request.urlopen(f"https://github.com/frc5024/lib5k/releases/download/{lib5k_tag}/logreader.py").read()

# Write the scripts
with open("scripts/simulate.py", "w") as fp:
    fp.write(simulate_script)
    fp.close()
with open("scripts/logreader.py", "w") as fp:
    fp.write(logreader_script)
    fp.close()