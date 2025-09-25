#include "robot.h"
#include <iostream>
using namespace std;

void Robot::showPos()
{
	cout<<"x = "<< this->posicao.x<<endl; //objeto.struct.variavel_struct
	cout<< "y = "<< this->posicao.y<<endl; 
}

void Robot::move(float t)
{
    posicao.x += velocidade.x*t;
    posicao.y += velocidade.y*t;
}

void Robot::changeSpeed(float a, float b)
{
    velocidade.x += a;
    velocidade.y += b;
}
void Robot::showSpeed()
{
	cout<<"vel x = "<< this->velocidade.x<<endl; //objeto.struct.variavel_struct
	cout<< "vel y = "<< this->velocidade.y<<endl; 
}
