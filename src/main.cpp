#if defined(__APPLE__)
#include <Python/Python.h>
#else
#include <Python.h>
#endif

const char projectName[] = "Project Epsilon";
uint8_t selection;

int main(int argc, char * argv[])
{
  std::cout << "Hello, Welcome to the " << projectName << " installer!\nWhat do you want to install?\n1: The main package.\nType the number of what you want.\n";
  std::cin >> selection;
}