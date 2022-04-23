#include<iostream>
#include<complex>
#include<cmath>
#include<functional>
using namespace std;
auto diff(function<complex<double>(complex<double>)> f)
{
    auto h = 1e-20;
    auto df = [=](double x){
        complex<double> xc = x+h*1i;
        return imag(f(xc)/h);
    };
    return df;
}
int main()
{
    auto f1 = [](complex<double> x){return sin(x*x);};

    auto df1 = diff(f1);
    cout<<f1(1);
    cout<<"hello,world"<<endl;
    return 0;
}