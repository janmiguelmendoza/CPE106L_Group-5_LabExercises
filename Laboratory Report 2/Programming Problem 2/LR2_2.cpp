#include <iostream>
#include <fstream>
#include <vector>
#include <string>

int main() {
    std::string filename;
    std::cout << "Enter the filename: ";
    std::cin >> filename;

    std::ifstream file(filename);
    if (!file) {
        std::cerr << "File '" << filename << "' not found." << std::endl;
        return 1;
    }

    std::vector<std::string> lines;
    std::string line;
    while (std::getline(file, line)) {
        lines.push_back(line);
    }

    int line_number;
    while (true) {
        std::cout << "The file contains " << lines.size() << " lines." << std::endl;
        std::cout << "Enter a line number (0 to quit): ";
        std::cin >> line_number;

        if (line_number == 0) {
            std::cout << "Exiting the program." << std::endl;
            break;
        } else if (line_number > 0 && line_number <= lines.size()) {
            std::cout << "Line " << line_number << ": " << lines[line_number - 1] << std::endl;
        } else {
            std::cout << "Invalid line number. Please try again." << std::endl;
        }
    }

    return 0;
}
