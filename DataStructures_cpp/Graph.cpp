class Graph{
    private:
        std::vector<GraphVertex*> graph;
        int size;
        bool directed;

        bool IsExistVertex(int value){
            for(GraphVertex* v : graph){
                if(v->GetData() == value)
                    return true;
            }
            return false;
        }

        bool IsExistEdge(int v, int u){
            if(!IsExistVertex(v) || !IsExistVertex(u))
                return false;
            
            for(GraphVertex* q : graph){
                if(q->GetData() == v && q->HasNeighbor(u))
                    return true;
            }
            return false;
        }

        int FindVertexIndex(int value){
            for(int i = 0; i < size; i++){
                if(graph[i]->GetData() == value)
                    return i;
            }
            return -1;
        }

        GraphVertex* GetVertex(int value){
            for(GraphVertex* q : graph)
                if(q->GetData() == value)
                    return q;
            return nullptr;
        }

        void BFS(int s){
            for(GraphVertex* v : graph){
                if(v->GetData() == s){
                    v->SetColor_BFS("gray");
                    v->SetDistance_BFS(0);
                }
                else{
                    v->SetColor_BFS("white");
                    v->SetDistance_BFS(INT_MAX);
                }
                v->SetParent_BFS(nullptr);
            }
            
            Queue* Q = new Queue();
            Q->Enqueue(s);

            while(!Q->IsEmpty()){
                int u = Q->Dequeue();
                GraphVertex* u_vertex = GetVertex(u);

                Node<int>* v = GetNeighbors(u)->GetHead(); 
                while(v != nullptr){
                    GraphVertex* v_vertex = GetVertex(v->GetData());
                    if(v_vertex->GetColor_BFS() == "white"){
                        v_vertex->SetColor_BFS("gray");
                        v_vertex->SetDistance_BFS(u_vertex->GetDistance_BFS() + 1);
                        v_vertex->SetParent_BFS(u_vertex);
                        Q->Enqueue(v->GetData());
                    }
                    v = v->GetNext();
                }

                u_vertex->SetColor_BFS("black");
            }
            delete Q;
        }

        std::vector<Edge*> GetEdges(){
            std::vector<Edge*> edges;

            for(GraphVertex* q : graph){
                Node<int>* current = GetNeighbors(q->GetData())->GetHead();
                while(current != nullptr){
                    Edge* e = new Edge(q->GetData(), current->GetData());
                    if(directed){
                        edges.push_back(e);
                    }
                    else{
                        bool toAdd = true;
                        for(Edge* temp : edges){
                            if(temp->getV() == e->getU() && temp->getU() == e->getV()){
                                toAdd = false;
                                break;
                            }
                        }
                        if(toAdd)
                            edges.push_back(e);
                    }
                    current = current->GetNext();
                }
            }

            return edges;
        }

    public:
        Graph(bool directed = true): graph(), size(0), directed(directed) {}

        ~Graph(){
            for(GraphVertex* v : graph)
                delete v;
        }

        bool IsDirected(){
            return directed;
        }

        int GetSize(){
            return size;
        }

        void CreateVertex(int value){
            if(IsExistVertex(value)){
                std::cout << "Vertex " << value << " already exists" << std::endl;
                return;
            }

            GraphVertex* new_vertex = new GraphVertex(value);
            graph.push_back(new_vertex);
            size++;
        }

        void DeleteVertex(int value){
            if(!IsExistVertex(value)){
                std::cout << "Cannot delete vertex " << value << " : Vertex does not exist" << std::endl;
                return;
            }

            for(GraphVertex* v : graph){
                if(v->GetData() != value && v->HasNeighbor(value))
                    v->DeleteNeighbor(value);
            }

            int index = FindVertexIndex(value);
            delete graph[index];
            graph.erase(graph.begin() + index);
            size--;
        }

        void AddEdge(int v, int u){
            if(!IsExistVertex(v) || !IsExistVertex(u)){
                std::cout << "Cannot add edge (" << v << "," << u << ") : One or both vertices do not exist" << std::endl;
                return;
            }
            if(IsExistEdge(v, u)){
                std::cout << "Edge" << " (" << v << "," << u << ") " <<"already exists" << std::endl;
                return;
            }

            for(GraphVertex* q : graph){
                if(q->GetData() == v)
                    q->AddNeighbor(u);
                if(!directed)
                    if(q->GetData() == u)
                        q->AddNeighbor(v);
            }
        }

        void DeleteEdge(int v, int u){
            if(!IsExistVertex(v) || !IsExistVertex(u)){
                std::cout << "Cannot delete edge (" << v << "," << u << ") : One or both vertices do not exist" << std::endl;
                return;
            }
            if(!IsExistEdge(v, u)){
                std::cout << "Cannot delete edge (" << v << "," << u << ") : Edge does not exist" << std::endl;
                return;
            }

            for(GraphVertex* q : graph){
                if(q->GetData() == v)
                    q->DeleteNeighbor(u);
                if(!directed)
                    if(q->GetData() == u)
                        q->DeleteNeighbor(v);
            }
        }

        LinkedList* GetNeighbors(int value){
            if(!IsExistVertex(value)){
                throw std::invalid_argument("Vertex does not exist");
            }

            for(GraphVertex* q : graph){
                if(q->GetData() == value)
                    return q->GetNeighbors();
            }
            return nullptr;
        }

        LinkedList* GetVertices(){
            if(size == 0)
                throw std::runtime_error("Graph is empty");

            LinkedList* vertices = new LinkedList();
            for(GraphVertex* q : graph){
                vertices->InsertLast(q->GetData());
            }
            return vertices;
        }

        void DisplayEdges(){
            if(size == 0){
                std::cout << "Graph is empty" << std::endl;
                return;
            }
            std::cout << "Edges List:" << std::endl;
            std::vector<Edge*> edges = GetEdges();
            for(Edge* e : edges)
                e->Display();
        }

        void Display(){
            if(size == 0){
                std::cout << "Graph is empty" << std::endl;
                return;
            }
            std::cout << "Graph is " << (directed ? "directed" : "undirected") << " with " << size << " vertices." << std::endl;
            std::cout << "Neighbors List:" << std::endl;
            for(GraphVertex* v : graph){
                std::cout << v->GetData() << "-> ";
                if(v->GetNeighbors()->IsEmpty()){
                    std::cout << "No neighbors" << std::endl;
                    continue;
                }
                Node<int>* current = v->GetNeighbors()->GetHead();
                while(current->GetNext() != nullptr){
                    std::cout << current->GetData() << ", ";
                    current = current->GetNext();
                }
                std::cout << current->GetData();
                std::cout << std::endl;
            }
        }

        void PrintPath(int s, int v){
            if(!IsExistVertex(s) || !IsExistVertex(v)){
                std::cout << "One or both vertices do not exist" << std::endl;
                return;
            }
            
            BFS(s);
            
            LinkedList* l = new LinkedList();

            GraphVertex* v_vertex = GetVertex(v);
            while(v_vertex != nullptr){
                l->Insert(v_vertex->GetData());

                v_vertex = v_vertex->GetParent_BFS();
            }

            Node<int>* current = l->GetHead();
            if(current->GetData() == s){
                while(current != nullptr){
                    if(current->GetNext() != nullptr)
                        std::cout << current->GetData() << " -> ";
                    else
                        std::cout << current->GetData();
                    current = current->GetNext();
                }
                std::cout << std::endl;
            }
            else
                std::cout << "No path from " << s << " to " << v << " exists" << std::endl;
        }

        int Distance(int s, int t){
            if(!IsExistVertex(s) || !IsExistVertex(t)){
                throw std::invalid_argument("One or both vertices do not exist");
            }

            BFS(s);

            GraphVertex* t_vertex = GetVertex(t);
            return t_vertex->GetDistance_BFS();
        }

        LinkedList* GetReachableVertices(int s){
            if(!IsExistVertex(s)){
                throw std::invalid_argument("Vertex does not exist");
            }

            BFS(s);

            LinkedList* l = new LinkedList();

            for(GraphVertex* v : graph)
                if(v->GetDistance_BFS() != INT_MAX && v->GetData() != s)
                    l->InsertLast(v->GetData());
            
            return l;
        }

        void Clear(){
            graph.clear();
            size = 0;
        }
};