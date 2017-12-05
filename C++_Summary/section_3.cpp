#include <iostream>

using namespace std;

void main_3()
{
	//-- if; else; else if
	// 需要注意的是，else与最接近的if想匹配，与缩进无关

	if ( const int bb = 55)
	{
		cout << "Just test" << '\n';
	}
	else
	{
		cout << "const can not be transformed into bool data" << '\n';
	}

	// 函数调用的格式（如果返回的是一个数值的话）
	int count1(1);
	cout << "函数的调用方式： 函数名 变量名(输入参数) \n" << "例如这里int函数定义的变量值为：" << count1 << '\n';

	//-- switch
	/*
	switch(表达式)
	{
	case 常量表达式1:
		语句1;
		break;
	default:
		语句2;
	}
	*/

	//-- 一般用for语句实现训话你次数确定的问题，而用while和do-while实现循环次数不确定的情况

	//-- continue跳出当前这一次循环，break是跳出这个循环体
}