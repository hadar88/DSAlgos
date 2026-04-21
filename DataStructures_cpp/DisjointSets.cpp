class DisjointSets{
    private:
        std::vector<SetItem*> items;

        SetItem* FindItem(int x){
            for(SetItem* i : items)
                if(i->GetData() == x)
                    return i;

            throw std::runtime_error("Item " + std::to_string(x) + " not found in the disjoint sets");
        }

        bool IsExist(int x){
            try{
                FindItem(x);
                return true;
            } catch (const std::runtime_error& e) {
                return false;
            }
        }

    public:
        DisjointSets(): items() {}

        ~DisjointSets(){
            for(SetItem* i : items)
                delete i;
        }

        void MakeSet(int x){
            if(IsExist(x)){
                std::cerr << "Error: Item " << x << " already exists in the disjoint sets" << std::endl;
                return;
            }
            
            SetItem* new_item = new SetItem(x, 0);
            items.push_back(new_item);
        }

        SetItem* FindSet(int x){
            try{
                SetItem* item = FindItem(x);
                if(item->GetParent() != item)
                    item->SetParent(FindSet(item->GetParent()->GetData()));
                return item->GetParent();
            } catch (const std::runtime_error& e) {
                throw std::runtime_error(e.what());
            }
        }

        void Union(int x, int y){
            if(x == y){
                std::cerr << "Error: Items are the same" << std::endl;
                return;
            }

            try{
                SetItem* x_item = FindSet(x);
                SetItem* y_item = FindSet(y);
                if(x_item == y_item){
                    std::cerr << "Error: Items are already in the same set" << std::endl;
                    return;
                }

                if(x_item->GetRank() > y_item->GetRank())
                    y_item->SetParent(x_item);
                else{
                    x_item->SetParent(y_item);
                    if(x_item->GetRank() == y_item->GetRank())
                        y_item->SetRank(y_item->GetRank() + 1);
                }
            } catch (const std::runtime_error& e){
                std::cerr << e.what() << std::endl;
            }
        }

        void Display(){
            if(items.empty()){
                std::cout << "Disjoint sets is empty" << std::endl;
                return;
            }

            for(SetItem* i : items){
                std::cout << i->GetData() << " -> " << i->GetParent()->GetData() << std::endl;
            }
        }
};