import os
import argparse
from PIL import Image


# for understanding purpose i am performing the task of resizing image for single image only then i will jump for batch resizing.
def resize_single_image(source_path, destination_path, target_width, target_height):
    try:
        with Image.open(source_path) as original:
            resized = original.resize(
                (target_width, target_height), Image.Resampling.LANCZOS
            )
            resized.save(destination_path)
        print(f"Saved resized image to: {destination_path}")
    except FileNotFoundError:
        print(f"Image is not available at the path: {source_path} Check & Verify")
    except Exception as err:
        print(f"There is Some error in resizing the Image: {err}")


# for "resize_single_image" functionto work i will pass the the functions and its arguments after taking from user.
# if __name__ == "__main__":
#     source_path = input("Enter the source_path of the image to resize: ")
#     destination_path = input(
#         "Enter the Destination_path to save the resized image (including filename and extension): "
#     )
#     target_width = int(input("Enter the target width (px): "))
#     target_height = int(input("Enter the target height (px): "))


def resize_images_in_directory(source_dir, destination_dir, width, height):
    # I am checking that path is available or not, if it is not available i am creating it.
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        # I am Assigning the extensions to suppport and i will check the file extension later using this variable.
    supported_extensions = (".png", ".jpg", ".jpeg")

    # Tracing that how many images were processed
    total = 0

    for item in os.listdir(source_dir):
        if item.lower().endswith(supported_extensions):
            original_path = os.path.join(source_dir, item)

            # Splitting the filename and extension to use these filenam to store the output.
            filename, _ = os.path.splitext(item)
            new_filename = f"{filename}_resized.jpg"

            save_path = os.path.join(destination_dir, new_filename)
            # I am resizing the all directory image files one by one in loop using my single resize function.
            resize_single_image(original_path, save_path, width, height)
            total += 1

    print(
        f"\n The resizing of {total} image(s) of your directory:{source_dir} is Completed and stored at the location: {destination_dir}  "
    )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description=" Resize images in bulk! Just provide source & target folder, plus width and height."
    )

    parser.add_argument(
        "source_folder", type=str, help=" Folder containing images you want to resize"
    )

    parser.add_argument(
        "destination_folder", type=str, help=" Folder to save resized images into"
    )

    parser.add_argument("width", type=int, help=" Desired width in pixels")

    parser.add_argument("height", type=int, help=" Desired height in pixels")

    args = parser.parse_args()

    resize_images_in_directory(
        source_dir=args.source_folder,
        destination_dir=args.destination_folder,
        width=args.width,
        height=args.height,
    )
