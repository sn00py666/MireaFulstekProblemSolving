#include <iostream>
#include <vector>
using namespace std;

int main() {
    // vector<vector<int>> a = {{2, 30, 2, 3}, {10, 2, 2, 2}, {-3, 20, 2, 2}};
    
    size_t m, n;
    std::cout << "введите число строк а потом число столбцов" << std::endl; 
    std::cin >> m >> n;
    std::vector<std::vector<int>> a(m, std::vector<int>(n));
    for (size_t i = 0; i != m; ++i) {
        for (size_t j = 0; j != n; ++j) {
            std::cin >> a[i][j];
        }
    }
    
    vector<vector<int>> b(m, vector<int>(n, 0));
    
    cout << endl;
    
    for (size_t i = 0; i < a.size(); ++i) {
        for (size_t j = 0; j < a[i].size(); ++j) {
            if (i == 0 && j == 0) {
                b[i][j] = a[i][j];
            }
            else if (i == 0) {
                b[i][j] = a[i][j] + b[i][j-1];
            }
            else if (j == 0) {
                b[i][j] = a[i][j] + b[i-1][j];
            }
            else {
                b[i][j] = max(a[i][j] + b[i-1][j], a[i][j] + b[i][j-1]);
            }
        }
    }
    
    // for (const auto& row : b) {
    //     for (auto value : row) {
    //         cout << value << ' ';
    //     }
    //     cout << endl;
    // }
    
    size_t i = b.size()-1;
    size_t j = b[i].size()-1;
    // cout << endl;
    
    vector<pair<size_t, size_t>> itog = {{i, j}};
    while (i != 0 || j != 0) {
        if (i != 0 && j != 0) {
            if (b[i-1][j] > b[i][j-1]) {
                i--;
            }
            else {
                j--;
            }
        }
        else if (i == 0) {
            j--;
        }
        else if (j == 0) {
            i--;
        }
        itog.push_back({i, j});
    }
    
    for (size_t k = 1; k <= itog.size(); ++k) {
        cout << "(" << itog[itog.size() - k].first << ", " << itog[itog.size() - k].second << ")" << endl;
    }
    
    return 0;
}
