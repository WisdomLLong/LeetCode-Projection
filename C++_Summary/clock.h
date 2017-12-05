#pragma once
/*
	声明时钟类的头文件
*/
#include <iostream>
using namespace std;
// 任何一个成员函数访问任何一个成员变量都不受限制
// main()函数中，创建的对象只能访问public成员

class clock // 类的声明
{

private: // 私有成员
	static int couts;	// 静态成员：解决同一类的不同对象之间数据和函数的共享问题。需要在main函数全局变量部分初始化。

protected: // 保护型成员
	// 类的对象不能访问，但是派生类的成员函数可以访问基类的protected成员（访问只是指自己不用定义了，而不是指“共用”）
	int Hour;
	int Minute;
	int Second;
public: // 公有成员
	
	///////// 构造函数 \\\\\\\\\\\
	// 1、复制（拷贝）构造函数	  2、无参构造函数	 3、含参有默认值的构造函数	4、含参无默认值的构造函数	
	// 2，3称为默认构造函数

	clock(const clock& c);	// 复制（拷贝构造函数）
	clock(); // 无参构造函数
	clock(int H = 0, int M = 0, int S = 0);	// 含参有默认值的构造函数
	//clock(int H, int M, int S); // 声明构造函数，为初始化工作
	//clock(int H);	// 重载
	

	// 类名::类名(){};		默认构造函数
	// 类名::类名(){语句...};		无参构造函数

	///////// 析构函数 \\\\\\\\\\\
	// 公有成员函数；系统自动调用；没有返回值；无法重载。
	~clock();		//格式

	///////// 静态成员函数 \\\\\\\\\\\
	// 不通过实体直接访问内部函数
	static void printC()
	{
		cout << "This number of clocks is: " << couts << endl;
	};
	
	//////// 友元函数声明 和 定义 \\\\\\\\\\\
	
	friend void Youyuan(clock aa)
	{
		cout << "可以访问私有数据中的小时啦：" << aa.Hour << endl;
	};


	void SetTime(int newH=0, int newM=0, int newS=0);
	void ShowTime();
	void ShowTime(int n);
};