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

void clock::ShowTime(int n)	// ���غ���
{
	cout << Hour << "��" << Minute << "��" << Second << "�� \n";
}

clock::clock(int H, int M, int S)	// ���캯����ʵ��
{
	Hour = H;
	Minute = M;
	Second = S;
	couts++;	// ÿ����һ��ʵ�壬couts��1��coutsΪstatic���͵�
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