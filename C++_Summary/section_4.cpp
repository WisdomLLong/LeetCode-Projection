#include <iostream>

using namespace std;


///////////
//���鼰������������
///////////
void main_4()
{
	//-------------- ���� -------------------
	int score[4] = { 80, 70, 90, 85 }; //����
	int score_2[] = { 80, 70, 90, 85 };
	cout << score[3] << '\n';

	//------------- �ַ����� ------------------
	char chArray[] = "Happy Birthday!";
	char buffer[9];

	///���������ַ�����ķ�ʽ
	//1���������������ַ�
	for (int i = 0; i < 9; i++)
	{
		cin >> buffer[i];
	}
	//2�����������ַ��������ո��س�����
	cin >> buffer;
	//3������һ���ַ��������س�����
	cin.getline(buffer, 9, '\n');	//��Ҫע����ǵ�9���ַ��� '\0' ��������cout��������һ���ո�

	///���
	cout << buffer << '\n';	// ֻ��char���͵��������ֱ���������
	for (int i = 0; i <= 8; i++)
	{
		cout << buffer[i] << " ";
	}
	cout << '\n';

	//------------ ��ά���� --------------
	const int M = 3, N = 3;	// ע���ʽ
	char lucky_tree[M][N] =	// []�б�ʾ����������������Ŀǰ�Ľ������������ܿ�
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

	//------------- ö������ ----------------
	// �Լ�����һ���������ͣ����������ܵ�ȡֵ
	enum weekday { sun, mon, tue, wed, thu, fri, sat = 7 };
	// �����ö��Ԫ�����г�ʼֵ�ģ��ֱ��� 0, 1, 2, ... ��Ҳ�����ڶ���ʱ��ֵ
	// ö��ֵֻ�ܽ��� ��ϵ����
	weekday day1 = sun, day2;
	int besend = day1;	// ö�����͵�ֵ����ֱ�Ӹ�����ֵ���͵�ֵ
	day2 = (weekday)3;	// ������ֻ�ܽ���ǿ������ת��
	cout << "ö������ֵ�� " << day1 << endl;
	cout << "��ö��ֵ��ֵ����ֵ���͵�ֵ�� " << besend << endl;
	cout << "��ö������ǿ������ת������ֵ���͵�ֵ�� " << day2 << endl;
	// ���Է���ֻ��ö��ֵ��ʾ��ֻ������

	//-------------- �ṹ���� ----------------
	// �����鲻ͬ���ǣ�����ͬʱ�洢��ͬ���͵�ֵ
	// char �� string ������ ǰ����һ���������ͣ������Ƿ�װ�õ�һ����
	struct student
	{
		long num;
		char name[20];
		int age;
	} stu{2016111349, "Wisdom Long", 18};
	cout << stu.name << endl;

	//-------------- �ṹ���� ----------------
	// ����˵���������ÿһ��Ԫ�ض���һ���ṹ�壬��������ṹ��
	struct student_array
	{
		long num;
		char name[20];
		int age;
	};
	student_array calssA[5] = { {2016111349, "Wisdom Long", 18}, 
								{2016111350, "Wisdom LLong", 18} };

	//-------------- �������� -----------------
	// ͬһ���ڴ�ɴ�ż��ֲ�ͬ���͵ĳ�Ա������ĳһ��ʱ�����ܴ��һ�֣�ͨ����Ϊ�ṹ���͵���Ƕ��Ա��
	// ����ֻ�ó�ʼ��һ��person��struct�����;Ϳ��Դ�� ѧ�� �� ��ʦ ��ְҵ��Ϣ
	struct person 
	{
		int num;
		string name;
		union {
			int classes;	// Ϊѧ����Ű༶
			char position[10];	// Ϊ��ʦ���ְ��
		};
	};
	person ux;
	ux.num = 4;
	ux.name = "wisdomlong";
	ux.classes = 5;
	/////// �ر�ע�� \\\\\\\
	
	char position_2[10] = "professor";
	ux.position[9] = 'f'; 
	// ux.position = "professor";
	// һ������ָ��̶��󣬲�������ָ����һ�����ݣ������������Ǵ���ģ����ڶ����ʱ���ǿ��Եģ�Ҳ�������ĳ��ֵ�����޸ġ�
	// Ҫô��string��Ҫô��cin
	// char ���ʺϴ��ݣ������Ǹ�ֵ��
	cin >> ux.position;
	cout << ux.position << endl;
	cout << ux.classes;	// ���������Ѿ����� 5 �ˣ����Ǵ�ӡ��ȥ��position��int����ת������ʽ��


}
