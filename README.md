# AI Curl Counter

AI Curl Counter is a small Python computer-vision demo that processes a video, detects a person's pose, and counts left-arm bicep curl repetitions. The processed video displays the curl progress and repetition count.

## Features

- Detects pose landmarks with MediaPipe Pose.
- Tracks the left shoulder, elbow, and wrist to estimate the elbow angle.
- Counts a repetition as the arm moves between the extended and curled positions.
- Includes a sample video for trying the demo without a camera.

## Getting started

### Requirements

- Python 3
- A desktop environment that supports OpenCV video windows

### Set up

Open a terminal in the project directory and create a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the packages imported by the project:

```powershell
python -m pip install opencv-python mediapipe numpy matplotlib
```

### Run the demo

Run the script from the project directory so it can locate the bundled video:

```powershell
python AI_trainer.py
```

The OpenCV window shows the video, a curl-progress bar, and the repetition count. The count is displayed as a whole number; internally, each completed curl adds two half-repetitions.

The input file is currently set to `Blueshirt.mp4` in `AI_trainer.py`. The video path is relative to the current working directory, and there is no command-line option for selecting another video or a webcam.

## Project files

- [AI_trainer.py](AI_trainer.py) — video processing loop and repetition counter.
- [Module.py](Module.py) — MediaPipe pose detection, landmark extraction, and joint-angle calculation.
- [Blueshirt.mp4](Blueshirt.mp4) — default input video.
- [Image.jpg](Image.jpg) — image asset; not used by the default run.

## Limitations

This is a demonstration rather than a general-purpose workout tracker. It uses fixed elbow-angle thresholds and tracks only the left arm. The video loop does not currently handle the end of the input video or frames where no pose is detected gracefully, so the sample may not finish cleanly.

## Help and support

There is no separate documentation or support channel in the project. For questions or bug reports, open an issue in the repository where you obtained the project.

## Maintainers and contributions

No maintainer details or contribution guide are included in the project. Contributions can be proposed through an issue or pull request in the hosting repository. Keep changes focused and include steps to reproduce or verify behavior where applicable.

## License

No `LICENSE` file is included. Check with the repository owner before redistributing or reusing this project.
