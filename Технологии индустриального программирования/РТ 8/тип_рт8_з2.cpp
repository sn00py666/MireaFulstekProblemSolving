
#include <iostream>
using namespace std;

int NOD(int a, int b){
    if (!b){
        return a;
    }
    return NOD(b, a % b);
}

int main()
{
    cout << NOD(42, 18);

    return 0;
}