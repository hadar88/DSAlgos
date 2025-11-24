class BinarySearchTree{
    private:
        TreeNode<int>* root;

        void DeleteTree(TreeNode<int>* node){
            if(node != nullptr){
                DeleteTree(node->GetLeft());
                DeleteTree(node->GetRight());
                delete node;
            }
        }

    public:
        BinarySearchTree(): root(nullptr) {}

        ~BinarySearchTree(){
            DeleteTree(root);
        }

        bool IsEmpty(){
            return root == nullptr;
        }

        TreeNode<int>* GetRoot(){
            return root;
        }

        bool Exists(int key){
            TreeNode<int>* current = root;

            while(current != nullptr){
                if(current->GetData() == key)
                    return true;
                else if(current->GetData() < key)
                    current = current->GetRight();
                else
                    current = current->GetLeft();
            }
            return false;
        }

        TreeNode<int>* Search(int key){
            if(!Exists(key)){
                std::cout << "Key does not exist in the tree." << std::endl;
                return nullptr;
            }
            
            TreeNode<int>* current = root;

            while(current != nullptr && current->GetData() != key){
                if(key < current->GetData())
                    current = current->GetLeft();
                else
                    current = current->GetRight();
            }

            return current;
        }

        int Minimum(){
            if(root == nullptr) 
                throw std::runtime_error("The tree is empty");

            TreeNode<int>* current = root;

            while(current->GetLeft() != nullptr)
                current = current->GetLeft();

            return current->GetData();
        }

        int Maximum(){
            if(root == nullptr) 
                throw std::runtime_error("The tree is empty");

            TreeNode<int>* current = root;

            while(current->GetRight() != nullptr)
                current = current->GetRight();

            return current->GetData();
        }

        TreeNode<int>* Successor(int key){
            if(!Exists(key))
                throw std::runtime_error("Key does not exist in the tree.");

            if(key == Maximum()){
                throw std::runtime_error("The key is the maximum in the tree, no successor exists.");
            }

            TreeNode<int>* current = Search(key);

            if(current->GetRight() != nullptr) {
                TreeNode<int>* temp = current->GetRight();
                while (temp->GetLeft() != nullptr) {
                    temp = temp->GetLeft();
                }
                return temp;
            }
            TreeNode<int>* y = current->GetParent();
            while(y != nullptr && current == y->GetRight()){
                current = y;
                y = y->GetParent();
            }
            return y;
        }

        void Insert(int key){
            if(Exists(key)){
                std::cout << "Key already exists in the tree." << std::endl;
                return;
            }

            TreeNode<int>* current = root;
            TreeNode<int>* newItem = new TreeNode<int>(key);
            TreeNode<int>* y = nullptr;
            
            while(current != nullptr){
                y = current;
                if(key < current->GetData())
                    current = current->GetLeft();
                else
                    current = current->GetRight();
            }
            newItem->SetParent(y);
            if(y == nullptr)
                root = newItem;
            else if(key < y->GetData())
                y->SetLeft(newItem);
            else
                y->SetRight(newItem);
        }

        void Delete(int key){
            if(!Exists(key)){
                std::cout << "Key does not exist in the tree." << std::endl;
                return;
            }

            TreeNode<int>* current = Search(key);

            if(current->GetRight() == nullptr && current->GetLeft() == nullptr){ // Case 1: No children
                if(current->GetParent() == nullptr) {
                    root = nullptr;
                    delete current;
                }
                else{
                    if(current->GetParent()->GetRight() == current){
                        current->GetParent()->SetRight(nullptr);
                        delete current;
                    }
                    else{
                        current->GetParent()->SetLeft(nullptr);
                        delete current;
                    }
                }
            }
            else if(current->GetRight() != nullptr && current->GetLeft() == nullptr){ // Case 2: One child (right)
                if(current->GetParent() == nullptr){
                    root = current->GetRight();
                    root->SetParent(nullptr);
                    delete current;
                }
                else{
                    if(current->GetParent()->GetRight() == current){
                        current->GetParent()->SetRight(current->GetRight());
                        current->GetRight()->SetParent(current->GetParent());
                    }
                    else{
                        current->GetParent()->SetLeft(current->GetRight());
                        current->GetRight()->SetParent(current->GetParent());
                    }
                    delete current;
                }
            }
            else if(current->GetRight() == nullptr && current->GetLeft() != nullptr){ // Case 2: One child (left)
                if(current->GetParent() == nullptr){
                    root = current->GetLeft();
                    root->SetParent(nullptr);
                    delete current;
                }
                else{
                    if(current->GetParent()->GetRight() == current){
                        current->GetParent()->SetRight(current->GetLeft());
                        current->GetLeft()->SetParent(current->GetParent());
                    }
                    else{
                        current->GetParent()->SetLeft(current->GetLeft());
                        current->GetLeft()->SetParent(current->GetParent());
                    }
                    delete current;
                }
            }
            else{ // Case 3: Two children
                TreeNode<int>* y = Successor(current->GetData());
                int successorData = y->GetData();
                Delete(successorData);
                current->SetData(successorData);
            }
        }

        int Depth(int key){
            if(!Exists(key))
                throw std::runtime_error("Key does not exist in the tree.");

            TreeNode<int>* current = Search(key);
            int depth = 0;

            while(true){
                if(current == root)
                    break;
                    
                depth += 1;
                current = current->GetParent();
            }

            return depth;
        }

        int Height(int key){
            if(!Exists(key))
                throw std::runtime_error("Key does not exist in the tree.");

            TreeNode<int>* current = Search(key);
            int leftHeight = 0, rightHeight = 0;

            if(current->GetLeft() != nullptr)
                leftHeight = Height(current->GetLeft()->GetData()) + 1;
            if(current->GetRight() != nullptr)
                rightHeight = Height(current->GetRight()->GetData()) + 1;

            return std::max(leftHeight, rightHeight);
        }

        void InOrder(TreeNode<int>* current){
            if(current != nullptr){
                InOrder(current->GetLeft());
                std::cout << current->GetData() << " ";
                InOrder(current->GetRight());
            }
            if(current == root){
                std::cout << std::endl;
            }
        }

        void PreOrder(TreeNode<int>* current){
            if(current != nullptr){
                std::cout << current->GetData() << " ";
                PreOrder(current->GetLeft());
                PreOrder(current->GetRight());
            }
            if(current == root){
                std::cout << std::endl;
            }
        }

        void PostOrder(TreeNode<int>* current){
            if(current != nullptr){
                PostOrder(current->GetLeft());
                PostOrder(current->GetRight());
                std::cout << current->GetData() << " ";
            }
            if(current == root){
                std::cout << std::endl;
            }
        }
};