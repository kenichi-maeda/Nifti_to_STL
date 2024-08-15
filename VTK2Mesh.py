from netgen.occ import *
from netgen.stl import *

from ngsolve import *
import pyvista as pv

def convert_VTK_to_Mesh(filename):
    # Read a mesh from the given VTK file
    temp_mesh = pv.read(filename)

    # Save it as a STL file
    stl_file = "temp.stl"
    temp_mesh.save(stl_file)

    # Load the temp STL gfile
    geo = STLGeometry(stl_file)
    mesh = geo.GenerateMesh()

    return mesh