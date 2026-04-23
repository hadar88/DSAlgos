#include "dataStructures.h"

extern "C" {
    // Node
    Node<int>* Create_node(int value){
        return new Node<int>(value);
    }

    void Destroy_node(Node<int>* node){
        delete node;
    }

    int GetData_node(Node<int>* node){
        if (node == nullptr) {
            return INT_MIN;
        }
        return node->GetData();
    }

    Node<int>* GetNext_node(Node<int>* node){
        return node->GetNext();
    }

    void SetData_node(Node<int>* node, int value){
        node->SetData(value);
    }

    void SetNext_node(Node<int>* node, Node<int>* next){
        node->SetNext(next);
    }

    // TreeNode
    TreeNode<int>* Create_treenode(int value){
        return new TreeNode<int>(value);
    }

    void Destroy_treenode(TreeNode<int>* node){
        delete node;
    }

    int GetData_treenode(TreeNode<int>* node){
        if (node == nullptr) {
            return INT_MIN;
        }
        return node->GetData();
    }

    TreeNode<int>* GetRight_treenode(TreeNode<int>* node){
        if (node == nullptr) {
            return nullptr;
        }
        return node->GetRight();
    }

    TreeNode<int>* GetLeft_treenode(TreeNode<int>* node){
        if (node == nullptr) {
            return nullptr;
        }
        return node->GetLeft();
    }

    TreeNode<int>* GetParent_treenode(TreeNode<int>* node){
        if (node == nullptr) {
            return nullptr;
        }
        return node->GetParent();
    }

    void SetData_treenode(TreeNode<int>* node, int value){
        node->SetData(value);
    }

    void SetRight_treenode(TreeNode<int>* node, TreeNode<int>* right){
        node->SetRight(right);
    }

    void SetLeft_treenode(TreeNode<int>* node, TreeNode<int>* left){
        node->SetLeft(left);
    }

    void SetParent_treenode(TreeNode<int>* node, TreeNode<int>* parent){
        node->SetParent(parent);
    }

    // LinkedList
    LinkedList* Create_linkedlist(){
        return new LinkedList();
    }

    void Destroy_linkedlist(LinkedList* list){
        delete list;
    }

    Node<int>* GetHead_linkedlist(LinkedList* list){
        return list->GetHead();
    }

    void Insert_linkedlist(LinkedList* list, int value){
        list->Insert(value);
    }

    void InsertLast_linkedlist(LinkedList* list, int value){
        list->InsertLast(value);
    }

    void Delete_linkedlist(LinkedList* list, int value){
        list->Delete(value);
    }

    bool IsEmpty_linkedlist(LinkedList* list){
        return list->IsEmpty();
    }

    int Size_linkedlist(LinkedList* list){
        return list->Size();
    }

    void Display_linkedlist(LinkedList* list){
        list->Display();
    }

    // Stack
    Stack* Create_stack(){
        return new Stack();
    }

    void Destroy_stack(Stack* stack){
        delete stack;
    }

    bool IsEmpty_stack(Stack* stack){
        return stack->IsEmpty();
    }

    void Push_stack(Stack* stack, int value){
        stack->Push(value);
    }

    int Pop_stack(Stack* stack){
        try {
            return stack->Pop();
        } catch (const std::runtime_error& e) {
            std::cerr << "Error: " << e.what() << std::endl;
            return -1;
        }
    }

    void Display_stack(Stack* stack){
        stack->Display();
    }

    // Queue
    Queue* Create_queue(){
        return new Queue();
    }

    void Destroy_queue(Queue* queue){
        delete queue;
    }

    bool IsEmpty_queue(Queue* queue){
        return queue->IsEmpty();
    }

    void Enqueue_queue(Queue* queue, int value){
        queue->Enqueue(value);
    }

    int Dequeue_queue(Queue* queue){
        try{
            return queue->Dequeue();
        } catch (const std::runtime_error& e) {
            std::cerr << "Error: " << e.what() << std::endl;
            return INT_MIN;
        }
    }

    void Display_queue(Queue* queue){
        queue->Display();
    }

    // BinarySearchTree
    BinarySearchTree* Create_BinarySearchTree(){
        return new BinarySearchTree();
    }

    void Destroy_BinarySearchTree(BinarySearchTree* tree){
        delete tree;
    }

    bool IsEmpty_BinarySearchTree(BinarySearchTree* tree){
        return tree->IsEmpty();
    }

    int Size_BinarySearchTree(BinarySearchTree* tree){
        return tree->Size();
    }

    TreeNode<int>* GetRoot_BinarySearchTree(BinarySearchTree* tree){
        return tree->GetRoot();
    }

    bool Exists_BinarySearchTree(BinarySearchTree* tree, int key){
        return tree->Exists(key);
    }

    TreeNode<int>* Search_BinarySearchTree(BinarySearchTree* tree, int key){
        try {
            return tree->Search(key);
        } catch (const std::runtime_error& e) {
            std::cerr << "Error: " << e.what() << std::endl;
            return nullptr;
        }
    }

    int Minimum_BinarySearchTree(BinarySearchTree* tree){
        try {
            return tree->Minimum();
        } catch (const std::runtime_error& e) {
            std::cerr << "Error: " << e.what() << std::endl;
            return INT_MIN;
        }
    }

    int Maximum_BinarySearchTree(BinarySearchTree* tree){
        try {
            return tree->Maximum();
        } catch (const std::runtime_error& e) {
            std::cerr << "Error: " << e.what() << std::endl;
            return INT_MAX;
        }
    }

    TreeNode<int>* Successor_BinarySearchTree(BinarySearchTree* tree, int key){
        try {
            return tree->Successor(key);
        } catch (const std::runtime_error& e) {
            std::cerr << "Error: " << e.what() << std::endl;
            return nullptr;
        }
    }

    void Insert_BinarySearchTree(BinarySearchTree* tree, int key){
        tree->Insert(key);
    }

    void Delete_BinarySearchTree(BinarySearchTree* tree, int key){
        tree->Delete(key);
    }

    int Depth_BinarySearchTree(BinarySearchTree* tree, int key){
        try {
            return tree->Depth(key);
        } catch (const std::runtime_error& e) {
            std::cerr << "Error: " << e.what() << std::endl;
            return -1;
        }
    }

    int Height_BinarySearchTree(BinarySearchTree* tree, int key){
        try {
            return tree->Height(key);
        } catch (const std::runtime_error& e) {
            std::cerr << "Error: " << e.what() << std::endl;
            return -1;
        }
    }

    void InOrder_BinarySearchTree(BinarySearchTree* tree){
        if (tree->IsEmpty()) return;
        tree->InOrder(tree->GetRoot());
    }

    void PreOrder_BinarySearchTree(BinarySearchTree* tree){
        if (tree->IsEmpty()) return;
        tree->PreOrder(tree->GetRoot());
    }

    void PostOrder_BinarySearchTree(BinarySearchTree* tree){
        if (tree->IsEmpty()) return;
        tree->PostOrder(tree->GetRoot());
    }

    // AVLTree
    AVLTree* Create_AVLTree(){
        return new AVLTree();
    }

    void Destroy_AVLTree(AVLTree* tree){
        delete tree;
    }

    bool IsEmpty_AVLTree(AVLTree* tree){
        return tree->IsEmpty();
    }

    int Size_AVLTree(AVLTree* tree){
        return tree->Size();
    }

    TreeNode<int>* GetRoot_AVLTree(AVLTree* tree){
        return tree->GetRoot();
    }

    bool Exists_AVLTree(AVLTree* tree, int key){
        return tree->Exists(key);
    }

    TreeNode<int>* Search_AVLTree(AVLTree* tree, int key){
        try {
            return tree->Search(key);
        } catch (const std::runtime_error& e) {
            std::cerr << "Error: " << e.what() << std::endl;
            return nullptr;
        }
    }

    int Minimum_AVLTree(AVLTree* tree){
        try {
            return tree->Minimum();
        } catch (const std::runtime_error& e) {
            std::cerr << "Error: " << e.what() << std::endl;
            return INT_MIN;
        }
    }

    int Maximum_AVLTree(AVLTree* tree){
        try {
            return tree->Maximum();
        } catch (const std::runtime_error& e) {
            std::cerr << "Error: " << e.what() << std::endl;
            return INT_MAX;
        }
    }

    TreeNode<int>* Successor_AVLTree(AVLTree* tree, int key){
        try {
            return tree->Successor(key);
        } catch (const std::runtime_error& e) {
            std::cerr << "Error: " << e.what() << std::endl;
            return nullptr;
        }
    }

    void Insert_AVLTree(AVLTree* tree, int key){
        tree->Insert(key);
    }

    void Delete_AVLTree(AVLTree* tree, int key){
        tree->Delete(key);
    }

    int Depth_AVLTree(AVLTree* tree, int key){
        try {
            return tree->Depth(key);
        } catch (const std::runtime_error& e) {
            std::cerr << "Error: " << e.what() << std::endl;
            return -1;
        }
    }

    int Height_AVLTree(AVLTree* tree, int key){
        try {
            return tree->Height(key);
        } catch (const std::runtime_error& e) {
            std::cerr << "Error: " << e.what() << std::endl;
            return -1;
        }
    }

    void InOrder_AVLTree(AVLTree* tree){
        if (tree->IsEmpty()) return;
        tree->InOrder(tree->GetRoot());
    }

    void PreOrder_AVLTree(AVLTree* tree){
        if (tree->IsEmpty()) return;
        tree->PreOrder(tree->GetRoot());
    }

    void PostOrder_AVLTree(AVLTree* tree){
        if (tree->IsEmpty()) return;
        tree->PostOrder(tree->GetRoot());
    }

    // SkipListNode
    SkipListNode* Create_SkipListNode(int value, int h){
        return new SkipListNode(value, h);
    }

    void Destroy_SkipListNode(SkipListNode* node){
        delete node;
    }

    int GetData_SkipListNode(SkipListNode* node){
        if(node == nullptr) return INT_MIN;
        return node->GetData();
    }

    int GetHeight_SkipListNode(SkipListNode* node){
        if(node == nullptr) return -1;
        return node->GetHeight();
    }

    SkipListNode* GetNext_SkipListNode(SkipListNode* node, int level){
        try {
            return node->GetNext(level);
        } catch (const std::out_of_range& e) {
            std::cerr << "Error: " << e.what() << std::endl;
            return nullptr;
        }
    }

    SkipListNode* GetPrev_SkipListNode(SkipListNode* node, int level){
        try {
            return node->GetPrev(level);
        } catch (const std::out_of_range& e) {
            std::cerr << "Error: " << e.what() << std::endl;
            return nullptr;
        }
    }

    void SetData_SkipListNode(SkipListNode* node, int data){
        node->SetData(data);
    }

    void SetHeight_SkipListNode(SkipListNode* node, int height){
        node->SetHeight(height);
    }

    void SetNext_SkipListNode(SkipListNode* node, int level, SkipListNode* next){
        node->SetNext(level, next);
    }

    void SetPrev_SkipListNode(SkipListNode* node, int level, SkipListNode* prev){
        node->SetPrev(level, prev);
    }

    // SkipList
    SkipList* Create_SkipList(){
        return new SkipList();
    }

    void Destroy_SkipList(SkipList* skipList){
        delete skipList;
    }

    bool IsEmpty_SkipList(SkipList* skipList){
        return skipList->IsEmpty();
    }

    SkipListNode* GetHead_SkipList(SkipList* skipList){
        return skipList->GetHead();
    }

    int GetHeight_SkipList(SkipList* skipList){
        return skipList->GetHeight();
    }

    SkipListNode* Search_SkipList(SkipList* skipList, int key){
        return skipList->Search(key);
    }

    void Insert_SkipList(SkipList* skipList, int key){
        skipList->Insert(key);
    }

    void Delete_SkipList(SkipList* skipList, int key){
        skipList->Delete(key);
    }

    void Display_SkipList(SkipList* skipList){
        skipList->Display();
    }

    // PriorityQueue
    PriorityQueue* Create_PriorityQueue(bool isMax = true){
        return new PriorityQueue(isMax);
    }

    void Destroy_PriorityQueue(PriorityQueue* pq){
        delete pq;
    }

    int IndexOf_PriorityQueue(PriorityQueue* pq, int key){
        return pq->IndexOf(key);
    }

    int GetSize_PriorityQueue(PriorityQueue* pq){
        return pq->GetSize();
    }

    double Top_PriorityQueue(PriorityQueue* pq){
        try {
            return pq->Top();
        } catch (const std::out_of_range& e) {
            std::cerr << "Error: " << e.what() << std::endl;
            return INT_MIN;
        }
    }

    double ExtractTop_PriorityQueue(PriorityQueue* pq){
        try {
            return pq->ExtractTop();
        } catch (const std::out_of_range& e) {
            std::cerr << "Error: " << e.what() << std::endl;
            return INT_MIN;
        }
    }

    void UpdateKey_PriorityQueue(PriorityQueue* pq, int i, double key){
        pq->UpdateKey(i, key);
    }

    void Insert_PriorityQueue(PriorityQueue* pq, double key){
        pq->Insert(key);
    }

    void HeapSort_PriorityQueue(PriorityQueue* pq){
        pq->HeapSort();
    }

    void Display_PriorityQueue(PriorityQueue* pq){
        pq->Display();
    }

    // Graph
    Graph* Create_Graph(bool directed){
        return new Graph(directed);
    }

    void Destroy_Graph(Graph* graph){
        delete graph;
    }

    bool IsDirected_Graph(Graph* graph){
        return graph->IsDirected();
    }

    int GetSize_Graph(Graph* graph){
        return graph->GetSize();
    }

    void CreateVertex_Graph(Graph* graph, int value){
        graph->CreateVertex(value);
    }

    void DeleteVertex_Graph(Graph* graph, int value){
        graph->DeleteVertex(value);
    }

    void CreateEdge_Graph(Graph* graph, int v, int u){
        graph->CreateEdge(v, u);
    }

    void CreateWeightedEdge_Graph(Graph* graph, int v, int u, double weight){
        graph->CreateEdge(v, u, weight);
    }

    void DeleteEdge_Graph(Graph* graph, int v, int u){
        graph->DeleteEdge(v, u);
    }

    LinkedList* GetNeighbors_Graph(Graph* graph, int value){
        try {
            return graph->GetNeighbors(value);
        } catch (const std::runtime_error& e) {
            std::cerr << "Error: " << e.what() << std::endl;
            return nullptr;
        }
    }

    LinkedList* GetVertices_Graph(Graph* graph){
        return graph->GetVertices();
    }

    void DisplayEdges_Graph(Graph* graph){
        graph->DisplayEdges();
    }

    void Display_Graph(Graph* graph){
        graph->Display();
    }

    struct BFSResult {
        std::map<int, std::string> colors;
        std::map<int, int> distances;
        std::map<int, GraphVertex*> parents;
    };

    BFSResult* BFS_Graph(Graph* graph, int s){
        try {
            auto [colors, distances, parents] = graph->BFS(s);
            BFSResult* res = new BFSResult();
            res->colors = colors;
            res->distances = distances;
            res->parents = parents;
            return res;
        } catch (const std::invalid_argument& e) {
            std::cerr << "Error: " << e.what() << std::endl;
            return nullptr;
        }
    }

    const char* GetBFSColor(BFSResult* res, int vertex){
        if (res == nullptr) return "";
        if (res->colors.find(vertex) != res->colors.end()) {
            return res->colors[vertex].c_str();
        }
        return "";
    }

    int GetBFSDistance(BFSResult* res, int vertex){
        if (res == nullptr) return -1;
        if (res->distances.find(vertex) != res->distances.end()) {
            return res->distances[vertex];
        }
        return -1;
    }

    int GetBFSParent(BFSResult* res, int vertex){
        if (res == nullptr) return -1;
        if (res->parents.find(vertex) != res->parents.end() && res->parents[vertex] != nullptr) {
            return res->parents[vertex]->GetData();
        }
        return -1;
    }

    void Destroy_BFSResult(BFSResult* res){
        delete res;
    }

    LinkedList* GetPath_Graph(Graph* graph, int s, int v){
        try {
            return graph->GetPath(s, v);
        } catch (const std::invalid_argument& e) {
            std::cerr << "Error: " << e.what() << std::endl;
            return nullptr;
        } catch (const std::runtime_error& e) {
            std::cerr << "Error: " << e.what() << std::endl;
            return nullptr;
        }
    }

    int Distance_Graph(Graph* graph, int s, int t){
        try {
            return graph->Distance(s, t);
        } catch (const std::invalid_argument& e) {
            std::cerr << "Error: " << e.what() << std::endl;
            return -1;
        }
    }

    LinkedList* GetReachableVertices_Graph(Graph* graph, int s){
        try {
            return graph->GetReachableVertices(s);
        } catch (const std::invalid_argument& e) {
            std::cerr << "Error: " << e.what() << std::endl;
            return nullptr;
        }
    }

    bool IsConnected_Graph(Graph* graph){
        return graph->IsConnected();
    }

    Graph* GetTransposed_Graph(Graph* graph){
        return graph->GetTransposed();
    }

    double EdgeWeight_Graph(Graph* graph, int v, int u){
        try {
            return graph->EdgeWeight(v, u);
        } catch (const std::invalid_argument& e) {
            std::cerr << "Error: " << e.what() << std::endl;
            return -1;
        }
    }

    double GraphWeight_Graph(Graph* graph){
        return graph->GraphWeight();
    }

    void Clear_Graph(Graph* graph){
        graph->Clear();
    }

    // SetItem
    SetItem* Create_SetItem(int value){
        return new SetItem(value, 0);
    }

    void Destroy_SetItem(SetItem* item){
        delete item;
    }

    int GetData_SetItem(SetItem* item){
        return item->GetData();
    }

    int GetRank_SetItem(SetItem* item){
        return item->GetRank();
    }

    SetItem* GetParent_SetItem(SetItem* item){
        return item->GetParent();
    }

    void SetRank_SetItem(SetItem* item, int rank){
        item->SetRank(rank);
    }

    void SetParent_SetItem(SetItem* item, SetItem* parent){
        item->SetParent(parent);
    }

    // DisjointSets
    DisjointSets* Create_DisjointSets(){
        return new DisjointSets();
    }

    void Destroy_DisjointSets(DisjointSets* ds){
        delete ds;
    }

    void MakeSet_DisjointSets(DisjointSets* ds, int x){
        ds->MakeSet(x);
    }

    SetItem* FindSet_DisjointSets(DisjointSets* ds, int x){
        try{
            return ds->FindSet(x);
        } catch (const std::runtime_error& e) {
            std::cerr << "Error: " << e.what() << std::endl;
            return nullptr;
        }
    }

    void Union_DisjointSets(DisjointSets* ds, int x, int y){
        ds->Union(x, y);
    }

    void Display_DisjointSets(DisjointSets* ds){
        ds->Display();
    }
}
