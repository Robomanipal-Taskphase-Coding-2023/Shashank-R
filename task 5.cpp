#include<iostream>
using namespace std;
int b;
int d;
char decision;


int convertDecimalToBinary(int);


cout << "The Decimal Calculator";

decimal:
cout << "\n" << "Enter a decimal value: ";
cin >> d;

conversion:

cout << "\n\nDo you want to convert " << d
    << " to Binary (b), Octal (o), or Hexadecimal (h)?: ;
cin >> decision;
if (decision == 'b')
{
    b = convertDecimalToBinary(d);
    cout << "\n\nThe decimal value you inputted, " << d << ", in binary: " << b << endl;
}


int convertDecimalToBinary(int decimal)
{

    int x = decimal;
    int i = 0;
    int a = 1;
    int remainder;
    int binary = 0;
    int step;


    while (x != 0)
    {
        i++;
        step = x / 2;
        remainder = x % 2;
        cout << "| Stage " << i << ": " << x << " / 2 = " << step << " | Remainder: " << remainder << " | " << endl;
        x /= 2;
        binary += remainder * a;
        a *= 10;
    }


    return binary;
}
