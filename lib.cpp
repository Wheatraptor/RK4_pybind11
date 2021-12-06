#include "lib.h"

double f1(double v2) {
	return v2;
}

double f2(double v1, double v2, double c, double k, double ks, double m) {
	return (-c * v2 - k * v1 - ks * pow(v1, 3)) / m;
}

vector<double> var1(double v1, double v2, double c, double k, double ks, double m) {
	vector<double> vect;
	double k1 = f1(v2);
	double l1 = f2(v1, v2, c, k, ks, m);
	vect.insert(vect.end(), { k1, l1 });
	return vect;
}

vector<double> var2(double v1, double v2, double c, double k, double ks, double m, double h, double k1, double l1) {
	vector<double> vect;
	double k2 = f1(v2 + (h / 2) * l1);
	double l2 = f2(v1 + (h / 2) * k1, v2 + (h / 2) * l1, c, k, ks, m);
	vect.insert(vect.end(), { k2, l2 });
	return vect;
}

vector<double> var3(double v1, double v2, double c, double k, double ks, double m, double h, double k2, double l2) {
	vector<double> vect;
	double k3 = f1(v2 + (h / 2) * l2);
	double l3 = f2(v1 + (h / 2) * k2, v2 + (h / 2) * l2, c, k, ks, m);
	vect.insert(vect.end(), { k3, l3 });
	return vect;
}

vector<double> var4(double v1, double v2, double c, double k, double ks, double m, double h, double k3, double l3) {
	vector<double> vect;
	double k4 = f1(v2 + h * l3);
	double l4 = f2(v1 + h * k3, v2 + h * l3, c, k, ks, m);
	vect.insert(vect.end(), { k4, l4 });
	return vect;
}

vector<vector<double>> rk4(double m, double k, double c, double ks, double v1, double v2, double step, bool mode, bool control, double control_val, double limit) {
	vector<vector<double>> table;
	vector<double> vec1, vec2, vec3, vec4;
	double n = 0;
	double h = 0;
	double k1, k2, k3, k4, l1, l2, l3, l4;
	double xn = 0;
	double vn1 = v1;
	double vn2 = v2;
	double vn1d = 0;
	double vn2d = 0;
	table.insert(table.end(), { n, h, xn, vn1, vn2, vn1d, vn2d });
	h = step;
	vn1d = v1;
	vn2d = v2;
	do {
		vec1 = var1(vn1, vn2, c, k, ks, m);
		k1 = vec1[0];
		l1 = vec1[1];
		vec2 = var2(vn1, vn2, c, k, ks, m, h, k1, l1);
		k2 = vec2[0];
		l2 = vec2[1];
		vec3 = var3(vn1, vn2, c, k, ks, m, h, k2, l2);
		k3 = vec3[0];
		l3 = vec3[1];
		vec4 = var4(vn1, vn2, c, k, ks, m, h, k3, l3);
		k4 = vec4[0];
		l4 = vec4[1];
		xn = xn + h;
		vn1 = vn1 + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4);
		vn2 = vn2 + (h / 6) * (l1 + 2 * l2 + 2 * l3 + l4);
		n++;
		table.insert(table.end(), { n, h, xn, vn1, vn2, vn1d, vn2d });
	} while (((mode == true) && (n < limit)) || ((mode == false) && (xn < limit)));
	return table;
}