from text_to_image.generating_image import TextToImageGenerator
from post_processing.enhance_image import ImageEnhancer

def generate_image(prompt, output_path="generated_image.png", height=512, width=512):
    """
    Generate an image based on a text prompt.

    Args:
        prompt (str): The text prompt to guide image generation.
        output_path (str): Path to save the generated image.
        height (int): Height of the generated image.
        width (int): Width of the generated image.

    Returns:
        str: The path to the generated image.
    """
    print(f"Generating image for prompt: '{prompt}'...")
    generator = TextToImageGenerator()
    generated_image_path = generator.generate(
        prompt=prompt,
        output_path=output_path,
        height=height,
        width=width
    )
    print(f"Image successfully generated and saved to: {generated_image_path}")
    return generated_image_path


def enhance_image(input_path, output_path="final_image.png", contrast_factor=1.5):
    """
    Enhance the contrast of an image.

    Args:
        input_path (str): Path to the input image.
        output_path (str): Path to save the enhanced image.
        contrast_factor (float): Factor to adjust image contrast.

    Returns:
        str: The path to the enhanced image.
    """
    print(f"Enhancing contrast for image: {input_path} with factor: {contrast_factor}...")
    enhancer = ImageEnhancer(input_path=input_path)
    enhanced_image_path = enhancer.enhance_contrast(
        output_path=output_path,
        factor=contrast_factor
    )
    print(f"Enhanced image saved to: {enhanced_image_path}")
    return enhanced_image_path


def example_workflow():
    """
    Example workflow for generating an image from a text prompt
    and enhancing it with post-processing.
    """
    text_prompt = "A serene forest with sunlight filtering through the trees"
    print("\n--- Starting Example Workflow ---\n")

    # Step 1: Generate Image
    generated_image_path = generate_image(prompt=text_prompt)

    # Step 2: Enhance Image
    enhanced_image_path = enhance_image(input_path=generated_image_path)

    print("\n--- Workflow Completed Successfully ---")
    print(f"Final enhanced image available at: {enhanced_image_path}")


if __name__ == "__main__":
    example_workflow()
