import argparse
from text_to_image.generating_image import TextToImageGenerator
from post_processing.enhance_image import ImageEnhancer

def main():
    # Argument parser setup
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

    # Step-based execution
    if args.step == "text_to_image":
        if not args.prompt:
            raise ValueError("텍스트에서 이미지를 생성하려면 '--prompt' 매개변수를 제공해야 합니다.")
        
        print(f"Generating image from text prompt: {args.prompt}")
        generator = TextToImageGenerator()
        generated_image_path = generator.generate(
            prompt=args.prompt,
            output_path=args.output_path,
            height=args.height,
            width=args.width
        )
        print(f"Image generated and saved at: {generated_image_path}")

    elif args.step == "post_processing":
        if not args.input_path:
            raise ValueError("후처리를 수행하려면 '--input_path' 매개변수를 제공해야 합니다.")
        
        print(f"Enhancing image at: {args.input_path}")
        enhancer = ImageEnhancer(input_path=args.input_path)
        
        if args.enhance_type == "contrast":
            enhanced_image_path = enhancer.enhance_contrast(output_path=args.output_path, factor=args.enhance_factor)
        elif args.enhance_type == "sharpness":
            enhanced_image_path = enhancer.enhance_sharpness(output_path=args.output_path, factor=args.enhance_factor)
        elif args.enhance_type == "brightness":
            enhanced_image_path = enhancer.enhance_brightness(output_path=args.output_path, factor=args.enhance_factor)
        
        print(f"Enhanced image saved at: {enhanced_image_path}")

    elif args.step == "full_workflow":
        if not args.prompt:
            raise ValueError("전체 워크플로를 실행하려면 '--prompt' 매개변수를 제공해야 합니다.")
        
        print(f"Running full workflow with prompt: {args.prompt}")
        
        # Step 1: Text-to-Image Generation
        generator = TextToImageGenerator()
        generated_image_path = generator.generate(
            prompt=args.prompt,
            output_path="generated_image.png",
            height=args.height,
            width=args.width
        )
        print(f"Image generated and saved at: {generated_image_path}")
        
        # Step 2: Post-Processing
        enhancer = ImageEnhancer(input_path=generated_image_path)
        enhanced_image_path = enhancer.enhance_contrast(output_path=args.output_path, factor=args.enhance_factor)
        print(f"Final enhanced image saved at: {enhanced_image_path}")
    else:
        print("Invalid step selected. Please choose a valid step: 'text_to_image', 'post_processing', or 'full_workflow'.")

if __name__ == "__main__":
    main()
