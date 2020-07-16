import os
import re
import urllib.request, urllib.error

PACKAGE = "{{cookiecutter.java_package}}.y{{cookiecutter.year}}.{{cookiecutter.robot_name}}"

# Convert Java package into a path
path = "src/main/java/" + PACKAGE.replace(".", "/")

# Make the directories
os.makedirs(path)

# Place a Main.java file at the end of the path
java_main_file = f"package {PACKAGE};" + """

import edu.wpi.first.wpilibj.RobotBase;
import edu.wpi.first.wpilibj.shuffleboard.Shuffleboard;

import io.github.frc5024.lib5k.autonomous.RobotProgram;

public class Main extends RobotProgram {

    public static void main(String[] args) {
        RobotBase.startRobot(Main::new);
    }

    public Main() {
        super(false, true, Shuffleboard.getTab("Main"));

    }

    @Override
    public void autonomous(boolean init) {
    }

    @Override
    public void disabled(boolean init) {

    }

    @Override
    public void teleop(boolean init) {

    }

    @Override
    public void test(boolean init) {

    }

}
"""

# Write the file to the end of the path
with open(f"{path}/Main.java", "w") as fp:
    fp.write(java_main_file)
    fp.close()

### Lib5K ###

# Make a libs directory
if not os.path.exists("libs"):
    os.mkdir("libs")

# Read the latest lib5k version number
print("Reading repository metadata from Lib5K: ", end="\r")
lib5k_info = urllib.request.urlopen("https://api.github.com/repos/frc5024/lib5k/releases/latest").read().decode()
lib5k_tag = re.findall(r'tag_name":"([v.0-9]*)"', lib5k_info, re.M)[0]
lib5k_version = lib5k_tag.strip("v")
print("Reading repository metadata from Lib5K: Done")

# Fetch the latest jar
print(f"Downloading lib5k-bundle-{lib5k_version}-monolithic.jar: ", end="\r")
lib5k_jar = urllib.request.urlopen(f"https://github.com/frc5024/lib5k/releases/download/{lib5k_tag}/lib5k-bundle-{lib5k_version}-monolithic.jar").read()
print(f"Downloading lib5k-bundle-{lib5k_version}-monolithic.jar: Done")

# Write jar to libs folder
print("Writing jar file to libs folder: ", end="\r")
with open(f"libs/lib5k-bundle-{lib5k_version}-monolithic.jar", "wb") as fp:
    fp.write(lib5k_jar)
    fp.close()
print("Writing jar file to libs folder: Done")

# Read the latest Lib5K python scripts
try:
    print("Downloading Lib5K scripts: ", end="\r")
    simulate_script = urllib.request.urlopen(f"https://github.com/frc5024/lib5k/releases/download/{lib5k_tag}/simulate.py").read().decode()
    logreader_script = urllib.request.urlopen(f"https://github.com/frc5024/lib5k/releases/download/{lib5k_tag}/logreader.py").read().decode()
    print("Downloading Lib5K scripts: Done")

    # Make a scripts directory
    if not os.path.exists("scripts"):
        os.mkdir("scripts")

    # Write the scripts
    print("Writing scripts to scripts folder: ", end="\r")
    with open("scripts/simulate.py", "w") as fp:
        fp.write(simulate_script)
        fp.close()
    with open("scripts/logreader.py", "w") as fp:
        fp.write(logreader_script)
        fp.close()
    print("Writing scripts to scripts folder: Done")

except urllib.error.HTTPError as e:
    print("Latest version of Lib5K does not contain any scripts")