#include "robot.h"

using namespace std;

int main()
{
	Robot r1;//Cria o objeto c1 que pertence a classe conta
	r1.posicao = {1,2};
	r1.showPos();
	r1.velocidade = {1,1};
	float t = 1;
	r1.move(t);
	r1.showPos();
	r1.changeSpeed(0.5,1);
	r1.showSpeed();
}
