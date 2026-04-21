void Merge(std::vector<Edge*>& A, int left, int mid, int right){
    int n1 = mid - left + 1;
    int n2 = right - mid;

    std::vector<Edge*> L(n1);
    std::vector<Edge*> R(n2);

    for(int i = 0; i < n1; i++)
        L[i] = A[left + i];
    for(int j = 0; j < n2; j++)
        R[j] = A[mid + j + 1];
        
    int i = 0;
    int j = 0;
    int k = left;

    while (i < n1 && j < n2) {
        if (L[i]->GetWeight() <= R[j]->GetWeight()) {
            A[k] = L[i];
            i++;
        } else {
            A[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        A[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        A[k] = R[j];
        j++;
        k++;
    }
}

void MergeSort(std::vector<Edge*>& A, int left, int right){
    if(left < right){
        int mid = (left + right) / 2;
        MergeSort(A, left, mid);
        MergeSort(A, mid + 1, right);
        Merge(A, left, mid, right);
    }
}

Graph* KruskalMST(Graph* g){
    if(g->GetSize() == 0)
        return new Graph(false);
    
    if(!g->IsConnected())
        throw std::invalid_argument("Graph is not connected");

    Graph* A = new Graph(false);
    DisjointSets* ds = new DisjointSets();

    LinkedList* vertices = g->GetVertices();
    Node<int>* head = vertices->GetHead();
    while(head != nullptr){
        A->CreateVertex(head->GetData());
        ds->MakeSet(head->GetData());
        head = head->GetNext();
    }

    std::vector<Edge*> edges = g->GetEdges();

    if (!edges.empty())
        MergeSort(edges, 0, edges.size() - 1);

    for(Edge* e : edges){
        if(ds->FindSet(e->GetV())->GetData() != ds->FindSet(e->GetU())->GetData()){
            A->CreateEdge(e->GetV(), e->GetU(), e->GetWeight());
            ds->Union(e->GetV(), e->GetU());
        }
    }

    delete vertices;
    delete ds;
    
    return A;
}