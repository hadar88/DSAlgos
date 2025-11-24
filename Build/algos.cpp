#include <climits>

extern "C"{
    // Insertion Sort
    void InsertionSort(int A[], int size){
        for (int j = 1; j <= size - 1; j++){
            int key = A[j];
            int i = j - 1;
            while(i >= 0 && A[i] > key){
                A[i + 1] = A[i];
                i--;
            }
            A[i + 1] = key;
        }
    }

    // Merge Sort
    void Merge(int A[], int left, int mid, int right){
        int n1 = mid - left + 1;
        int n2 = right - mid;

        int* L = new int[n1 + 1];
        int* R = new int[n2 + 1];

        for(int i = 0; i < n1; i++)
            L[i] = A[left + i];
        for(int j = 0; j < n2; j++)
            R[j] = A[mid + j + 1];
        L[n1] = INT_MAX;
        R[n2] = INT_MAX;
        
        int i = 0;
        int j = 0;

        for(int k = left; k <= right; k++){
            if(L[i] <= R[j]){
                A[k] = L[i];
                i++;
            }
            else{
                A[k] = R[j];
                j++;
            }
        }
    }

    void MergeSort(int A[], int left, int right){
        if(left < right){
            int mid = (left + right) / 2;
            MergeSort(A, left, mid);
            MergeSort(A, mid + 1, right);
            Merge(A, left, mid, right);
        }
    }

    // Quick Sort
    int Partition(int A[], int left, int right){
        int i = left - 1;
        for(int j = left; j <= right - 1; j++){
            if(A[j] <= A[right]){
                i++;
                int temp = A[i];
                A[i] = A[j];
                A[j] = temp;
            }
        }
        int temp = A[i + 1];
        A[i + 1] = A[right];
        A[right] = temp;
        return i + 1;
    }

    void QuickSort(int A[], int left, int right){
        if(left < right){
            int p = Partition(A, left, right);
            QuickSort(A, left, p - 1);
            QuickSort(A, p + 1, right);
        }
    }

    // Counting Sort
    void CountingSort(int A[], int B[], int k, int size){
        int* C = new int[k + 1];
        for(int i = 0; i <= k; i++)
            C[i] = 0;
        for(int i = 0; i < size; i++)
            C[A[i]] = C[A[i]] + 1;
        for(int i = 1; i <= k; i++)
            C[i] = C[i] + C[i - 1];
        for(int i = size - 1; i >= 0; i--){
            B[C[A[i]] - 1] = A[i];
            C[A[i]] = C[A[i]] -1;
        }
    }

    
}
// run this to build the library: g++ -shared -fPIC -o algos.so algos.cpp