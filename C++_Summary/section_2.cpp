#include <iostream>
#include <iomanip>
#include <typeinfo> //�鿴��������
#include <fstream> //�����������
#include <string> //
using namespace std;


void main_2()	// Ϊʲô������ôд
{
	//-- Constant����
	// 1�����ӿɶ���	2�����ӿ�ά����
	const int FLONG = 5, flong_3 = 6;	// ����ʱ���븳ֵ; ����ͬʱ����������Ϊһ�����͵ģ�������ȫ��д��ʾ
	const char flong_2 = 100;	
	cout << "First constant:\t" << FLONG << endl;
	cout << "Type of the constant:" << typeid(5.5e3f).name() << endl;	//�鿴��������
	cout << "Output char data:" << flong_2 << '\n';	//�����䱾���������ͽ������

	//////////////////////////////////////////////////////////////////////////
	// ������Ĳ��ܸ�����
	const int aa = 3;
	int* p = const_cast<int*>(&aa);
	* p = 4;
	cout << "value of p: " << *p << endl;
	cout << "value of a: " << aa << endl;	// �����Ȼ��3
	cout << "address of p: " << p << endl;
	cout << "address of a: " << &aa << endl;
	// 1�������Ǵ��ڷ��ű��еģ������ڴ���  2��&a�൱�������ڴ��д�����һ��a�ĸ���Ʒ������ǿ��Ը��ĵ�


	int a = 4, b = 5;
	//-- ����������� ���ʽ1��(���ʽ2):(���ʽ3)�����ʽ1��ȷ�����б��ʽ2���������б��ʽ3��
	cout << (a > b ? a + b : a - b) << '\n';

	//-- Ϊ�˲�ʹ��ʽ����ת�������в���������ݾ��ȶ�ʧ��
	//������ɾ��ȵ͡���ΧС������ת���ɾ��Ƚϸߡ���Χ�ϴ������

	//-- static_cast<������>(���ʽ)	ʵ��ǿ������ת��

	//-- �������
	//cin�ǴӼ��̶�ȡ���ݣ�cout��������ݵ���Ļ
	/*
	int aa;
	char bb;
	cin >> aa >> bb;
	cout << "The input data1:" << aa << "   data2:" << bb << '\n';
	*/

	// ���ü��setw(int n)��setiosflags(ios::left)ʵ�������
	cout << setiosflags(ios::left) << 's' << setw(8) << 'a' << setw(8) << 'b' << endl;

	// ʹ�ñ�׼�� ifstream�� �� ofstream�� ������
	// ���������"<<"����ȡ�����">>"�����ļ��Ķ�/д����
	ifstream ifile("idata.txt");
	int sum = 0, value;
	cout << "data: ";
	while (ifile >> value)
	{
		cout << value << " ";
		sum += value;
	}
	cout << '\n';
	cout << "The sum is: " << sum << '\n';

	//-- String����
	string str1("Happy");
	string str2(" Birthday!\n");
	cout << (str1+=str2) << '\n';
	// ����string�������ݵĴ�Сȡ���� ��һ����ͬ�ַ���ASCII��ֵ


	//-- typedef
	// ���������������ͣ��������� pstr �ĳ��־ʹ����� char*
	typedef char * pstr;
	pstr mystr;
}