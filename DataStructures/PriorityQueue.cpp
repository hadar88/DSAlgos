class PriorityQueue{
    private:
        std::vector<double> A;
        int size;
        static const int QUEUE_MAX_LENGTH = 100;
        function<bool(double,double)> cmp;

        int Parent(int i){
            return (i - 1) / 2;
        }

        int Left(int i){
            return 2 * i + 1;
        }

        int Right(int i){
            return 2 * i + 2;
        }

        void Heapify(int i){
            int l = Left(i);
            int r = Right(i);
            int best = i;

            if(l <= size - 1 && cmp(A[l], A[best]))
                best = l;
            if(r <= size - 1 && cmp(A[r], A[best]))
                best = r;

            if(best != i){
                swap(A[i], A[best]);
                Heapify(best);
            }
        }

        void BuildHeap(){
            if (size == 0)
                return;
            for(int i = Parent(size - 1); i >= 0; i--)
                Heapify(i);
        }

        void BubbleUp(int i) {
            while (i > 0 && cmp(A[i], A[Parent(i)])) {
                swap(A[i], A[Parent(i)]);
                i = Parent(i);
            }
        }

    public:
        PriorityQueue(bool isMax): A(QUEUE_MAX_LENGTH), size(0) {
            if(isMax)
                cmp = [](double a, double b){ return a > b; };
            else
                cmp = [](double a, double b){ return a < b; };
        }

        int IndexOf(double key){
            for(int i = 0; i < size; i++){
                if(A[i] == key)
                    return i;
            }
            return -1;
        }

        int GetSize(){
            return size;
        }

        double Top(){
            if(size == 0)
                throw std::out_of_range("Heap is empty"); 
            return A[0];
        }
        
        double ExtractTop(){
            if(size == 0)
                throw std::out_of_range("Heap underflow");

            double top = A[0];
            A[0] = A[size - 1];
            size--;
            Heapify(0);
            return top;
        }

        void UpdateKey(int i, double key){
            if (i < 0 || i >= size) {
                std::cerr << "Error: Index out of range" << std::endl;
                return;
            }

            if (cmp(A[i], key)) {
                std::cerr << "Error: New key does not improve priority" << std::endl;
                return;
            }
            
            A[i] = key;

            BubbleUp(i);
        }

        void Insert(double key){
            if(size == QUEUE_MAX_LENGTH){
                std::cerr << "Error: Heap overflow" << std::endl;
                return;
            }

            A[size] = key;
            size++;
            BubbleUp(size - 1);
        }

        void HeapSort(){
            BuildHeap();
            int temp_size = size;
            for(int i = size - 1; i >= 1; i--)
                A[i] = ExtractTop();
            size = temp_size;
        }

        void Display(){
            if (size == 0) {
                std::cout << "Priority queue is empty" << std::endl;
                return;
            }
            for(int i = 0; i < size; i++) {
                std::cout << A[i] << " ";
            }
            std::cout << std::endl;
        }
};