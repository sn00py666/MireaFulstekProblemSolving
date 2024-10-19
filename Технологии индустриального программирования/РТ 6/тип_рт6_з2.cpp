#include <iostream>

int main() {
    int N, M, W;
    std::cin >> N >> M >> W;
    char map[32][32] = { '0' };
    for (int i = 0; i < W; ++i) {
        int x, y;
        std::cin >> x >> y;
        x--;
        y--;
        map[x][y] = '*';
    }
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (map[i][j] == '*') {
                continue;
            }

            int count = 0;
            for (int dx = -1; dx <= 1; ++dx) {
                for (int dy = -1; dy <= 1; ++dy) {
                    if (dx == 0 && dy == 0) continue;
                    int ni = i + dx, nj = j + dy;
                    if (ni >= 0 && ni < N && nj >= 0 && nj < M && map[ni][nj] == '*') {
                        count++;
                    }
                }
            }
            map[i][j] = count + '0';
        }
    }
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            std::cout << map[i][j];
        }
        std::cout << std::endl;
    }
    return 0;
}
