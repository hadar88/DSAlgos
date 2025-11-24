class PriorityQueue{
    private:
        std::vector<int> A;
        int size;
        static const int QUEUE_MAX_LENGTH = 100;

        int Parent(int i){
            return (i - 1) / 2;
        }

        int Left(int i){
            return 2 * i + 1;
        }

        int Right(int i){
            return 2 * i + 2;
        }

        void MaxHeapify(int i){
            int l = Left(i);
            int r = Right(i);
            int largest = i;

            if(l <= size - 1 && A[l] > A[largest])
                largest = l;
            if(r <= size - 1 && A[r] > A[largest])
                largest = r;

            if(largest != i){
                int temp = A[i];
                A[i] = A[largest];
                A[largest] = temp;
                MaxHeapify(largest);
            }
        }

        void BuildMaxHeap(){
            for(int i = Parent(size - 1); i >= 0; i--)
                MaxHeapify(i);
        }

    public:
        PriorityQueue(): A(QUEUE_MAX_LENGTH), size(0) {}

        int GetSize(){
            return size;
        }

        int Maximum(){
            return A[0];
        }
        
        int ExtractMax(){
            if(size == 0)
                throw std::out_of_range("Heap underflow");

            int max = A[0];
            A[0] = A[size - 1];
            size--;
            A[size] = 0;
            MaxHeapify(0);
            return max;
        }

        void IncreaseKey(int i, int key){
            if(key < A[i])
                throw std::invalid_argument("New key is smaller than current key");
            
            A[i] = key;
            while(i > 0 && A[Parent(i)] < A[i]){
                int temp = A[i];
                A[i] = A[Parent(i)];
                A[Parent(i)] = temp;
                i = Parent(i);
            }
        }

        void Insert(int key){
            if(size == QUEUE_MAX_LENGTH)
                throw std::overflow_error("Heap overflow");

            A[size] = INT_MIN;
            size++;
            IncreaseKey(size - 1, key);
        }

        void HeapSort(){
            BuildMaxHeap();
            int temp_size = size;
            for(int i = size - 1; i >= 1; i--)
                A[i] = ExtractMax();
            size = temp_size;
        }

        void Display(){
            for(int i = 0; i < size; i++) {
                std::cout << A[i] << " ";
            }
            std::cout << std::endl;
        }


};