from setuptools import setup, find_packages

setup(
    name='pubgapi',  # 패키지 이름
    version='0.1',  # 패키지 버전
    packages=find_packages(),  # 패키지 자동 탐색
    install_requires=[  # 필요한 외부 라이브러리
        # 예: 'requests', 'numpy' 등
    ],
    author='ThrypsisJ',
    author_email='gjzprdl@gmail.com',
    description='Wrapper package to use PUBG API',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ThrypsisJ/pubgapi',  # 프로젝트 URL (선택)
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # 필요한 파이썬 버전
)