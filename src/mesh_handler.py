import trimesh
import pyrender
import numpy as np

class MeshHandler:
    def __init__(self, mesh):
        self.mesh = mesh

    def export(self, output_path):
        """Export mesh to .stl or .obj."""
        try:
            self.mesh.export(output_path)
        except Exception as e:
            raise ValueError(f"Mesh export failed: {e}")

    def visualize(self):
        """Visualize mesh using pyrender."""
        try:
            scene = pyrender.Scene()
            mesh = pyrender.Mesh.from_trimesh(self.mesh)
            scene.add(mesh)
            pyrender.Viewer(scene, use_raymond_lighting=True)
        except Exception as e:
            raise ValueError(f"Visualization failed: {e}")