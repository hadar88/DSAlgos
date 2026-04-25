UPLOAD=false
WIN_INSTALL=false

for arg in "$@"; do
    if [ "$arg" == "--upload" ]; then
        UPLOAD=true
    elif [ "$arg" == "--windows" ]; then
        WIN_INSTALL=true
    fi
done

if [ -f ".env" ]; then
    source .env
fi

version=$(sed -n 's/^version = "\([^"]*\)"/\1/p' pyproject.toml | tr -d '\r')
echo "Version detected: $version"

echo "building dstructures.so..."
g++ -shared -fPIC -o src/algos_structs/DataStructures/dstructures.so Build/dstructures.cpp

echo "building algos.so..."
g++ -shared -fPIC -o src/algos_structs/Algos/algos.so Build/algos.cpp

echo "cleaning up pycache..."
find . -type d -name "__pycache__" -exec rm -rf {} +

echo "building wheel (package)..."
python -m build

echo "cleaning up egg-info..."
rm -rf src/algos_structs.egg-info

echo "uninstalling current package on WSL..."
pip uninstall algos-structs -y

if [ "$WIN_INSTALL" = true ]; then
    echo "uninstalling current package on Windows..."
    python3.13.exe -m pip uninstall algos-structs -y
fi

if [ "$UPLOAD" = true ]; then
    echo ""
    echo "--- Uploading to PyPI ---"

    python -m pip install --upgrade twine -q
    python -m twine upload dist/*
    
    echo "Waiting for PyPI to index the new version (10s)..."
    sleep 10
    
    echo "installing new package from PyPI on WSL..."
    pip install --no-cache-dir -U algos-structs==${version}
    
    if [ "$WIN_INSTALL" = true ]; then
        echo "installing new package from PyPI on Windows (for VS Code IntelliSense)..."
        python3.13.exe -m pip install --no-cache-dir -U algos-structs==${version}
    fi
else
    echo "installing new package locally on WSL..."
    pip install -U dist/algos_structs-${version}-py3-none-any.whl
    
    if [ "$WIN_INSTALL" = true ]; then
        echo "installing new package locally on Windows (for VS Code IntelliSense)..."
        python3.13.exe -m pip install -U dist/algos_structs-${version}-py3-none-any.whl
    fi
fi

echo "Done!!!"