template<typename T>

class TreeNode{
    private:
        T data;
        TreeNode<T>* right;
        TreeNode<T>* left;
        TreeNode<T>* parent;

    public:
        TreeNode(T value): data(value), right(nullptr), left(nullptr), parent(nullptr) {}

        T GetData(){
            return data;
        }

        TreeNode<T>* GetRight(){
            return right;
        }

        TreeNode<T>* GetLeft(){
            return left;
        }

        TreeNode<T>* GetParent(){
            return parent;
        }

        void SetData(T value) {
            data = value;
        }

        void SetRight(TreeNode<T>* rightNode){
            right = rightNode;
        }

        void SetLeft(TreeNode<T>* leftNode){
            left = leftNode;
        }

        void SetParent(TreeNode<T>* parentNode){
            parent = parentNode;
        }
};