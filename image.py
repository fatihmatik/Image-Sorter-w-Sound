from PIL import Image


def split_image_vertically(image_path, num_tiles):
    # Open the image
    original_image = Image.open(image_path)

    # Get the width and height of the original image
    width, height = original_image.size

    # Calculate the width of each vertical tile
    tile_width = width // num_tiles

    # List to store individual tiles
    vertical_tiles = []

    # Iterate through the number of vertical tiles
    for i in range(num_tiles):
        # Calculate the left and right coordinates for cropping
        left = i * tile_width
        right = (i + 1) * tile_width if i < num_tiles - 1 else width

        # Crop the image vertically
        tile = original_image.crop((left, 0, right, height))

        # Append the cropped tile to the list
        vertical_tiles.append(tile)

    return vertical_tiles