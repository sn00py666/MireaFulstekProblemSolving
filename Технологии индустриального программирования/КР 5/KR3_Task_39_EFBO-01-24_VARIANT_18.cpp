#include <iostream>
#include <set>
#include <vector>

// Функция для получения всех подмножеств множества
std::vector<std::set<int>> getSubsets(const std::set<int>& originalSet) {
    std::vector<int> elements(originalSet.begin(), originalSet.end());
    std::vector<std::set<int>> subsets;

    int totalSubsets = 1 << elements.size();
    
    for (int mask = 0; mask < totalSubsets; ++mask) {
        std::set<int> subset;
        for (int i = 0; i < elements.size(); ++i) {
            if (mask & (1 << i)) {
                subset.insert(elements[i]);
            }
        }
        subsets.push_back(subset);
    }

    return subsets;
}

int main() {
    std::set<int> mySet = {1, 2, 3};

    std::vector<std::set<int>> subsets = getSubsets(mySet);

    std::cout << "подмножества множества: {1, 2, 3}" << std::endl;
    for (const auto& subset : subsets) {
        std::cout << "{";
        for (auto it = subset.begin(); it != subset.end(); ++it) {
            std::cout << *it;
            if (std::next(it) != subset.end()) {
                std::cout << ", ";
            }
        }
        std::cout << "}" << std::endl;
    }

    return 0;
}
