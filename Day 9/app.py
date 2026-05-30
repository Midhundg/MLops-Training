import cv2
import os

project_path = "/Users/midhundg/Downloads/Project/Air Quality Proxy via Smoke Plume Detection"

video_folder = os.path.join(project_path, "Videos")
frames_folder = os.path.join(project_path, "frames")

os.makedirs(frames_folder, exist_ok=True)

videos = sorted([
    v for v in os.listdir(video_folder)
    if v.endswith((".mp4", ".mkv", ".avi", ".mov"))
])

for idx, video_name in enumerate(videos, start=1):

    print(f"\nProcessing {video_name}")

    video_path = os.path.join(video_folder, video_name)

    output_folder = os.path.join(frames_folder, f"frames{idx}")
    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Cannot open {video_name}")
        continue

    framerate = int(cap.get(cv2.CAP_PROP_FPS))

    framecount = 0
    count = 0

    while True:

        success, frame = cap.read()

        if not success:
            break

        frame = cv2.resize(frame, (1280, 720))

        framecount += 1

        if framecount >= (framerate // 10):

            framecount = 0

            frame_name = os.path.join(
                output_folder,
                f"{video_name.split('.')[0]}_{count}.jpg"
            )

            cv2.imwrite(frame_name, frame)

            print(f"Saved: {frame_name}")

            count += 1

    cap.release()

    print(f"{video_name} completed")

cv2.destroyAllWindows()

print("\nAll videos converted successfully")