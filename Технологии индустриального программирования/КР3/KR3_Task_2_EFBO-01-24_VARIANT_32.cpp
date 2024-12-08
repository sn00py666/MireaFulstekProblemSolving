#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>

std::string generateGreeting(const std::string& name) {
    std::vector<std::string> greetings = {
        "Счастья и успехов, " + name + "!",
        "Поздравляю, " + name + "!",
        name + ", пусть сбудутся мечты!",
        "Всего наилучшего, " + name + "!",
        name + ", радости и удачи!"
    };

    int randomIndex = rand() % greetings.size();
    return greetings[randomIndex];
}

int main() {
    std::srand(std::time(0));

    std::ifstream inputFile("names.txt");
    std::ofstream outputFile("greetings.txt");

    if (!inputFile || !outputFile) {
        std::cerr << "не удалось открыть файл." << std::endl;
        return 1;
    }

    std::string name;
    while (std::getline(inputFile, name)) {
        if (!name.empty()) {
            outputFile << generateGreeting(name) << std::endl;
        }
    }
    
    return 0;
}
