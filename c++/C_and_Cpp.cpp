#include<iostream>									// #include<stdio.h>

using namespace std;

int main()
{
	cout << "Hello world" << endl;					// printf("Hello world\n");
	
	int x = 10, y = 20;
	cout << "x = " << x << "y = " << y << endl;		// printf("x = %d y = %d\n",x,y);

	cout << "Input Number = ";
	cin >> x;										// scanf("%d",&x);
	cout << "x = " << x << endl;
	
	bool b = true;

	if(b)
		cout << "b is true" << endl;
	else
		cout << "b is false" << endl;

	cout.setf(ios::boolalpha);						// bool 형 출력(true or false)
	cout << b << !b << endl;

	cout.setf(ios::boolalpha);

	auto i2 = 10;									// int i2 = 10;
	auto d2 = 3.14;									// int d2 = 3.14;

	cout << "auto i2 = " << i2 << "auto d2 = " << d2 << endl;
	return 0;
}
