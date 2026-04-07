class Edge{
    private:
        int v;
        int u;
        double weight;
        bool directed;

    public:
        Edge(int v, int u, bool directed): v(v), u(u), weight(0), directed(directed) {}

        Edge(int v, int u, double weight, bool directed): v(v), u(u), weight(weight), directed(directed) {}

        int getV(){
            return v;
        }

        int getU(){
            return u;
        }

        double getWeight(){
            return weight;
        }

        void setWeight(double weight){
            weight = weight;
        }

        void Display(){
            if(directed)
                std::cout << "(" << v << " --> " << u << "), weight = " << weight << std::endl;
            else
                std::cout << "(" << v << " <--> " << u << "), weight = " << weight << std::endl;
        }
};