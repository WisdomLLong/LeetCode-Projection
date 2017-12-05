#include <iostream>

using namespace std;


///////////
//数组及其他定义类型
///////////
void main_4()
{
	//-------------- 数组 -------------------
	int score[4] = { 80, 70, 90, 85 }; //或者
	int score_2[] = { 80, 70, 90, 85 };
	cout << score[3] << '\n';

	//------------- 字符数组 ------------------
	char chArray[] = "Happy Birthday!";
	char buffer[9];

	///三种输入字符数组的方式
	//1、接收逐个输入的字符
	for (int i = 0; i < 9; i++)
	{
		cin >> buffer[i];
	}
	//2、接收整个字符串，遇空格或回车结束
	cin >> buffer;
	//3、接收一行字符，遇到回车结束
	cin.getline(buffer, 9, '\n');	//需要注意的是第9个字符是 '\0' 结束符，cout出来的是一个空格

	///输出
	cout << buffer << '\n';	// 只有char类型的数组可以直接输出内容
	for (int i = 0; i <= 8; i++)
	{
		cout << buffer[i] << " ";
	}
	cout << '\n';

	//------------ 多维数组 --------------
	const int M = 3, N = 3;	// 注意格式
	char lucky_tree[M][N] =	// []中表示的是行数和列数，目前的结论是列数不能空
	{
		' ', '6', ' ',
		'6', ' ', '6',
		' ', '6', ' ',
	};
	for (int i = 0; i < M; i++)
	{
		for (int k = 0; k < N; k++)
		{
			cout << lucky_tree[i][k] << ' ';
		}
		cout << '\n';
	}

	//------------- 枚举类型 ----------------
	// 自己定义一种数据类型，并给出可能的取值
	enum weekday { sun, mon, tue, wed, thu, fri, sat = 7 };
	// 这里的枚举元素是有初始值的，分别是 0, 1, 2, ... 但也可以在定义时赋值
	// 枚举值只能进行 关系运算
	weekday day1 = sun, day2;
	int besend = day1;	// 枚举类型的值可以直接赋给数值类型的值
	day2 = (weekday)3;	// 反过来只能进行强制类型转换
	cout << "枚举类型值： " << day1 << endl;
	cout << "被枚举值赋值的数值类型的值： " << besend << endl;
	cout << "被枚举类型强制类型转化的数值类型的值： " << day2 << endl;
	// 可以发现只会枚举值显示的只是数字

	//-------------- 结构类型 ----------------
	// 与数组不同的是，可以同时存储不同类型的值
	// char 与 string 的区别： 前者是一个基础类型，后者是封装好的一个类
	struct student
	{
		long num;
		char name[20];
		int age;
	} stu{2016111349, "Wisdom Long", 18};
	cout << stu.name << endl;

	//-------------- 结构数组 ----------------
	// 简单来说就是数组的每一个元素都是一个结构体，数组包含结构体
	struct student_array
	{
		long num;
		char name[20];
		int age;
	};
	student_array calssA[5] = { {2016111349, "Wisdom Long", 18}, 
								{2016111350, "Wisdom LLong", 18} };

	//-------------- 联合类型 -----------------
	// 同一段内存可存放几种不同类型的成员，但在某一个时刻智能存放一种；通常作为结构类型的内嵌成员。
	// 例如只用初始化一个person的struct的类型就可以存放 学生 和 教师 的职业信息
	struct person 
	{
		int num;
		string name;
		union {
			int classes;	// 为学生存放班级
			char position[10];	// 为教师存放职称
		};
	};
	person ux;
	ux.num = 4;
	ux.name = "wisdomlong";
	ux.classes = 5;
	/////// 特别注意 \\\\\\\
	
	char position_2[10] = "professor";
	ux.position[9] = 'f'; 
	// ux.position = "professor";
	// 一旦数组指针固定后，不能重新指向另一个数据，因此上面语句是错误的，而在定义的时候是可以的，也可以针对某个值进行修改。
	// 要么用string，要么用cin
	// char 更适合传递，而不是赋值。
	cin >> ux.position;
	cout << ux.position << endl;
	cout << ux.classes;	// 这里面存的已经不是 5 了，而是打印进去的position的int类型转换的形式。


}
