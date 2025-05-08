import argparse
from image_processor import ImageProcessor
from text_to_3d import TextTo3D
from mesh_handler import MeshHandler

def main():
    parser = argparse.ArgumentParser(description="Convert photo or text to 3D model.")
    parser.add_argument("--image", type=str, help="Path to input image")
    parser.add_argument("--text", type=str, help="Text prompt for 3D generation")
    parser.add_argument("--output", type=str, required=True, help="Output file (.stl or .obj)")
    args = parser.parse_args()

    if args.image and args.text:
        raise ValueError("Provide either an image or text prompt, not both.")
    if not (args.image or args.text):
        raise ValueError("Provide an image or text prompt.")

    if args.image:
        processor = ImageProcessor(args.image)
        mesh = processor.voxel_to_mesh()
    else:
        generator = TextTo3D()
        mesh = generator.generate(args.text)

    handler = MeshHandler(mesh)
    handler.export(args.output)
    handler.visualize()

if __name__ == "__main__":
    main()