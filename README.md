# Embedded Autonomous Mecanum Car - Workspace

## Cloning the Repository with Submodules

To clone the repository, run: `git clone --recurse-submodules git@github.com:autonomous-embedded/high-level-system-4wd-mecanum.git`. Don't use HTTP...

## Setting up ROS Noetic Catkin Workspace

The root directory of this repository represents a [catkin workspace](http://wiki.ros.org/catkin/workspaces).

## Building the software

To build the packages, run: `catkin_make` in the root of this repository. If you're cloning from `mecanum_integration`, you can also run: `cd $MECANUM_HL_PATH; catkin_make;` after sourcing the `environment-check.sh` script.

## devel/setup.sh script

The `<ros_workspace>/devel/setup.sh` script will setup all of the necessary paths, autocompletions etc., so you can run the commands below...

## Running the high-level software

To run the software, simply run: `roslaunch mecanum_bringup mecanum_vision.launch`. You can run this from anywhere basically once you've sourced the `devel/setup.sh` script. If you're cloning from `mecanum_integration` you can also run the `mecanum-hl-run.sh` script, which should source the `devel/setup.sh` script for you.

## Debugging

Simple print debugging. Good luck!

