#include "clock.h"


void clock::SetTime(int newH, int newM, int newS)
{
	Hour = newH;
	Minute = newM;
	Second = newS;
}

void clock::ShowTime()
{
	cout << Hour << ":" << Minute << ":" << Second << endl;
}

void clock::ShowTime(int n)	// 重载函数
{
	cout << Hour << "点" << Minute << "分" << Second << "秒 \n";
}

clock::clock(int H, int M, int S)	// 构造函数的实现
{
	Hour = H;
	Minute = M;
	Second = S;
	couts++;	// 每创建一个实体，couts加1，couts为static类型的
}

clock::clock(const clock& c)
{
	Hour = c.Hour;
	Minute = c.Minute;
	Second = c.Second;
}

clock::~clock()
{
	couts--;
}