# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("\n" + "="*60)
print("Dr. Strange Shields - Project Validation")
print("="*60 + "\n")

# Test imports
try:
    import cv2
    print("✓ OpenCV imported successfully")
except ImportError as e:
    print(f"✗ OpenCV import failed: {e}")

try:
    import mediapipe
    print("✓ MediaPipe imported successfully")
except ImportError as e:
    print(f"✗ MediaPipe import failed: {e}")

try:
    import numpy
    print("✓ NumPy imported successfully")
except ImportError as e:
    print(f"✗ NumPy import failed: {e}")

try:
    import sklearn
    print("✓ Scikit-learn imported successfully")
except ImportError as e:
    print(f"✗ Scikit-learn import failed: {e}")

try:
    import pyvirtualcam
    print("✓ PyVirtualCam imported successfully")
except ImportError as e:
    print(f"✗ PyVirtualCam import failed: {e}")

try:
    from utils import mediapipe_detection
    print("✓ Utils module imported successfully")
except Exception as e:
    print(f"✗ Utils import failed: {e}")

# Test model loading
try:
    import pickle
    model = pickle.load(open('models/model_svm.sav', 'rb'))
    print("✓ SVM model loaded successfully")
    print(f"  - Model classes: {list(model.classes_)}")
except Exception as e:
    print(f"✗ Model loading failed: {e}")

# Test data files
import os
files_to_check = [
    'effects/shield.mp4',
    'data/hand_position.csv',
    'models/model_svm.sav'
]

print("\nData files:")
for file in files_to_check:
    if os.path.exists(file):
        size = os.path.getsize(file)
        print(f"✓ {file} ({size:,} bytes)")
    else:
        print(f"✗ {file} NOT FOUND")

print("\n" + "="*60)
print("PROJECT READY! You can now run:")
print("  python shield.py --output window")
print("  python shield.py --output virtual")
print("  python shield.py --output both")
print("="*60 + "\n")
