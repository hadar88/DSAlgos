from DataStructures import LinkedList, Stack, Queue, PriorityQueue, SkipList, Graph, DisjointSets, BinarySearchTree, AVLTree

def test_linkedlist_display(capfd):
    ll = LinkedList()
    ll.Insert(1)
    ll.Insert(2)
    ll.Insert(3)
    
    ll.Display()
    out, err = capfd.readouterr()
    assert "[3] -> [2] -> [1]" in out

def test_stack_display(capfd):
    s = Stack()
    s.Push(10)
    s.Push(20)
    
    s.Display()
    out, err = capfd.readouterr()
    assert "The stack contains:" in out
    assert "|20|" in out
    assert "|10|" in out

def test_queue_display(capfd):
    q = Queue()
    q.Enqueue(1)
    q.Enqueue(2)
    
    q.Display()
    out, err = capfd.readouterr()
    assert "1" in out
    assert "2" in out

def test_priorityqueue_display(capfd):
    pq = PriorityQueue()
    pq.Insert(10)
    pq.Insert(20)
    pq.Insert(15)
    
    pq.Display()
    out, err = capfd.readouterr()
    assert "20 10 15" in out or "20 15 10" in out

def test_skiplist_display(capfd):
    sl = SkipList()
    sl.Insert(10)
    sl.Insert(20)
    
    sl.Display()
    out, err = capfd.readouterr()
    assert "The skip list contains:" in out
    assert "[10]" in out
    assert "[20]" in out

def test_disjointsets_display(capfd):
    ds = DisjointSets()
    ds.MakeSet(0)
    ds.MakeSet(1)
    ds.Union(0, 1)
    
    ds.Display()
    out, err = capfd.readouterr()
    assert "0" in out
    assert "1" in out

def test_graph_display(capfd):
    g = Graph(directed=False)
    g.CreateVertex(1)
    g.CreateVertex(2)
    g.CreateWeightedEdge(1, 2, 10)
    
    g.Display()
    out, err = capfd.readouterr()
    assert "Graph is undirected" in out
    assert "1 -> 2" in out or "2 -> 1" in out
    
    g.DisplayEdges()
    out, err = capfd.readouterr()
    assert "(1 <--> 2), weight = 10" in out or "(2 <--> 1), weight = 10" in out

def test_bst_traversals(capfd):
    bst = BinarySearchTree()
    bst.Insert(2)
    bst.Insert(1)
    bst.Insert(3)
    
    bst.InOrder()
    out, err = capfd.readouterr()
    assert out.strip() == "1 2 3"
    
    bst.PreOrder()
    out, err = capfd.readouterr()
    assert out.strip() == "2 1 3"
    
    bst.PostOrder()
    out, err = capfd.readouterr()
    assert out.strip() == "1 3 2"

def test_avltree_traversals(capfd):
    avl = AVLTree()
    avl.Insert(1)
    avl.Insert(2)
    avl.Insert(3)
    
    avl.InOrder()
    out, err = capfd.readouterr()
    assert out.strip() == "1 2 3"
    
    avl.PreOrder()
    out, err = capfd.readouterr()
    assert out.strip() == "2 1 3"

def test_graph_getpath_invalid_argument(capfd):
    g = Graph(directed=True)
    g.CreateVertex(1)
    path = g.GetPath(1, 2)
    out, err = capfd.readouterr()
    assert path is None
    assert "Error: Vertex 1 or 2 does not exist" in err

def test_graph_getpath_runtime_error(capfd):
    g = Graph(directed=True)
    g.CreateVertex(1)
    g.CreateVertex(2)
    path = g.GetPath(1, 2)
    out, err = capfd.readouterr()
    assert path is None
    assert "Error: No path from 1 to 2 exists" in err

def test_empty_structures_display(capfd):
    ll = LinkedList()
    ll.Display()
    out, err = capfd.readouterr()
    assert "LinkedList is empty" in out
    
    s = Stack()
    s.Display()
    out, err = capfd.readouterr()
    assert "Stack is empty" in out
    
    q = Queue()
    q.Display()
    out, err = capfd.readouterr()
    assert "Queue is empty" in out
    
    sl = SkipList()
    sl.Display()
    out, err = capfd.readouterr()
    assert "The skip list is empty" in out

def test_single_element_display(capfd):
    ll = LinkedList()
    ll.Insert(-5)
    ll.Display()
    out, err = capfd.readouterr()
    assert "[-5]" in out

def test_graph_no_edges_display(capfd):
    g = Graph(directed=False)
    g.CreateVertex(1)
    g.CreateVertex(2)
    
    g.Display()
    out, err = capfd.readouterr()
    assert "1 -> No neighbors" in out
    assert "2 -> No neighbors" in out
    
    g.DisplayEdges()
    out, err = capfd.readouterr()

def test_tree_degenerate_display(capfd):
    bst = BinarySearchTree()
    bst.Insert(1)
    bst.Insert(2)
    bst.Insert(3)
    
    bst.InOrder()
    out, err = capfd.readouterr()
    assert out.strip() == "1 2 3"
    
    bst.PreOrder()
    out, err = capfd.readouterr()
    assert out.strip() == "1 2 3"

def test_priority_queue_overflow(capfd):
    pq = PriorityQueue()
    for i in range(10):
        pq.Insert(i)
    
    pq.Display()
    out, err = capfd.readouterr()
    assert "9" in out
    assert "0" in out

def test_graph_self_loop_display(capfd):
    g = Graph(directed=True)
    g.CreateVertex(1)
    g.CreateVertex(2)
    g.CreateEdge(1, 2)
    
    g.Display()
    out, err = capfd.readouterr()
    assert "1 -> 2" in out
    
    g.DisplayEdges()
    out, err = capfd.readouterr()
    assert "(1 --> 2)" in out

def test_graph_getpath_exceptions(capfd):
    g = Graph(directed=True)
    g.CreateVertex(1)
    g.CreateVertex(2)
    
    path = g.GetPath(1, 3)
    out, err = capfd.readouterr()
    assert path is None
    assert "Error: Vertex 1 or 3 does not exist" in err
    
    path = g.GetPath(1, 2)
    out, err = capfd.readouterr()
    assert path is None
    assert "Error: No path from 1 to 2 exists" in err