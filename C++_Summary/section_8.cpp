#include <iostream>
#include <cstring>
#include <string>
#include "clock.h"
#include "watch.h"


using namespace std ;

///////////
// �̳�������
///////////

//////////////////////////////////////////////////////////////////////////
// �̳еĸ���

// ���е���Ϊ���࣬�½�������Ϊ����(�̳�)��
// class ��������: �̳з�ʽ(public,private,protected) ���� {}��
// ������һ�ּ̳з�ʽ��������ĳ�Ա�������Է��ʻ����public,protected��Ա��
// ֻ����public�̳з�ʽ�������������ܷ��ʻ����public��Ա

// ע��ͬ�����������ص�����ǰ�߶����������������֮�䣬�����߶�����ͬһ�����ڲ�

void main_8()
{
	clock c1(8, 8, 8);
	//clock c2 = (10, 10, 10);
	clock* c3 = new clock(9, 9, 9);
	c1.ShowTime();
	c3->ShowTime();

	watch w1(6, 6, 6, "winter");
	w1.ShowTime();

	c1 = w1;	// �����ൽ�����ת��
	c3 = &w1;	// �������ָ��ָ�����������
	cout << '\n';
	c1.ShowTime();
	c3->ShowTime();
	w1.ShowTime();


}







