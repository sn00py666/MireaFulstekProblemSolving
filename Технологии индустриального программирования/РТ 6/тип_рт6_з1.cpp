#include <iostream>

int main() {
    int N;
    std::cin >> N;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (j < N - 1 - i) {
                std::cout << 0 << " ";
            } else if (j == N - 1 - i) {
                std::cout << 1 << " ";
            } else {
                std::cout << 2 << " ";
            }
        }
        std::cout << std::endl;
    }
    return 0;
}
