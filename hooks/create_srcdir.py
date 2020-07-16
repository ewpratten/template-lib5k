import os

PACKAGE = "{{cookiecutter.java_package}}.y{{cookiecutter.year}}.{{cookiecutter.robot_name}}"

# Convert Java package into a path
path = "src/main/java/" + PACKAGE.replace(".", "/")

# Make the directories
os.makedirs(path)

# Place a Main.java file at the end of the path
java_main_file = f"package {PACKAGE};" + """

import edu.wpi.first.wpilibj.RobotBase;

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