class SkipListNode{
    private:
        int data;
        int height;
        std::vector<SkipListNode*> next;
        std::vector<SkipListNode*> prev;

    public:
        SkipListNode(int value, int h): data(value), height(h), next(h, nullptr), prev(h, nullptr) {}

        int GetData() const{
            return data;
        }

        int GetHeight() const{
            return height;
        }

        SkipListNode* GetNext(int level){
            if(level >= 0 && level < height){
                return next[level];
            }
            throw std::out_of_range("Level out of range");
        }

        SkipListNode* GetPrev(int level){
            if(level >= 0 && level < height){
                return prev[level];
            }
            throw std::out_of_range("Level out of range");
        }

        void SetData(int value){
            data = value;
        }

        void SetHeight(int h){
            height = h;
            next.resize(std::max(1, h), nullptr);
            prev.resize(std::max(1, h), nullptr);
        }

        void SetNext(int level, SkipListNode* node){
            if(level >= 0 && level < height){
                next[level] = node;
            }
        }

        void SetPrev(int level, SkipListNode* node){
            if(level >= 0 && level < height){
                prev[level] = node;
            }
        }
};