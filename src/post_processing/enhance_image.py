from PIL import Image, ImageEnhance

class ImageEnhancer:
    def __init__(self, input_path):
        """
        이미지 후처리 클래스 초기화.
        :param input_path: 입력 이미지 경로.
        """
        self.image = Image.open(input_path)
        self.input_path = input_path

    def enhance_contrast(self, output_path="enhanced_contrast.png", factor=1.5):
        """
        이미지의 대비 향상
        :param output_path: 결과 이미지 저장 경로.
        :param factor: 대비 향상 정도 (Default: 1.5).
        :return: 결과 이미지 경로.
        """
        enhancer = ImageEnhance.Contrast(self.image)
        enhanced_image = enhancer.enhance(factor)
        enhanced_image.save(output_path)
        print(f"Contrast enhanced by factor {factor}. Saved to {output_path}")
        return output_path

    def enhance_sharpness(self, output_path="enhanced_sharpness.png", factor=2.0):
        """
        이미지의 선명도 향상
        :param output_path: 결과 이미지 저장 경로.
        :param factor: 선명도 향상 정도 (Default: 2.0).
        :return: 결과 이미지 경로.
        """
        enhancer = ImageEnhance.Sharpness(self.image)
        enhanced_image = enhancer.enhance(factor)
        enhanced_image.save(output_path)
        print(f"Sharpness enhanced by factor {factor}. Saved to {output_path}")
        return output_path

    def enhance_brightness(self, output_path="enhanced_brightness.png", factor=1.2):
        """
        이미지의 밝기 향상
        :param output_path: 결과 이미지 저장 경로.
        :param factor: 밝기 향상 정도 (Default: 1.2).
        :return: 결과 이미지 경로.
        """
        enhancer = ImageEnhance.Brightness(self.image)
        enhanced_image = enhancer.enhance(factor)
        enhanced_image.save(output_path)
        print(f"Brightness enhanced by factor {factor}. Saved to {output_path}")
        return output_path