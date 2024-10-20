
# VidCropper

VidCropper is a simple video cropping application that allows users to crop the uploaded video from the top, bottom, left, and right and export the cropped video. This tool is designed to provide an easy-to-use interface for quickly adjusting the visible area of any video.

## Features

- Upload video files of various formats.
- Crop the video by specifying the number of pixels to remove from each side (top, bottom, left, and right).
- Preview the cropped area before exporting.
- Export the cropped video in a desired format while maintaining the original quality.
  
## Technologies Used

- **Python**: Backend processing of video files.
- **Streamlit**: User interface to upload videos and specify cropping parameters.
- **MoviePy**: Handling the video processing, cropping, and export functionalities.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/AKSHTMISHRA/VidCropper.git
    ```
   
2. Navigate to the project directory:
    ```bash
    cd VidCropper
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Upload a video file using the provided file upload field.

3. Specify the number of pixels to crop from the top, bottom, left, and right sides.

4. Click on the **Crop** button to preview the cropped video.

5. Export the cropped video by clicking the **Export** button.

## Project Structure

```
VidCropper/
│
├── .streamlit
|    ├── config.toml           # Streamlit configuration file
├── app.py                   # Main Streamlit application file
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## Future Improvements

- Add support for different video export formats.
- Enhance the UI/UX for a smoother video cropping experience.
- Optimize the video processing for faster export times.
  
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
