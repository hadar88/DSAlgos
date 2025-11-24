class Stack{
    private:
        LinkedList* list;

    public:
        Stack(){
            list = new LinkedList();
        }

        ~Stack(){
            delete list;
        }

        bool IsEmpty(){
            return list->IsEmpty();
        }

        void Push(int item){
            list->Insert(item);
        }

        int Pop(){
            if (list->IsEmpty()) {
                throw std::runtime_error("Stack is empty");
            }
            Node<int>* head = list->GetHead();
            int item = head->GetData();
            list->Delete(item);
            return item;
        }

        void Display(){
            Node<int>* current = list->GetHead();
            if (current == nullptr) {
                std::cout << "The stack is empty" << std::endl;
                return;
            }
            std::cout << "The stack contains:" << std::endl;
            while (current->GetNext() != nullptr) {
                std::cout << "|" << current->GetData() << "|" << std::endl;
                current = current->GetNext();
            }
            std::cout << "|" << current->GetData() << "|" << std::endl;
        }
};