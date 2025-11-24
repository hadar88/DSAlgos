

class GraphVertex{
    private:
        const int data;
        LinkedList* neighbors;

        string color_BFS;
        int distance_BFS;
        GraphVertex* parent_BFS;

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

        // BFS attributes
        string GetColor_BFS(){
            return color_BFS;
        }

        int GetDistance_BFS(){
            return distance_BFS;
        }

        GraphVertex* GetParent_BFS(){
            return parent_BFS;
        }

        void SetColor_BFS(string color){
            color_BFS = color;
        }

        void SetDistance_BFS(int distance){
            distance_BFS = distance;
        }

        void SetParent_BFS(GraphVertex* parent){
            parent_BFS = parent;
        }

    };