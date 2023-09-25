def main():
    import sys
    from PIL import Image
    from PIL import ImageOps

    # check for correct number of command line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # verify that both files are the same type and .jpg or .jpeg or .png file
    input_file = sys.argv[1].lower()
    output_file = sys.argv[2].lower()
    input_type = input_file.split(".")[1]
    output_type = output_file.split(".")[1]
    if input_type != "jpeg" and input_type != "jpg" and input_type != "png":
        sys.exit("Invalid input")
    if output_type != "jpeg" and output_type != "jpg" and output_type != "png":
        sys.exit("Invalid output")
    if input_type != output_type:
        sys.exit("Input and output have different extensions")

    # Get shirt size
    shirt = Image.open("shirt.png")
    size = shirt.size

    # Open input file
    try:
        image = Image.open(input_file)
    except (Exception):
        sys.exit("Input does not exist")

    # Resize image
    resized_image = ImageOps.fit(image, size)

    # Paste shirt
    resized_image.paste(shirt, shirt)

    # Save file
    resized_image.save(output_file)

if __name__ == "__main__":
    main()
