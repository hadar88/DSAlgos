#include "algos.h"

extern "C"{
    // Insertion Sort
    void Insertion(int A[], int size){
        InsertionSort(A, size);
    }
    
    // Merge Sort
    void Merge(int A[], int left, int right){
        MergeSort(A, left, right);
    }

    // Quick Sort
    void Quick(int A[], int left, int right){
        QuickSort(A, left, right);
    }

    // Counting Sort
    void Counting(int A[], int B[], int k, int size){
        CountingSort(A, B, k, size);
    }

    // Kruskal's Algorithm
    Graph* Kruskal(Graph* g){
        try{
            return KruskalMST(g);
        } catch (const std::invalid_argument& e) {
            std::cerr << "Error: " << e.what() << std::endl;
            return nullptr;
        }
    }

    // Prim's Algorithm
    Graph* Prim(Graph* g){
        try{
            return PrimMST(g);
        } catch(const std::invalid_argument& e) {
            std::cerr << "Error: " << e.what() << std::endl;
            return nullptr;
        }
    }
}