#pragma once
/*
	����ʱ�����ͷ�ļ�
*/
#include <iostream>
using namespace std;
// �κ�һ����Ա���������κ�һ����Ա��������������
// main()�����У������Ķ���ֻ�ܷ���public��Ա

class clock // �������
{

private: // ˽�г�Ա
	static int couts;	// ��̬��Ա�����ͬһ��Ĳ�ͬ����֮�����ݺͺ����Ĺ������⡣��Ҫ��main����ȫ�ֱ������ֳ�ʼ����

protected: // �����ͳ�Ա
	// ��Ķ����ܷ��ʣ�����������ĳ�Ա�������Է��ʻ����protected��Ա������ֻ��ָ�Լ����ö����ˣ�������ָ�����á���
	int Hour;
	int Minute;
	int Second;
public: // ���г�Ա
	
	///////// ���캯�� \\\\\\\\\\\
	// 1�����ƣ����������캯��	  2���޲ι��캯��	 3��������Ĭ��ֵ�Ĺ��캯��	4��������Ĭ��ֵ�Ĺ��캯��	
	// 2��3��ΪĬ�Ϲ��캯��

	clock(const clock& c);	// ���ƣ��������캯����
	clock(); // �޲ι��캯��
	clock(int H = 0, int M = 0, int S = 0);	// ������Ĭ��ֵ�Ĺ��캯��
	//clock(int H, int M, int S); // �������캯����Ϊ��ʼ������
	//clock(int H);	// ����
	

	// ����::����(){};		Ĭ�Ϲ��캯��
	// ����::����(){���...};		�޲ι��캯��

	///////// �������� \\\\\\\\\\\
	// ���г�Ա������ϵͳ�Զ����ã�û�з���ֵ���޷����ء�
	~clock();		//��ʽ

	///////// ��̬��Ա���� \\\\\\\\\\\
	// ��ͨ��ʵ��ֱ�ӷ����ڲ�����
	static void printC()
	{
		cout << "This number of clocks is: " << couts << endl;
	};
	
	//////// ��Ԫ�������� �� ���� \\\\\\\\\\\
	
	friend void Youyuan(clock aa)
	{
		cout << "���Է���˽�������е�Сʱ����" << aa.Hour << endl;
	};


	void SetTime(int newH=0, int newM=0, int newS=0);
	void ShowTime();
	void ShowTime(int n);
};