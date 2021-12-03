#pragma once
#include <vector>
using namespace std;

double f1(double v2);

double f2(double v1, double v2, double c, double k, double ks, double m);

vector<double> var1(double v1, double v2, double c, double k, double ks, double m);

vector<double> var2(double v1, double v2, double c, double k, double ks, double m, double h, double k1, double l1);

vector<double> var3(double v1, double v2, double c, double k, double ks, double m, double h, double k2, double l2);

vector<double> var4(double v1, double v2, double c, double k, double ks, double m, double h, double k3, double l3);

vector<vector<double>> rk4(double h, double m, double k, double c, double ks, double v1, double v2, bool mode, bool control, double control_val, double limit);