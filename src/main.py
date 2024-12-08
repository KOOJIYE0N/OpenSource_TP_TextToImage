import argparse
from text_to_image.generating_image import TextToImageGenerator
from post_processing.enhance_image import ImageEnhancer

def main():
    parser = argparse.ArgumentParser(description="AI 기반 디지털 아트 생성 및 변환 도구")
    
    parser.add_argument("--step", type=str, required=True, choices=["text_to_image", "post_processing", "full_workflow"],
                        help="실행할 작업 단계 선택: 'text_to_image', 'post_processing', 'full_workflow'")
    parser.add_argument("--prompt", type=str, help="텍스트에서 이미지를 생성하기 위한 프롬프트 (text_to_image 및 full_workflow에서 필요)")
    parser.add_argument("--input_path", type=str, help="후처리할 입력 이미지 경로 (post_processing에서 필요)")
    parser.add_argument("--output_path", type=str, default="output.png", help="결과 이미지를 저장할 경로")
    parser.add_argument("--height", type=int, default=512, help="생성할 이미지의 높이 (기본값: 512)")
    parser.add_argument("--width", type=int, default=512, help="생성할 이미지의 너비 (기본값: 512)")
    parser.add_argument("--enhance_type", type=str, choices=["contrast", "sharpness", "brightness"], default="contrast",
                        help="이미지 후처리 방식 선택: 'contrast', 'sharpness', 'brightness'")
    parser.add_argument("--enhance_factor", type=float, default=1.5, help="후처리 강화 계수 (기본값: 1.5)")

    args = parser.parse_args()
  
    else:
        print("Invalid step selected. Please choose a valid step: 'text_to_image', 'post_processing', or 'full_workflow'.")

if __name__ == "__main__":
    main()
