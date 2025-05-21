#include <iostream>
#include <cstddef> // offsetof
using namespace std;

class Test
{
private:
    int a;
    double b;
    char c;
public:
    Test(): a(10), b(3.14), c('X') {}
};

int main() {
    Test obj;
    char* ptr = reinterpret_cast<char*>(&obj);

    size_t offset_a = 0;
    size_t offset_b = (offset_a + sizeof(int) + 7) & ~7;
    size_t offset_c = offset_b + sizeof(double);

    int* aPtr = reinterpret_cast<int*>(ptr + offset_a);
    double* bPtr = reinterpret_cast<double*>(ptr + offset_b);
    char* cPtr = reinterpret_cast<char*>(ptr + offset_c);

    cout << "a: " << *aPtr << endl;
    cout << "b: " << *bPtr << endl;
    cout << "c: " << *cPtr << endl;

    return 0;
}
