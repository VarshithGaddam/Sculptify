from PIL import Image
import numpy as np
from rembg import remove
import trimesh

class ImageProcessor:
    def __init__(self, image_path):
        self.image_path = image_path

    def preprocess(self):
        """Remove background and convert to grayscale."""
        try:
            img = Image.open(self.image_path).convert("RGBA")
            img_no_bg = remove(img)
            img_gray = img_no_bg.convert("L")
            return np.array(img_gray)
        except Exception as e:
            raise ValueError(f"Image preprocessing failed: {e}")

    def image_to_voxel(self):
        """Convert 2D image to a simple voxel grid."""
        img_array = self.preprocess()
        # Threshold to binary
        binary = (img_array > 128).astype(np.uint8)
        # Create a 3D voxel grid (extrude 2D binary image)
        depth = 10  # Simple extrusion depth
        voxel = np.zeros((binary.shape[0], binary.shape[1], depth))
        for z in range(depth):
            voxel[:, :, z] = binary
        return voxel

    def voxel_to_mesh(self):
        """Convert voxel grid to mesh."""
        voxel = self.image_to_voxel()
        # Create a mesh from voxel grid
        mesh = trimesh.voxel.ops.matrix_to_marching_cubes(voxel)
        return mesh