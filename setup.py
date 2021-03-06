from distutils.core import setup, Extension
import numpy

module = Extension("_shinythings",
                   sources=["_shinythings/_shinythings.c",
                            "_shinythings/_shinythings_Scene.c",
                            "_shinythings/_shinythings_Matrix.c",
                            "_shinythings/render.c",
                            "_shinythings/color.c",
                            "_shinythings/py_parse.c",
                            "_shinythings/kd_tree.c",
                            "_shinythings/scene.c",
                            "_shinythings/matrix.c",
                            "_shinythings/geometry.c"],
                   include_dirs=[numpy.get_include(), "_shinythings/"],
                   extra_compile_args=["-O3"])

setup(
    name="shinythings",
    description="Simple ray tracer supporting Phong shading, Wavefront .obj file loading, among other features",
    author="Andrew Bauer",
    packages=["shinythings"],
    license="MIT",
    ext_modules=[module])

