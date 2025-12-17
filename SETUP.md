# Dr. Strange Shields - Setup Guide

## Prerequisites

### Virtual Camera Setup (Required for Virtual Camera Output)

The project supports virtual camera output to stream shields to applications like Discord, OBS, Zoom, etc. To use this feature, you need to install one of the following:

#### Option 1: OBS Virtual Camera (Windows)

1. Download and install [OBS Studio](https://obsproject.com/download)
2. Go to **Tools → Start Virtual Camera**
3. The virtual camera will be available as a device in applications

#### Option 2: Unity Capture (Windows)

1. Download [Unity Capture](https://github.com/schellingb/UnityCapture/releases)
2. Run the installer
3. Register a camera through the application

### Windows Camera Access

Ensure your camera has permission to be accessed by Python/OpenCV on Windows.

## Installation

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **(Optional) For virtual camera support:**
   - Install OBS Studio or Unity Capture (see Prerequisites above)

## Running the Project

### Basic Usage (Window Output Only)

```bash
python shield.py --output window
```

### With Virtual Camera

```bash
python shield.py --output virtual
```

### With Both Outputs

```bash
python shield.py --output both
```

### Advanced Options

```bash
python shield.py \
  --camera_id 0 \
  --model models/model_svm.sav \
  --threshold 0.9 \
  --det_conf 0.5 \
  --trk_conf 0.5 \
  --shield effects/shield.mp4 \
  --output both
```

**Parameters:**

- `--camera_id`: Camera device ID (default: 0)
- `--model`: Path to SVM model (default: models/model_svm.sav)
- `--threshold`: Prediction confidence threshold (default: 0.9)
- `--det_conf`: Hand detection confidence (default: 0.5)
- `--trk_conf`: Hand tracking confidence (default: 0.5)
- `--shield`: Shield effect video file (default: effects/shield.mp4)
- `--output`: Output mode - 'window', 'virtual', or 'both' (default: both)

## Gesture Sequence

The shields activate in the following sequence:

1. **KEY_1** - First gesture
2. **KEY_2** - Second gesture (within 2 seconds of KEY_1)
3. **KEY_3** - Third gesture (within 2 seconds of KEY_2)
4. **KEY_4** - Deactivate shields

## Exit

- Press **'q'** in the OpenCV window (if enabled)
- Press **Ctrl+C** in the terminal

## Troubleshooting

### ModuleNotFoundError: No module named 'mediapipe'

```bash
pip install mediapipe==0.10.21
```

### Virtual Camera Not Found

Make sure OBS Virtual Camera or Unity Capture is properly installed and running.

### Camera Not Detected

- Check camera permissions on Windows
- Try a different camera_id (0, 1, 2, etc.)

### Inconsistent Gesture Recognition

Adjust confidence thresholds using:

- `--threshold`: Gesture prediction confidence (increase for stricter matching)
- `--det_conf`: Hand detection confidence (decrease if hands aren't detected)

## Project Structure

- `shield.py` - Main gesture recognition and shield rendering application
- `utils.py` - Utility functions for hand detection and processing
- `train_svm.py` - SVM model training script
- `dataset_collection.py` - Dataset collection tool
- `models/` - Pre-trained SVM models
- `effects/` - Shield animation videos
- `data/` - Hand position data
