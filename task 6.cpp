#include<iostream>
using namespace std;
void accept(int Arr[], int s);
void display(int Arr[], int s);
void ssort(int Arr[], int s);
void bsort(int Arr[],int s);
int main()
{
	int Arr[100],n,choice;
	cout<<"Enter Size of Array ";
	cin>>n;
	do
	{
		cout<<"\n\nMENU";
		cout<<"\n1. Accept elements of array";
		cout<<"\n2. Display elements of array";
		cout<<"\n3. Sort the array using selection sort method";
		cout<<"\n4. Sort the array using bubble sort method";
		cout<<"\n5. Exit";
		cout<<"\n\nEnter your choice 1-5 :";
		cin>>choice;
		switch(choice)
		{
			case 1:	accept(Arr,n);
				break;
			case 2:	display(Arr,n);
				break;
			case 3:	ssort(Arr,n);
				break;
			case 4:	bsort(Arr,n);
				break;
			case 5:	break;
			default:cout<<"\nInvalid choice";
		}
	}while(choice!=6);
	return 0;
}
void accept(int Arr[], int s)
{
	for(int I=0;I<s;I++)
	{
		cout<<"Enter element "<<I+1<<":";
		cin>>Arr[I];
	}
}
void display(int Arr[], int s)
{
	cout<<"The elements of the array are:\n";
	for(int I=0;I<s;I++)
		cout<<Arr[I]<<" ";
}

void bsort(int Arr[],int s)
{
	int I,J,Temp;
	for(I=0;I<s-1;I++)
	{
		for(J=0;J<(s-1-I);J++)
			if(Arr[J]>Arr[J+1])
			{
				Temp=Arr[J];
				Arr[J]=Arr[J+1];
				Arr[J+1]=Temp;
			}
	}
}
