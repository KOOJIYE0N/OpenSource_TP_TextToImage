from diffusers import StableDiffusionPipeline
import torch

class TextToImageGenerator:
    """
    텍스트 프롬프트를 기반으로 이미지를 생성하는 클래스
    Stable Diffusion 모델을 사용하여 텍스트 입력을 이미지로 변환
    """

    def __init__(self, model_name="runwayml/stable-diffusion-v1-5", device=None):
        """
        생성자 메서드로 모델 초기화.

        Args:
            model_name (str): 사용할 Stable Diffusion 모델 이름 (기본값: "runwayml/stable-diffusion-v1-5").
            device (str): 사용할 장치 ('cuda' 또는 'cpu'). None이면 자동으로 설정.
        """
        # 사용할 장치 자동 감지
        self.device = device if device else ("cuda" if torch.cuda.is_available() else "cpu")
        
        # Stable Diffusion 모델 로딩 및 장치 설정
        self.pipe = StableDiffusionPipeline.from_pretrained(model_name)
        self.pipe.to(self.device)
        print(f"[INFO] 모델이 {self.device}에서 초기화되었습니다.")

    def generate(self, prompt, output_path="output.png", height=512, width=512, guidance_scale=7.5):
        """
        텍스트 입력을 기반으로 이미지를 생성합니다.

        Args:
            prompt (str): 이미지 생성에 사용할 텍스트 입력.
            output_path (str): 생성된 이미지를 저장할 경로 (기본값: "output.png").
            height (int): 생성할 이미지의 세로 크기 (기본값: 512).
            width (int): 생성할 이미지의 가로 크기 (기본값: 512).
            guidance_scale (float): 생성 품질을 조정하는 값 (기본값: 7.5).

        Returns:
            str: 생성된 이미지의 파일 경로.

        Example:
            generator = TextToImageGenerator()
            generator.generate("A serene forest with sunlight filtering through the trees")
        """
        print(f"[INFO] '{prompt}'에 대한 이미지 생성 중...")
        
        # 텍스트 기반 이미지 생성
        image = self.pipe(
            prompt, 
            height=height, 
            width=width, 
            guidance_scale=guidance_scale
        ).images[0]

        # 생성된 이미지 저장
        image.save(output_path)
        print(f"[INFO] 이미지가 {output_path}에 저장되었습니다.")
        return output_path
