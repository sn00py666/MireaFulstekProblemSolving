#include <iostream>
#include <string>

int main() {
    std::string date;
    std::cout << "Введите дату в формате гггг-мм-дд: ";
    std::cin >> date;

    if (date.size() == 10 && date[4] == '-' && date[7] == '-') {
        std::string year = date.substr(0, 4);
        std::string month = date.substr(5, 2);
        std::string day = date.substr(8, 2);

        std::cout << "Дата в формате дд/мм/гггг: " << day << "/" << month << "/" << year << std::endl;
    } else {
        std::cout << "Некорректный формат даты. Пожалуйста, введите дату в формате гггг-мм-дд." << std::endl;
    }

    return 0;
}
