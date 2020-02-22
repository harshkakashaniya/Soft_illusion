// File:          EPuckGoForward.cpp
// Date:
// Description:
// Author:
// Modifications:

// You may need to add webots include files such as
// <webots/DistanceSensor.hpp>, <webots/Motor.hpp>, etc.
// and/or to add some other includes
#include <webots/Robot.hpp>
#include <webots/Motor.hpp>

// All the webots classes are defined in the "webots" namespace
using namespace webots;
#define TIME_STEP 64
#define MAX_SPEED 6.28
// This is the main program of your controller.
// It creates an instance of your Robot instance, launches its
// function(s) and destroys it at the end of the execution.
// Note that only one instance of Robot should be created in
// a controller program.
// The arguments of the main function can be specified by the
// "controllerArgs" field of the Robot node
int main(int argc, char **argv) {
  // create the Robot instance.
  Robot *robot = new Robot();
  // get the motor devices
  Motor *leftMotor = robot->getMotor("left wheel motor");
  Motor *rightMotor = robot->getMotor("right wheel motor");
  // set the target position of the motors
 leftMotor->setPosition(INFINITY);
 rightMotor->setPosition(INFINITY);
 
 leftMotor->setVelocity(0.1 * MAX_SPEED);
 rightMotor->setVelocity(0.1 * MAX_SPEED);
  // You should insert a getDevice-like function in order to get the
  // instance of a device of the robot. Something like:
  //  Motor *motor = robot->getMotor("motorname");
  //  DistanceSensor *ds = robot->getDistanceSensor("dsname");
  //  ds->enable(timeStep);

  // Main loop:
  // - perform simulation steps until Webots is stopping the controller
  while (robot->step(TIME_STEP) != -1);

  // Enter here exit cleanup code.

  delete robot;
  return 0;
}