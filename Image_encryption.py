try:
    from PIL import Image
    import numpy as np
    import os
except ImportError as e:
    print(f"Required packages not found. Please install them by running:")
    print("pip install pillow numpy")
    exit(1)

def invert_rgb(image_path, output_path):
    """
    Encrypt/decrypt image by inverting RGB values
    (R, G, B) → (255 - R, 255 - G, 255 - B)
    This transformation is fully reversible
    """
    try:
        with Image.open(image_path) as img:
            # Convert image to RGB if it's not (handles grayscale, RGBA, etc.)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Convert image to numpy array
            img_array = np.array(img)
            
            # Invert RGB values
            inverted_array = 255 - img_array
            
            # Save the inverted image
            Image.fromarray(inverted_array).save(output_path)
            
        print(f"Image processed and saved to {output_path}")
        return True
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        return False

def main():
    print("Image Encryption Tool with RGB Inversion")
    print("Note: The same operation encrypts and decrypts the image")
    
    try:
        input_path = input("Enter input image path: ")
        output_path = input("Enter output image path: ")
        
        if not os.path.exists(input_path):
            print("Error: Input file does not exist")
            return
            
        invert_rgb(input_path, output_path)
        print("Operation completed successfully!")
        print("Run the same operation again on the output image to decrypt it")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()