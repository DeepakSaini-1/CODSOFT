#include <iostream>
using namespace std;

int swap(int *x, int *y){
    *x+=*y;
    *y=*x-*y;
    *x=*x-*y;
    return 0;
}

int reverse(int arr[],int size){
    int start=0, end=size-1;
    while(start<end){
        swape(&arr[start],&arr[end]);
        start++;
        end--;
    }
    return 0;
}

int main(){
    int arr[]={1,2,3,4,5,6,7,8,9,10,78,79,80,81};
    int size = sizeof(arr)/sizeof(int);
    reverse(arr,size);
    for(int i=0;i<size;i++){
        cout << arr[i] << ", ";
    }
    return 0;
}