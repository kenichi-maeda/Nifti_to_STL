### How to convert NIfTI to Mesh via STL

#### 1. Concert NIfTi to VTK<br>
Go to https://github.com/neurolabusc/nii2mesh and clone the repo.
```
git clone https://github.com/neurolabusc/nii2mesh
cd nii2mesh/src
make
```
Then,
```
./nii2mesh input.nii output.vtk
```

#### 2. Convert VTK to STL and Load it
Pass in the vtk file the convert_VTK_to_Mesh() function which returns a corresponding mesh.

-------------------
(Note)<brs>
test.ipynb viusalizes a mesh.

