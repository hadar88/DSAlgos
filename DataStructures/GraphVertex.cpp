class GraphVertex{
    private:
        const int data;
        LinkedList* neighbors;
        
    public:
        GraphVertex(int value): data(value) {
            neighbors = new LinkedList();
        }

        ~GraphVertex(){
            delete neighbors;
        }

        int GetData(){
            return data;
        }

        LinkedList* GetNeighbors(){
            return neighbors;
        }

        void AddNeighbor(int value){
            neighbors->InsertLast(value);
        }

        void DeleteNeighbor(int value){
            neighbors->Delete(value);
        }

        bool HasNeighbor(int value){
            Node<int>* current = neighbors->GetHead();
            while(current != nullptr){
                if(current->GetData() == value)
                    return true;
                current = current->GetNext();
            }
            return false;
        }
    };