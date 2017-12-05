#include <iostream>
#include "clock.h"

// watch类是clock的派生类

using namespace std;

class watch : public clock
{
protected:
	string weather = "winter";

public:
	watch(int H, int M, int S, string w):clock(H, M, S) 
	{
		weather = w;
	}
	void ShowTime()
	{
		cout <<  weather << "\t天气\t" << Hour << "\t:\t" << Minute << "\t:\t" << Second << endl;
	}
};
