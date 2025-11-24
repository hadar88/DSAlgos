class Edge{
    private:
        int v;
        int u;

    public:
        Edge(int v, int u): v(v), u(u) {}

        int getV(){
            return v;
        }

        int getU(){
            return u;
        }

        void Display(){ 
            std::cout << "(" << v << "," << u << ")" << std::endl;
        }
};
