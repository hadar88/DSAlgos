class LinkedList{
    private:
        Node<int>* head;

    public:
        LinkedList(): head(nullptr) {}

        ~LinkedList(){
            while(head != nullptr){
                Node<int>* temp = head;
                head = head->GetNext();
                delete temp;
            }
        }

        Node<int>* GetHead(){
            return head;
        }

        void Insert(int item){
            Node<int>* newNode = new Node<int>(item);
            if (head == nullptr)
                head = newNode;
            else{
                newNode->SetNext(head);
                head = newNode;
            }
        }

        void InsertLast(int item){
            Node<int>* newNode = new Node<int>(item);
            if(head == nullptr){
                head = newNode;
            }
            else{
                Node<int>* current = head;
                while(current->GetNext() != nullptr){
                    current = current->GetNext();
                }
                current->SetNext(newNode);
            }
        }

        void Delete(int item){
            if(head == nullptr) 
                return;
            if(head->GetData() == item){
                Node<int>* toDelete = head;
                head = head->GetNext();
                delete toDelete;
            }
            else{
                Node<int>* current = head;
                while(current != nullptr && current->GetNext() != nullptr){
                    if(current->GetNext()->GetData() == item){
                        Node<int>* toDelete = current->GetNext();
                        current->SetNext(toDelete->GetNext());
                        delete toDelete;
                        break;
                    }
                    current = current->GetNext();
                }
            }
        }

        bool IsEmpty(){
            return head == nullptr;
        }

        void Display(){
            if (head == nullptr) {
                std::cout << "LinkedList is empty" << std::endl;
                return;
            }
            Node<int>* current = head;
            while (current->GetNext() != nullptr) {
                std::cout << "[" << current->GetData() << "] -> ";
                current = current->GetNext();
            }
            std::cout << "[" << current->GetData() << "]" << std::endl;
        }
};