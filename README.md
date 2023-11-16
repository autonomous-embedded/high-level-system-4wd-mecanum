# Embedded Autonomous Car - Workspace

## Cloning the Repository with Submodules

To properly clone the "ros_workspace" repository, which contains submodules (`mecanum_controller`, `mecanum_driver`, and `realsense-ros`), follow the steps below.

### Step 1: Clone the Repository

```bash
git clone --recurse-submodules git@github.com:autonomous-embedded/ros_workspace.git
```

If you forget the `--recurse-submodules` flag during cloning, you can initialize and update submodules manually after cloning:

```bash
# Navigate into the repository's directory
cd ros_workspace

# Initialize and update submodules
git submodule init
git submodule update
```

### Step 2: Verify Submodules

To ensure that the submodules have been cloned successfully, you can check the contents of the `mecanum_controller`, `mecanum_driver`, and `realsense-ros` directories:

```bash
ls mecanum_controller
ls mecanum_driver
ls realsense-ros
```

You should see the content of each submodule's repository.

### Step 3: Cloning with HTTPS (Optional)

If you encounter permission issues or if you prefer using HTTPS, you can modify the submodule URLs in the `.gitmodules` file. Change the `url` values from `git@github.com:...` to `https://github.com/...`.

For example, change:

```ini
[submodule "mecanum_controller"]
	path = src/mecanum_controller
	url = git@github.com:autonomous-embedded/mecanum_controller.git
	branch = master
```

to:

```ini
[submodule "mecanum_controller"]
	path = src/mecanum_controller
	url = https://github.com/autonomous-embedded/mecanum_controller.git
	branch = master
```

Repeat this modification for each submodule.

## Adding New Submodule to the Project

To add a new submodule to your project, follow these steps:

```bash
# Add the submodule with its URL and desired path
git submodule add 'URL-to-repo' path/to/submodule

# Initialize and update the submodule
git submodule init
git submodule update
```

Replace `'URL-to-repo'` with the actual URL of the submodule's repository and `path/to/submodule` with the desired path where you want to place the submodule within your project.

By following these steps, you can clone the "ros_workspace" repository with its submodules and add new submodules to your project.

## Setting up ROS Noetic Catkin Workspace

After cloning the "ros_workspace" repository, follow the steps below to set up the ROS Noetic catkin workspace:

### Step 1: Initialize Workspace

Navigate into the repository's directory:

```bash
cd ros_workspace
```

Initialize the catkin workspace using:

```bash
catkin_make
```

**Note:** If `catkin_make` fails due to uninstalled dependencies related to `realsense-ros`, please refer to the installation process described in [src/realsense-ros/README.md](src/realsense-ros/README.md).

### Step 2: Source Setup

After successfully initializing the workspace, source the setup script:

```bash
source devel/setup.sh
```

### Step 3: Start ROS Core (roscore)

Ensure that the ROS core is running by executing:

```bash
roscore
```

This command starts the ROS master server.

### Step 4: Run Specific Node

To run a specific node from a package, use the `rosrun` command. For example:

```bash
rosrun mecanum_controller node
```

Replace `mecanum_controller` with the actual package name, and `node` with the executable you want to run.

### Step 5: Start Camera Node

This project involves a camera node (from `realsense-ros`), start it using the provided launch file:

```bash
roslaunch realsense2_camera rs_camera.launch
```

**Note:** To verify the proper functionality of the camera node by running the `rviz` application.

You have now set up your ROS Noetic catkin workspace and are ready to run and develop your ROS nodes. If you encounter any issues, please refer to the specific README files in each package or module for further instructions.
