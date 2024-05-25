int multiply(int a, int b) {
    float result;
    result = a * b;
    return result;
}

int sum(int a, int b) {
    int result;
    result = a + b;
    return result;
}

int main() {
    int x;
    int y;
    int result;
    
    x = 5;
    y = 10;
    result = sum(x, y);

	x = 3;
    y = 2;
    result = multiply(x, y);
    
    return 0;
}
