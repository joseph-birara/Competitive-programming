#include <stdio.h>

int main() {
    int num = 42;
    int* ptr = &num;
    int** ptrToPtr = &ptr;

    printf("Value of num: %d\n", num);
    printf("Value of ptr: %p\n", (void*)ptr);
    printf("Value of ptrToPtr: %p\n", (void*)ptrToPtr);

    printf("Value pointed by ptrToPtr: %d\n", **ptrToPtr);

    return 0;
}
