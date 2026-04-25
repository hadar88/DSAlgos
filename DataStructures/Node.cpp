template<typename T>

class Node{
    private:
        T data;
        Node<T>* next;

    public:
        Node(T value): data(value), next(nullptr) {}
        
        T GetData(){
            return data;
        }

        Node<T>* GetNext(){
            return next;
        }

        void SetData(T value) {
            data = value;
        }

        void SetNext(Node<T>* nextNode){
            next = nextNode;
        }
};