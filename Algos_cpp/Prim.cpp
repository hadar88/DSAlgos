int findKeyByValue(const std::map<int, double>& m, double value) {
    for (const auto& pair : m) {
        if (pair.second == value)
            return pair.first;
    }
    return -1;
}

Graph* PrimMST(Graph* g){
    if(g->GetSize() == 0)
        return new Graph(false);

    if(g->IsDirected())
        throw std::invalid_argument("Graph is directed");

    if(!g->IsConnected())
        throw std::invalid_argument("Graph is not connected");

    Graph* A = new Graph(false);

    std::map<int, double> keys;
    std::map<int, int> parents;

    LinkedList* vertices = g->GetVertices();
    Node<int>* current = vertices->GetHead();
    while(current){
        int data = current->GetData();
        A->CreateVertex(data);
        keys[data] = INT_MAX;
        parents[data] = INT_MIN;
        current = current->GetNext();
    }
    
    keys[vertices->GetHead()->GetData()] = 0;
    
    PriorityQueue* pq = new PriorityQueue(false);
    for(auto pair : keys){
        pq->Insert(pair.second);
    }
    
    while(pq->GetSize() != 0){
        double u_key = pq->ExtractTop();
        int u = findKeyByValue(keys, u_key);
        keys.erase(u);

        LinkedList* neighbors = g->GetNeighbors(u);
        Node<int>* current = neighbors->GetHead();
        
        while(current){
            int v = current->GetData();
            
            double edge_weight = g->EdgeWeight(u, v);  
            if(pq->IndexOf(keys[v]) != -1 && edge_weight < keys[v]){
                parents[v] = u;
                pq->UpdateKey(pq->IndexOf(keys[v]), edge_weight);
                keys[v] = edge_weight;
            }
            
            current = current->GetNext();
        }

        delete neighbors;
    }    

    for(auto pair: parents){
        if(pair.second != INT_MIN)
            A->CreateEdge(pair.second, pair.first, g->EdgeWeight(pair.first, pair.second));
    }

    delete pq;
    delete vertices;

    return A;
}