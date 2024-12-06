from text_to_image.generating_image import TextToImageGenerator
from post_processing.enhance_image import ImageEnhancer

def example_workflow():
    """
    Example workflow for generating and enhancing an image.
    """
    # Step 1: Text-to-Image Generation
    text_prompt = "A serene forest with sunlight filtering through the trees"
    generator = TextToImageGenerator()
    generated_image = generator.generate(
        prompt=text_prompt,
        output_path="generated_image.png",
        height=512,
        width=512
    )

    # Step 2: Image Post-Processing
    enhancer = ImageEnhancer(input_path=generated_image)
    enhanced_image = enhancer.enhance_contrast(
        output_path="final_image.png",
        factor=1.5
    )

    print("Example workflow completed successfully.")
    print(f"Final enhanced image saved as 'final_image.png'.")

if __name__ == "__main__":
    example_workflow()
