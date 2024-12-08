#include <iostream>

void findCombinations(int arr[], int n, int k, int start, int current[], int currentSize) {
    if (currentSize == k) {
        for (int i = 0; i < k; ++i) {
            std::cout << current[i] << " ";
        }
        std::cout << std::endl;
        return;
    }

    for (int i = start; i < n; ++i) {
        current[currentSize] = arr[i];
        findCombinations(arr, n, k, i + 1, current, currentSize + 1); 
    }
}

void findAllCombinations(int arr[], int n) {
    int current[100];  // если список больше 100 эл нужно увеличить

    for (int k = 1; k <= n; ++k) {
        findCombinations(arr, n, k, 0, current, 0);
        std::cout << std::endl;
    }
}

int main() {
    //  Тут пишем массив
    int arr[] = {1, 2, 3, 4};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    findAllCombinations(arr, n);

    return 0;
}
