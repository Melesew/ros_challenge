# ros_challenge

# Requirements

1. Install ros following this link http://wiki.ros.org/kinetic/Installation/Ubuntu if you are using ubuntu
   or use google if not.

2. Once you have finished installation create your workspace, http://wiki.ros.org/ROS/Tutorials/CreatingPackage

3. Download the project and then extract it in your workspace, catkin_ws in my case.
  cd /catkin_ws/

4. Define source by typing in "source devel/setup.bash" in the terminal window.

5. Install blender

---------Then-------

1. Capture an image from the webcam and convert it to grayscale.
roslaunch ros_challenge publish_subscribe_launcher.launch

2. Create interesting fractals using turtlesim.
Run fractale by typing the following command
roslaunch ros_challenge fractal_launcher.launch

3. Communicate messages between ROS and blender.
Open src/server.blend file using blender and then run the following in your terminal
roslaunch ros_challenge blender_launcher.launch

4. Make the second turtle follow or chase the first one using PID motion.
Run chasing turtle simulation by typing the following command
roslaunch ros_challenge turtle_chasing_launcher.launch

5. Create GUI Application to drive turtle.
Run GUI controlled turtle simulation by typing the following command
rosrun ros_challenge gui_launcher.py

then click the buttons to move the turtle to your direction in need.
