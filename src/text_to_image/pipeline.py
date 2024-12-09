from .generating_image import TextToImageGenerator

class TextToImagePipeline:
    """
    텍스트 프롬프트를 기반으로 이미지를 생성하는 파이프라인 클래스
    Stable Diffusion 모델을 사용하여 텍스트 입력을 이미지로 변환하는 작업 수향
    """

    def __init__(self, model_name="runwayml/stable-diffusion-v1-5"):
        """
        Text-to-Image 파이프라인 초기화 메서드

        Args:
            model_name (str): 사용할 Stable Diffusion 모델의 이름 (기본값: "runwayml/stable-diffusion-v1-5").
        """
        # 텍스트 입력을 이미지로 변환할 생성기 초기화
        self.generator = TextToImageGenerator(model_name)
        print(f"[INFO] {model_name} 모델로 파이프라인 초기화 완료.")

    def run_pipeline(self, prompt, output_path="final_output.png", height=512, width=512, guidance_scale=7.5):
        """
        텍스트 입력을 기반으로 이미지를 생성하는 전체 파이프라인 실행 메서드

        Args:
            prompt (str): 이미지 생성을 위한 텍스트 입력.
            output_path (str): 생성된 이미지를 저장할 경로 (기본값: "final_output.png").
            height (int): 생성할 이미지의 세로 크기 (기본값: 512).
            width (int): 생성할 이미지의 가로 크기 (기본값: 512).
            guidance_scale (float): 이미지 품질을 조정하는 값 (기본값: 7.5).

        Returns:
            str: 최종 생성된 이미지의 파일 경로

        Example:
            >>> pipeline = TextToImagePipeline()
            >>> result_path = pipeline.run_pipeline(
            >>>     prompt="A futuristic city at sunset",
            >>>     output_path="output.png"
            >>> )
            >>> print(f"Generated image saved at: {result_path}")
        """
        print(f"[INFO] 텍스트 프롬프트 '{prompt}' 에 대한 이미지 생성 시작...")
        
        # 텍스트 기반 이미지 생성
        image_path = self.generator.generate(
            prompt=prompt,
            output_path=output_path,
            height=height,
            width=width,
            guidance_scale=guidance_scale,
        )

        print(f"[INFO] 파이프라인 작업이 성공적으로 완료되었습니다!")
        return image_path
