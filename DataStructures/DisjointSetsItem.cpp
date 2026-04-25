class SetItem{
    private:
        int data;
        int rank;
        SetItem* parent;

    public:
        SetItem(int data, int rank): data(data), rank(rank), parent(this) {}

        int GetData(){
            return data;
        }

        int GetRank(){
            return rank;
        }

        SetItem* GetParent(){
            return parent;
        }

        void SetRank(int rank){
            this->rank = rank;
        }

        void SetParent(SetItem* parent){
            this->parent = parent;
        }
};