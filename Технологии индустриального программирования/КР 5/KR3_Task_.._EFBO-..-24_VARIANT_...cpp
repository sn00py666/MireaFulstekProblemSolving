#include <iostream>
#include <stack>

int main() {
    std::stack<int> stack;

    stack.push(10);
    stack.push(20);
    stack.push(30);

    std::cout << "Размер: " << stack.size() << std::endl;
    std::cout << "Верхний элемент: " << stack.top() << std::endl;

    stack.pop();
    std::cout << "Размер после Удаления: " << stack.size() << std::endl;

    std::cout << "Новый верхний элемент: " << stack.top() << std::endl;

    stack.pop();
    stack.pop();
    std::cout << "Размер после удаления всех элементов: " << stack.size() << std::endl;


    return 0;
}
