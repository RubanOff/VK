#include <iostream>

void ReverseArray(double arr[], int length, int pointer)
{
    for(int i = 0; i < length/2; i++)
    {
        std::swap(arr[i], arr[length - 1 - i]);
    }
}

int main()
{   
    double arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int length = sizeof(arr)/sizeof(arr[0]);
    int pointer = 3;

    ReverseArray(arr, length, pointer);

    for(int i = 0; i < length; i++)
    {
        std::cout << arr[i] << ", ";
    }

    return 0;
}


