// Котовщиков, решал задачи 1(25) и 3(1)
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    int n, targetSum;

    cout << "Введите размер массива: ";
    cin >> n;
    int arr[n]; 

    srand(time(NULL));

    // Зпаолняем рандомными числами от 1 до 100, я тут по условию не очень понял какой нужен диапазон
    for (int i = 0; i < n; ++i) {
        arr[i] = std::rand() % 100 + 1;
    }

    cout << "Сгенерированный массив: ";
    for (int i = 0; i < n; ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    cout << "Введите желаемую сумму: ";
    cin >> targetSum;

    int pairCount = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (arr[i] + arr[j] == targetSum) {
                pairCount++;
            }
        }
    }

    cout << "Количество пар, сумма которых = " << targetSum << ": " << pairCount << endl;

    return 0;
}
