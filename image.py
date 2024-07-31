from PIL import Image, ImageEnhance

def enhance_image(file_path):
    # Open an image file
    with Image.open(file_path) as img:
        # Enhancing the image's brightness
        enhancer = ImageEnhance.Brightness(img)
        img_enhanced = enhancer.enhance(1.5)  # Increase brightness by 50%
        
        # Enhancing the image's contrast
        enhancer = ImageEnhance.Contrast(img_enhanced)
        img_enhanced = enhancer.enhance(1.5)  # Increase contrast by 50%

        # Save the enhanced image
        img_enhanced.save('enhanced_image.jpg')

# Assuming 'your_image.jpg' is the image you want to enhance
enhance_image('your_image.jpg')