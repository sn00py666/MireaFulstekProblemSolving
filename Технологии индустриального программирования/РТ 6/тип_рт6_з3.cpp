#include <iostream>
#include <string>

std::string nextTerm(const std::string& term) {
    std::string result;
    int count = 1;
    
    for (size_t i = 1; i <= term.length(); ++i) {
        if (i < term.length() && term[i] == term[i - 1]) {
            count++;
        } else {
            result += std::to_string(count) + term[i - 1];
            count = 1;
        }
    }
    return result;
}

int main() {
    int x, n;
    std::cin >> x >> n;
    std::string currentTerm = std::to_string(x);
    for (int i = 1; i < n; ++i) {
        currentTerm = nextTerm(currentTerm);
    }
    std::cout << currentTerm << std::endl;
    return 0;
}
