#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "lib.h"

namespace py = pybind11;

PYBIND11_MODULE(rk4s, m) {
    m.def("rk4", &rk4);
};