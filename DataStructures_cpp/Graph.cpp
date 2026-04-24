class Graph{
    private:
        std::vector<GraphVertex*> vertices;
        std::vector<Edge*> edges;
        int size;
        bool directed;

        bool IsExistVertex(int value){
            for(GraphVertex* v : vertices){
                if(v->GetData() == value)
                    return true;
            }
            return false;
        }

        bool IsExistEdge(int v, int u){
            if(!IsExistVertex(v) || !IsExistVertex(u))
                return false;
            
            for(GraphVertex* q : vertices){
                if(q->GetData() == v && q->HasNeighbor(u))
                    return true;
            }
            return false;
        }

        int FindVertexIndex(int value){
            for(int i = 0; i < size; i++){
                if(vertices[i]->GetData() == value)
                    return i;
            }
            return -1;
        }

        int FindEdgeIndex(int v, int u){
            for(int i = 0; i < edges.size(); i++){
                if(edges[i]->GetV() == v && edges[i]->GetU() == u)
                    return i;
                else if(!directed)
                    if((edges[i]->GetV() == v && edges[i]->GetU() == u) || (edges[i]->GetV() == u && edges[i]->GetU() == v))
                        return i;
            }
            return -1;
        }

        GraphVertex* GetVertex(int value){
            for(GraphVertex* q : vertices)
                if(q->GetData() == value)
                    return q;
            return nullptr;
        }

    public:
        Graph(bool directed = true): vertices(), edges(), size(0), directed(directed) {}

        ~Graph(){
            for(GraphVertex* v : vertices)
                delete v;
            for(Edge* e : edges)
                delete e;
        }

        bool IsDirected(){
            return directed;
        }

        int GetSize(){
            return size;
        }

        void CreateVertex(int value){
            if(IsExistVertex(value)){
                std::cerr << "Error: Vertex " << value << " already exists" << std::endl;
                return;
            }

            GraphVertex* new_vertex = new GraphVertex(value);
            vertices.push_back(new_vertex);
            size++;
        }

        void DeleteVertex(int value){
            if(!IsExistVertex(value)){
                std::cerr << "Error: Cannot delete vertex " << value << " : Vertex does not exist" << std::endl;
                return;
            }

            for(GraphVertex* v : vertices){
                if(v->HasNeighbor(value))
                    v->DeleteNeighbor(value);
            }

            for(int i = 0; i < edges.size();){
                if(edges[i]->GetV() == value || edges[i]->GetU() == value){
                    delete edges[i];
                    edges.erase(edges.begin() + i);
                }
                else
                    i++;
            }

            int index = FindVertexIndex(value);
            delete vertices[index];
            vertices.erase(vertices.begin() + index);
            size--;
        }

        void CreateEdge(int v, int u){
            if(v == u){
                std::cerr << "Error: Can't create an edge from a vertex to itself" << std::endl;
                return;
            }

            if(!IsExistVertex(v) || !IsExistVertex(u)){
                std::cerr << "Error: Cannot add edge (" + std::to_string(v) + "," + std::to_string(u) + ") : One or both vertices do not exist" << std::endl;
                return;
            }

            if(IsExistEdge(v, u)){
                std::cerr << "Error: Edge (" + std::to_string(v) + ", " + std::to_string(u) + ") already exists" << std::endl;
                return;
            }

            for(GraphVertex* q : vertices){
                if(q->GetData() == v)
                    q->AddNeighbor(u);
                if(!directed)
                    if(q->GetData() == u)
                        q->AddNeighbor(v);
            }

            Edge* new_edge = new Edge(v, u, directed);
            edges.push_back(new_edge);
        }

        void CreateEdge(int v, int u, double weight){
            if(v == u){
                std::cerr << "Error: Can't create edge from a vertex to itself" << std::endl;
                return;
            }

            if(!IsExistVertex(v) || !IsExistVertex(u)){
                std::cerr << "Error: Cannot add edge (" + std::to_string(v) + "," + std::to_string(u) + ") : One or both vertices do not exist" << std::endl;
                return;
            }

            if(IsExistEdge(v, u)){
                std::cerr << "Error: Edge (" + std::to_string(v) + ", " + std::to_string(u) + ") already exists" << std::endl;
                return;
            }

            for(GraphVertex* q : vertices){
                if(q->GetData() == v)
                    q->AddNeighbor(u);
                if(!directed)
                    if(q->GetData() == u)
                        q->AddNeighbor(v);
            }

            Edge* new_edge = new Edge(v, u, weight, directed);
            edges.push_back(new_edge);
        }

        void DeleteEdge(int v, int u){
            if(!IsExistVertex(v) || !IsExistVertex(u)){
                std::cerr << "Error: Cannot delete edge (" + std::to_string(v) + "," + std::to_string(u) + ") : One or both vertices do not exist" << std::endl;
                return;
            }
            
            if(!IsExistEdge(v, u)){
                std::cerr << "Error: Cannot delete edge (" + std::to_string(v) + "," + std::to_string(u) + ") : Edge does not exist" << std::endl;
                return;
            }

            for(GraphVertex* q : vertices){
                if(q->GetData() == v)
                    q->DeleteNeighbor(u);
                if(!directed)
                    if(q->GetData() == u)
                        q->DeleteNeighbor(v);
            }

            for(auto it = edges.begin(); it != edges.end(); ++it){
                Edge* e = *it;
                if(e->GetV() == v && e->GetU() == u){
                    delete e;
                    edges.erase(it);
                    break;
                }
                else if(!directed && e->GetV() == u && e->GetU() == v){
                    delete e;
                    edges.erase(it);
                    break;
                }
            }
        }

        LinkedList* GetNeighbors(int value){
            if(!IsExistVertex(value))
                throw std::runtime_error("Vertex does not exist");

            for(GraphVertex* q : vertices){
                if(q->GetData() == value){
                    LinkedList* copy = new LinkedList();
                    LinkedList* neighbors = q->GetNeighbors();
                    Node<int>* current = neighbors->GetHead();
                    while(current){
                        copy->Insert(current->GetData());
                        current = current->GetNext();
                    }
                    return copy;
                }
            }
            return nullptr;
        }

        LinkedList* GetVertices(){
            LinkedList* vertices = new LinkedList();
            if(size == 0)
                return vertices;

            for(GraphVertex* q : this->vertices){
                vertices->InsertLast(q->GetData());
            }
            return vertices;
        }

        std::vector<Edge*> GetEdges(){
            return edges;
        }

        void DisplayEdges(){
            if(size == 0){
                std::cout << "Graph is empty" << std::endl;
                return;
            }

            std::cout << "Edges List:" << std::endl;
            for(Edge* e : edges){
                e->Display();
            }
        }

        void Display(){
            if(size == 0){
                std::cout << "Graph is empty" << std::endl;
                return;
            }

            std::cout << "Graph is " << (directed ? "directed" : "undirected") << " with " << size << " vertices." << std::endl;
            std::cout << "Neighbors List:" << std::endl;
            for(GraphVertex* v : vertices){
                std::cout << v->GetData() << " -> ";
                if(v->GetNeighbors()->IsEmpty()){
                    std::cout << "No neighbors" << std::endl;
                    continue;
                }

                LinkedList* neighbors = v->GetNeighbors();
                Node<int>* current = neighbors->GetHead();
                while(current->GetNext() != nullptr){
                    std::cout << current->GetData() << ", ";
                    current = current->GetNext();
                }

                std::cout << current->GetData();
                std::cout << std::endl;
            }
        }

        std::tuple<std::map<int, std::string>, std::map<int, int>, std::map<int, GraphVertex*>> BFS(int s){
            if(!IsExistVertex(s)){
                throw std::invalid_argument("Vertex " + std::to_string(s) + " does not exist");
            }
            
            std::map<int, std::string> colors;
            std::map<int, int> distances;
            std::map<int, GraphVertex*> parents;
            
            for(GraphVertex* v : vertices){
                if(v->GetData() == s){
                    colors[v->GetData()] = "gray";
                    distances[v->GetData()] = 0;
                }
                else{
                    colors[v->GetData()] = "white";
                    distances[v->GetData()] = INT_MAX;
                }
                parents[v->GetData()] = nullptr;
            }
            
            Queue* Q = new Queue();
            Q->Enqueue(s);

            while(!Q->IsEmpty()){
                int u = Q->Dequeue();
                GraphVertex* u_vertex = GetVertex(u);

                Node<int>* v = u_vertex->GetNeighbors()->GetHead(); 
                while(v != nullptr){
                    GraphVertex* v_vertex = GetVertex(v->GetData());
                    if(colors[v->GetData()] == "white"){
                        colors[v_vertex->GetData()] = "gray";
                        distances[v_vertex->GetData()] = distances[u] + 1;
                        parents[v_vertex->GetData()] = u_vertex;
                        Q->Enqueue(v->GetData());
                    }
                    v = v->GetNext();
                }

                colors[u] = "black";
            }

            delete Q;
            
            return {colors, distances, parents};
        }

        LinkedList* GetPath(int s, int v){
            if(!IsExistVertex(s) || !IsExistVertex(v)){
                throw std::invalid_argument("Vertex " + std::to_string(s) + " or " + std::to_string(v) + " does not exist");
            }
            
            if(s == v){
                LinkedList* l = new LinkedList();
                l->Insert(s);
                return l;
            }
            
            auto [colors, distances, parents] = BFS(s);

            LinkedList* l = new LinkedList();

            GraphVertex* v_vertex = GetVertex(v);
            while(v_vertex != nullptr){
                l->Insert(v_vertex->GetData());
                v_vertex = parents[v_vertex->GetData()];
            }

            if(l->GetHead()->GetData() == s){
                return l;
            }
            else{
                delete l;
                throw std::runtime_error("No path from " + std::to_string(s) + " to " + std::to_string(v) + " exists");
            }
        }

        int Distance(int s, int t){
            if(!IsExistVertex(s) || !IsExistVertex(t))
                throw std::invalid_argument("One or both vertices do not exist");

            auto [colors, distances, parents] = BFS(s);

            GraphVertex* t_vertex = GetVertex(t);
            return distances[t_vertex->GetData()];
        }

        LinkedList* GetReachableVertices(int s){
            if(!IsExistVertex(s))
                throw std::invalid_argument("Vertex does not exist");

            auto [colors, distances, parents] = BFS(s);

            LinkedList* l = new LinkedList();

            for(GraphVertex* v : vertices)
                if(distances[v->GetData()] != INT_MAX && v->GetData() != s)
                    l->InsertLast(v->GetData());
            
            return l;
        }

        bool IsConnected(){
            if(size <= 1)
                return true;

            GraphVertex* v = vertices[0];
            LinkedList* l = GetReachableVertices(v->GetData());
            bool connected = l->Size() == size - 1;
            delete l;

            if(!connected)
                return false;

            if(directed){
                Graph* transposed = GetTransposed();
                LinkedList* l_rev = transposed->GetReachableVertices(v->GetData());
                bool stronglyConnected = l_rev->Size() == size - 1;
                delete l_rev;
                delete transposed;
                return stronglyConnected;
            }

            return true;
        }

        Graph* GetTransposed(){
            Graph* transposed = new Graph(directed);
            for(GraphVertex* v : vertices)
                transposed->CreateVertex(v->GetData());
            
            for(Edge* e : edges)
                transposed->CreateEdge(e->GetU(), e->GetV(), e->GetWeight());
            
            return transposed;
        }

        double EdgeWeight(int v, int u){
            if(!IsExistEdge(v, u))
                throw std::invalid_argument("Edge (" + std::to_string(v) + " -> " + std::to_string(u) + ") does not exist");

            for(Edge* e : edges){
                if(directed){
                    if(e->GetV() == v && e->GetU() == u)
                        return e->GetWeight();
                }
                else
                    if((e->GetV() == v && e->GetU() == u) || (e->GetV() == u && e->GetU() == v))
                        return e->GetWeight();
            }
            return 0;
        }

        double GraphWeight(){
            if(edges.size() == 0)
                return 0.0;

            double weight = 0.0;
            for(Edge* e : edges)
                weight += e->GetWeight();

            return weight;
        }

        void Clear(){
            for(GraphVertex* v : vertices)
                delete v;
            for(Edge* e : edges)
                delete e;

            vertices.clear();
            edges.clear();

            size = 0;
        }
};