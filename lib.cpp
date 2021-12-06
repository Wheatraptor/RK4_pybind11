#include "lib.h"

double f1(double v2) {
	return v2;
}

double f2(double v1, double v2, double c, double k, double ks, double m) {
	return ((-c * v2) - (k * v1) - (ks * pow(v1, 3))) / m;
}

vector<double> var1(double v1, double v2, double c, double k, double ks, double m) {
	vector<double> vect;
	double k1 = f1(v2);
	double l1 = f2(v1, v2, c, k, ks, m);
	//cout << "v1 " << v1 << " v2 " << v2 << " c " << c << " k " << k << " ks " << ks << " m " << m << " k1 " << k1 << " l1 " << l1 << endl;
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
	double k1, k2, k3, k4, l1, l2, l3, l4, S1, S2, Sn;
	double xn = 0;
	double vn1 = v1;
	double vn2 = v2;
	double vn1d = 0;
	double vn2d = 0;
	double Ss = 0;
	table.insert(table.end(), { n, h, xn, vn1, vn2, vn1d, vn2d, Ss});
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
		vn1 = vn1 + ((h / 6) * (k1 + 2 * k2 + 2 * k3 + k4));
		vn2 = vn2 + (h / 6) * (l1 + 2 * l2 + 2 * l3 + l4);
		h /= 2;
		for (int i = 0; i < 2; i++) {
			vec1 = var1(vn1d, vn2d, c, k, ks, m);
			k1 = vec1[0];
			l1 = vec1[1];
			vec2 = var2(vn1d, vn2d, c, k, ks, m, h, k1, l1);
			k2 = vec2[0];
			l2 = vec2[1];
			vec3 = var3(vn1d, vn2d, c, k, ks, m, h, k2, l2);
			k3 = vec3[0];
			l3 = vec3[1];
			vec4 = var4(vn1d, vn2d, c, k, ks, m, h, k3, l3);
			k4 = vec4[0];
			l4 = vec4[1];
			xn = xn + h;
			vn1d = vn1d + ((h / 6) * (k1 + 2 * k2 + 2 * k3 + k4));
			vn2d = vn2d + (h / 6) * (l1 + 2 * l2 + 2 * l3 + l4);
		}
		h *= 2;

		S1 = (vn1d - vn1) / 15;
		S2 = (vn2d - vn2) / 15;
		S1 = abs(S1);
		S2 = abs(S2);
		Sn = max(S1, S2);
		Ss = Sn * 16;

		if (control == true) {
			cout << vn1 << endl;
			if (abs(Sn) <= control_val && abs(Sn) >= (control_val / 32)) {
				table.insert(table.end(), { n, h, xn, vn1, vn2, vn1d, vn2d, Ss });
				xn = xn + h;
				n++;
			}
			else if (abs(Sn) < (control_val / 32)) {
				table.insert(table.end(), { n, h, xn, vn1, vn2, vn1d, vn2d, Ss });
				xn = xn + h;
				h *= 2;
				n++;
			}
			else {
				h /= 2;
				
				vn1 = table[n][3];
				vn2 = table[n][4];
				if (n != 0) {
					vn1d = table[n][5];
					vn2d = table[n][6];
				}
				else {
					vn1d = v1;
					vn2d = v2;
				}
			}
		}
		else {
			table.insert(table.end(), { n, h, xn, vn1, vn2, vn1d, vn2d, Ss });
			xn = xn + h;
			n++;
		}
		//cout << " k1 " << k1 << " l1 " << l1 << " k2 " << k2 << " l2 " << l2 << " k3 " << k3 << " l3 " << l3 << " k4 " << k4 << " l4 " << l4 << endl;
		//cout << endl;
	} while (((mode == true) && (n < limit)) || ((mode == false) && (xn < limit)));
	return table;
}