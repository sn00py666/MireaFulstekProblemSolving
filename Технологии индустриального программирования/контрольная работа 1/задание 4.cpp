#include <iostream>
#include <cmath>
#include <string> 

int main() {
    int a, b, c;
    std::string s; 
    
    double d;

    std::cin >> a >> b >> c >> s; 

    if (s == "R") {
        std::cout << "Kotovshchikov Andrey" << std::endl;
    } 
    else if (s == "c") {
        if (a == 0 && b == 0 && c == 0) {
            std::cout << "x ∈ R" << std::endl;
        } else {
            d = b * b - 4 * a * c;
            if (d == 0) {
                std::cout << (-b) / (2.0 * a) << std::endl; 
            } else if (d > 0) {
                std::cout << (-b + sqrt(d)) / (2.0 * a) << std::endl; 
                std::cout << (-b - sqrt(d)) / (2.0 * a) << std::endl; 
            } else {
                std::cout << "Решений не существует" << std::endl;
            }
        }
    }
    if (s == "s") {
        double r;
        double st;
        if (3.14 * r * r > st * st){
            std::cout << "Площадь круга больше" << std::endl;
        }
        if (3.14 * r * r < st * st){
            std::cout << "Площадь квадрата больше" << std::endl;
        }
        if (3.14 * r * r == st * st){
            std::cout << "Площади равны" << std::endl;
        }
        
    } 
    
    
    return 0;
}
