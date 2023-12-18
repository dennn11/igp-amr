import picamera
import cv2

class RaspberryPiCamera:
    def __init__(self, resolution=(1280, 720), framerate=30):
        """
        Initialize the Raspberry Pi camera with specified resolution and framerate.

        Args:
            resolution (tuple): Resolution of the captured image/video (width, height).
            framerate (int): Frames per second for video capture.
        """
        self.camera = picamera.PiCamera(resolution=resolution, framerate=framerate)

    def capture_image(self, filename="image.jpg"):
        """
        Capture an image and save it to the specified filename.

        Args:
            filename (str): Path and filename to save the captured image.
        """
        self.camera.capture(filename)

    def start_recording(self, filename="video.h264"):
        """
        Start recording a video and save it to the specified filename.

        Args:
            filename (str): Path and filename to save the captured video.
        """
        self.camera.start_recording(filename)

    def stop_recording(self):
        """
        Stop recording the video.
        """
        self.camera.stop_recording()

    def adjust_camera_settings(self, **kwargs):
        """
        Adjust camera settings like ISO, contrast, saturation, etc.

        Args:
            **kwargs: Key-value pairs of camera settings and their values to adjust.
        """
        for key, value in kwargs.items():
            self.camera.brightness = value if key == "brightness" else getattr(self.camera, key, value)

    def preview_stream(self, window_name="Raspberry Pi Camera Stream"):
        """
        Preview the camera stream in a named window.

        Args:
            window_name (str): Name of the window displaying the camera stream.
        """
        cv2.namedWindow(window_name)
        while True:
            frame = self.camera.capture_continuous(format="bgr", use_video_port=True)
            frame = next(frame.frames)
            cv2.imshow(window_name, frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        cv2.destroyAllWindows()

    def close_camera(self):
        """
        Release resources and close the camera.
        """
        self.camera.close()
