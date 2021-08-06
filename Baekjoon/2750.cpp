#include <iostream>
#include <stdio.h>

using namespace std;

void copy(int nums[], int sorted[], int left, int right){
    for(int i=left; i<=right; i++){
        nums[i]=sorted[i];
    }
}

void merge(int nums[], int sorted[], int left, int mid, int right){
    int i = left;
    int j = mid+1;
    int k = i;

    while(i<=mid && j<=right){
        if(nums[i]<=nums[j]){
            sorted[k] = nums[i];
            i++;
            k++;

        }else{
            sorted[k] = nums[j];
            j++;
            k++;
        }
    }

    if(j<=right){
        while(j<=right){
            sorted[k] = nums[j];
            j++;
            k++;
        }
    }else{
        while(i<=mid){
            sorted[k] = nums[i];
            i++;
            k++;
        }
    }

    copy(nums, sorted, left, right);
}

void mergesort(int nums[], int sorted[], int left, int right){
    int mid = (left + right) / 2;
    if(left!=right){
        mergesort(nums, sorted, left, mid);
        mergesort(nums, sorted, mid+1, right);
    }
    merge(nums, sorted, left, mid, right);
}

int main()
{
    int num;
    cin >> num;

    int nums[num];
    int sorted[num];

    for(int i=0; i<num; i++){
        cin >> nums[i];
        sorted[i] = -1;
    }

    mergesort(nums, sorted, 0, num-1);

    for (int i=0; i < num; i++) {
        cout << sorted[i] << ' ';
    }
    cout << '\n';
}
