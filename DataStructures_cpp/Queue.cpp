class Queue{
    private:
        LinkedList* list;

    public:
        Queue() {
            list = new LinkedList();
        }

        ~Queue(){
            delete list;
        }

        bool IsEmpty(){
            return list->IsEmpty();
        }

        void Enqueue(int item){
            list->InsertLast(item);
        }

        int Dequeue(){
            if (list->IsEmpty()) {
                throw std::runtime_error("Queue is empty");
            }
            Node<int>* head = list->GetHead();
            int item = head->GetData();
            list->Delete(item);
            return item;
        }

        void Display(){
            list->Display();
        }
};