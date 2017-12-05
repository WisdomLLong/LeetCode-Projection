#include <iostream>
#include <iomanip>
#include <typeinfo> //查看数据类型
#include <fstream> //输入输出流库
#include <string> //
using namespace std;


void main_2()	// 为什么可以这么写
{
	//-- Constant常量
	// 1、增加可读性	2、增加可维护性
	const int FLONG = 5, flong_3 = 6;	// 定义时必须赋值; 可以同时定义多个，但为一个类型的；尽量用全大写表示
	const char flong_2 = 100;	
	cout << "First constant:\t" << FLONG << endl;
	cout << "Type of the constant:" << typeid(5.5e3f).name() << endl;	//查看数据类型
	cout << "Output char data:" << flong_2 << '\n';	//根据其本身数据类型进行输出

	//////////////////////////////////////////////////////////////////////////
	// 常量真的不能更改吗？
	const int aa = 3;
	int* p = const_cast<int*>(&aa);
	* p = 4;
	cout << "value of p: " << *p << endl;
	cout << "value of a: " << aa << endl;	// 输出仍然是3
	cout << "address of p: " << p << endl;
	cout << "address of a: " << &aa << endl;
	// 1、常量是存在符号表中的，不再内存中  2、&a相当于又在内存中创建了一个a的复制品，这个是可以更改的


	int a = 4, b = 5;
	//-- 条件运算符： 表达式1？(表达式2):(表达式3)；表达式1正确则运行表达式2，否则运行表达式3。
	cout << (a > b ? a + b : a - b) << '\n';

	//-- 为了不使隐式类型转换过程中不会造成数据精度丢失，
	//因此是由精度低、范围小的类型转换成精度较高、范围较大的类型

	//-- static_cast<类型名>(表达式)	实现强制类型转换

	//-- 输入输出
	//cin是从键盘读取数据，cout是输出数据到屏幕
	/*
	int aa;
	char bb;
	cin >> aa >> bb;
	cout << "The input data1:" << aa << "   data2:" << bb << '\n';
	*/

	// 设置间隔setw(int n)；setiosflags(ios::left)实现左对齐
	cout << setiosflags(ios::left) << 's' << setw(8) << 'a' << setw(8) << 'b' << endl;

	// 使用标准库 ifstream类 和 ofstream类 来定义
	// 插入运算符"<<"，提取运算符">>"进行文件的读/写操作
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

	//-- String对象
	string str1("Happy");
	string str2(" Birthday!\n");
	cout << (str1+=str2) << '\n';
	// 两个string类型数据的大小取决于 第一个不同字符的ASCII码值


	//-- typedef
	// 重新命名数据类型，例如下面 pstr 的出现就代表着 char*
	typedef char * pstr;
	pstr mystr;
}