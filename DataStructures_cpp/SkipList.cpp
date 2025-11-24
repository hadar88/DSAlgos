class SkipList{
    private:
        SkipListNode* head;
        int height;

        SkipListNode* Find(int key){
            if(head == nullptr) return nullptr;

            SkipListNode* p = head;
            for(int i = height - 1; i >= 0; i--){
                while(p->GetNext(i) != nullptr && p->GetNext(i)->GetData() <= key){
                    p = p->GetNext(i);
                }
            }
            return p;
        }

        int randomHeight(){
            int height = 1;
            int r = std::rand();
            while(r % 2 == 0){
                height++;
                r = std::rand();
            }
            return height;
        }

        int Place(int key){
            int place = 0;
            SkipListNode* current = head;
            while(current != nullptr && current->GetData() != key){
                current = current->GetNext(0);
                place++;
            }
            return place;
        }

        int digitsInNumber(int n){
            int digits = 0;
            if (n == 0) return 1;
            while(n != 0){
                digits++;
                n /= 10;
            }
            return digits;
        }

    public:
        SkipList(): head(nullptr), height(1) {
            std::srand(std::time(nullptr));
        }

        ~SkipList(){
            while(head != nullptr){
                SkipListNode* temp = head;
                head = head->GetNext(0);
                delete temp;
            }
        }

        bool IsEmpty(){
            if(head == nullptr) return true;
            else if(head->GetNext(0) == nullptr) return true;
            return false;
        }

        SkipListNode* GetHead(){
            return head;
        }

        int GetHeight(){
            return height;
        }

        SkipListNode* Search(int key){
            SkipListNode* p = Find(key);
            if(p != nullptr && p->GetData() == key)
                return p;
            return nullptr;
        }

        void Insert(int key){
            if(Search(key) != nullptr || key == INT_MIN){
                std::cout << "Warning: " << key << " already exists." << std::endl;
                return;
            }

            int newHeight = randomHeight();
            SkipListNode* x = new SkipListNode(key, newHeight);

            if(head == nullptr){
                head = new SkipListNode(INT_MIN, newHeight);
                height = newHeight;
                for(int i = 0; i < newHeight; i++){
                    head->SetNext(i, x);
                    x->SetPrev(i, head);
                }
                return;
            }

            if(newHeight > height){
                height = newHeight;
                head->SetHeight(newHeight);
            }

            SkipListNode* p = Find(key);

            for(int i = 0; i < newHeight; i++){
                SkipListNode* next = p->GetNext(i);
                p->SetNext(i, x);
                x->SetNext(i, next);
                if(next != nullptr)
                    next->SetPrev(i, x);
                x->SetPrev(i, p);

                while(p->GetHeight() == i + 1 && p->GetPrev(i) != nullptr)
                    p = p->GetPrev(i);
            }
        }

        void Delete(int key){
            if(key == INT_MIN) return;

            SkipListNode* x = Search(key);
            if(x == nullptr){ 
                std::cout << "WARNING: " << key << " not found!" << std::endl;
                return; 
            }

            for(int i = 0; i < x->GetHeight(); i++){
                SkipListNode* prev = x->GetPrev(i);
                SkipListNode* next = x->GetNext(i);

                if(prev != nullptr){
                    prev->SetNext(i, next);
                }
                if(next != nullptr){
                    next->SetPrev(i, prev);
                }
            }

            // std::cout << "Delete " << key << std::endl;

            int newHeight = 1;

            for(int i = this->height - 1; i >= 0; i--){
                if(head->GetNext(i) != nullptr){
                    newHeight = i + 1;
                    break;
                }
            }

            if(newHeight < 1) newHeight = 1;

            if(newHeight != this->height){
                for(int i = newHeight; i < this->height; i++){
                    head->SetNext(i, nullptr);
                    head->SetPrev(i, nullptr);
                }
                this->height = newHeight;
                head->SetHeight(newHeight);
            }

            delete x;
        }

        void Display() {
            if (head == nullptr) {
                std::cout << "The skip list is empty" << std::endl;
                return;
            }
            std::cout << "The skip list contains: " << std::endl;
            for (int i = height - 1; i >= 0; i--) {
                std::cout << "[ ]";
                
                SkipListNode* node = head->GetNext(i);
                while (node != nullptr) {
                    std::string space = "";
                    int place = Place(node->GetData());

                    SkipListNode* prev = node->GetPrev(i);
                    int prevPlace = Place(prev->GetData()); 

                    int delta = place - prevPlace - 1;
                    
                    int prevData;
                    int size;
                    int amount = 0; 
                    
                    for(int j = 0; j < delta; j++){
                        prev = prev->GetNext(0);
                        prevData = prev->GetData();
                        size = digitsInNumber(prevData) + 2;
                        amount += size;
                    }

                    amount += 1 * (delta + 1);

                    for(int j = 0; j < amount; j++){
                        space += " ";
                    }

                    std::cout << space << "[" << node->GetData() << "]";
                    node = node->GetNext(i);
                }
                std::cout << std::endl;
            }
        }
};