#include <webots/DistanceSensor.hpp>
#include <webots/Motor.hpp>
#include <webots/Robot.hpp>
#include <webots/Keyboard.hpp>
#include <webots/GPS.hpp>
#include <webots/InertialUnit.hpp>
#include <webots/Camera.hpp>


#define TIME_STEP 64
using namespace webots;

int main(int argc, char **argv) {
  Robot *robot = new Robot();
  Keyboard kb;
  DistanceSensor *ds[2];
  
  char dsNames[2][10] = {"ds_right", "ds_left"};
  for (int i = 0; i < 2; i++) {
    ds[i] = robot->getDistanceSensor(dsNames[i]);
    ds[i]->enable(TIME_STEP);
  }
  Motor *lr;
  lr=robot->getMotor("linear");
  
  Motor *rm;
  rm=robot->getMotor("rm");
  
  Camera *cm;
  cm=robot->getCamera("camera");
  cm->enable(TIME_STEP);
  
  Motor *wheels[4];
  char wheels_names[4][8] = {"wheel1", "wheel2", "wheel3", "wheel4"};
  for (int i = 0; i < 4; i++) {
    wheels[i] = robot->getMotor(wheels_names[i]);
    wheels[i]->setPosition(INFINITY);
    wheels[i]->setVelocity(0.0);
  }
  
  kb.enable(TIME_STEP);
  double leftSpeed = 0.0;
  double rightSpeed = 0.0;
  double linear=0.0;
  double rotate=0.0;
  while (robot->step(TIME_STEP) != -1) {
    int key=kb.getKey();
    
    if (key==315){
    leftSpeed = 1.0;
    rightSpeed = 1.0;
    } else if (key==317){
    leftSpeed = -1.0;
    rightSpeed = -1.0;
    }else if (key==316){
    leftSpeed = 1.0;
    rightSpeed = -1.0;
    }else if (key==314){
    leftSpeed = -1.0;
    rightSpeed = 1.0;
    }else {
    leftSpeed = 0.0;
    rightSpeed = 0.0;
    }
    wheels[0]->setVelocity(leftSpeed);
    wheels[1]->setVelocity(rightSpeed);
    wheels[2]->setVelocity(leftSpeed);
    wheels[3]->setVelocity(rightSpeed);
    if (key==87 && linear<0.19){
    linear += 0.005;
    } else if (key==83 && linear>0){
    linear += -0.005;
    }else {
    linear+=0;
    }
    lr->setPosition(linear);
    std::cout<<key<<std::endl;
    if (key==65 && rotate<1.57){
    rotate += 0.05;
    } else if (key==68 && rotate>-1.57){
    rotate += -0.05;
    }else {
    rotate+=0;
    }
    rm->setPosition(rotate);
    
    
  }
  delete robot;
  return 0;  // EXIT_SUCCESS
}
