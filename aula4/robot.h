#ifndef ROBOT_H
#define ROBOT_H

#include <string>

struct Coordenadas{
    float x;
    float y;
};

class Robot
{
private: //Atributos privados só podem ser acessados pela classe e seus metodos
public://Podem ser acessados direto no main
	Coordenadas posicao;
	Coordenadas velocidade;
	void showPos();
	void move(float t);
	void changeSpeed(float, float);
	void showSpeed();
	

};

#endif
