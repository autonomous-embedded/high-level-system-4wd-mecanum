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
	path = mecanum_controller
	url = git@github.com:autonomous-embedded/mecanum_controller.git
	branch = master
```

to:

```ini
[submodule "mecanum_controller"]
	path = mecanum_controller
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

## Launching ROS nodes
