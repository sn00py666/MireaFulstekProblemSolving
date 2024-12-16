#include <iostream>
using namespace std;

int count_triangles(int P, int Q) {
    int count = 0;
    for (int c = P; c <= Q; ++c) {
        for (int a = P; a <= c; ++a) {
            int b_start = max(a, c - a + 1);
            for (int b = b_start; b <= c; ++b) {
                count++;
            }
        }
    }
    
    return count;
}

int main() {
    int P, Q;
    cin >> P >> Q;
    
    cout << count_triangles(P, Q) << endl;

    return 0;
}
