// Котовщиков, решал задачи 1(25) и 3(1)
#include <iostream>
using namespace std;

int suma(int a, int b){
    return a + b;
}

int main()
{
    cout << "Введите 2 числа: ";
    int a, b;
    cin >> a;
    cin >> b;
    cout << "Сумма чисел "<< a << " и " << b << " = " << suma(a,b);
    
    return 0;
}