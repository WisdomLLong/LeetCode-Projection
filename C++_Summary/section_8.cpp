#include <iostream>
#include <cstring>
#include <string>
#include "clock.h"
#include "watch.h"


using namespace std ;

///////////
// 继承与派生
///////////

//////////////////////////////////////////////////////////////////////////
// 继承的概念

// 现有的类为基类，新建立的类为派生(继承)类
// class 派生类名: 继承方式(public,private,protected) 基类 {}；
// 不论哪一种继承方式，派生类的成员函数可以访问基类的public,protected成员。
// 只有以public继承方式的派生类对象才能访问基类的public成员

// 注意同名覆盖于重载的区别，前者多用于派生类与基类之间，而后者多用于同一个类内部

void main_8()
{
	clock c1(8, 8, 8);
	//clock c2 = (10, 10, 10);
	clock* c3 = new clock(9, 9, 9);
	c1.ShowTime();
	c3->ShowTime();

	watch w1(6, 6, 6, "winter");
	w1.ShowTime();

	c1 = w1;	// 派生类到基类的转换
	c3 = &w1;	// 基类对象指针指向派生类对象
	cout << '\n';
	c1.ShowTime();
	c3->ShowTime();
	w1.ShowTime();


}







