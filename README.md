### How to convert NIfTI to Mesh via STL

#### 1. Convert NIfTi to VTK<br>
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
Pass  the vtk file to ```convert_VTK_to_Mesh()``` which returns a corresponding mesh.

-------------------
##### Note
1. ```test.ipynb``` viusalizes the mesh.
2. For VTK to STL conversions, just do Step2.

