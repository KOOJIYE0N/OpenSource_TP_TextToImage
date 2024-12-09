<h1 align="center">🌟 AI 기반 디지털 아트 생성 및 후처리 도구 🌟</h1>

<p align="center">안녕하세요!🙇‍♂️<br/>가천대학교 2024-2학기 OpenSource Termproject Team 입니다!👋<br/>이 프로젝트는 텍스트 프롬프트를 기반으로 Stable Diffusion을 활용해 이미지를 생성하고, 생성된 이미지에 후처리를 적용하는 AI 기반 디지털 아트 생성 오픈소스 입니다.</p>

<br/>

<p align="center">
<img width="500" alt="image" src="https://github.com/user-attachments/assets/5313f604-edd6-438d-9f25-be533c096a35">
</p>
<p align="center">The result of the prompt ‘A cute panda is eating a lot of bamboo.’</p>

<br/><br/>

## 주요 기능

1. **텍스트에서 이미지 생성**:
   - 사용자의 텍스트 프롬프트를 기반으로 Stable Diffusion 모델을 활용하여 이미지를 생성합니다.

2. **이미지 후처리**:
   - 생성된 이미지에 대비, 선명도, 밝기 조정과 같은 후처리를 적용합니다.

<br/><br/>

## 설치 방법

### 1. 가상환경 설정 (선택 사항)
```bash
python -m venv venv
source venv/bin/activate  # Windows에서는 venv\Scripts\activate
```

### 2. 필수 패키지 설치
```bash
pip install -r requirements.txt
```
<br/>

<br/>

## 사용법

1. **텍스트에서 이미지 생성**:
```bash
python src/main.py --step text_to_image --prompt "A serene forest with sunlight filtering through the trees" --output_path generated_image.png
```
2. **이미지 후처리**:
```bash
python src/main.py --step post_processing --input_path generated_image.png --enhance_type contrast --enhance_factor 1.5 --output_path enhanced_image.png
```
3. **전체 워크플로 실행**:
```bash
python src/main.py --step full_workflow --prompt "A futuristic city at night" --output_path final_image.png
```
