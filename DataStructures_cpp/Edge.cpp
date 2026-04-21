class Edge{
    private:
        int v;
        int u;
        double weight;
        bool directed;

    public:
        Edge(int v, int u, bool directed): v(v), u(u), weight(0), directed(directed) {}

        Edge(int v, int u, double weight, bool directed): v(v), u(u), weight(weight), directed(directed) {}

        int GetV(){
            return v;
        }

        int GetU(){
            return u;
        }

        double GetWeight(){
            return weight;
        }

        void SetWeight(double weight){
            this->weight = weight;
        }

        void Display(){
            if(directed)
                std::cout << "(" << v << " --> " << u << "), weight = " << weight << std::endl;
            else
                std::cout << "(" << v << " <--> " << u << "), weight = " << weight << std::endl;
        }
};