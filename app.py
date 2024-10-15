import streamlit as st
from moviepy.editor import VideoFileClip
import tempfile
import os

# Function to load the video
def load_video(file):
    temp_video_path = os.path.join(tempfile.gettempdir(), file.name)
    with open(temp_video_path, 'wb') as f:
        f.write(file.read())
    return VideoFileClip(temp_video_path), temp_video_path

# Function to crop the video based on user input
def crop_video(video, top, bottom, left, right):
    width, height = video.size
    cropped_video = video.crop(x1=left, x2=width-right, y1=top, y2=height-bottom)
    return cropped_video

# Streamlit app
st.title("Video Cropper App")

# Upload video
uploaded_video = st.file_uploader("Upload a video", type=None)  # Allow all file types

if uploaded_video:
    # Load the video using the load_video function
    video, video_path = load_video(uploaded_video)
    
    st.video(video_path)  # Show the uploaded video

    st.subheader("Enter the number of pixels to crop:")
    # Input fields for crop dimensions
    crop_top = st.number_input("Crop from top (in pixels)", min_value=0, max_value=video.size[1], value=0)
    crop_bottom = st.number_input("Crop from bottom (in pixels)", min_value=0, max_value=video.size[1], value=0)
    crop_left = st.number_input("Crop from left (in pixels)", min_value=0, max_value=video.size[0], value=0)
    crop_right = st.number_input("Crop from right (in pixels)", min_value=0, max_value=video.size[0], value=0)

    # Real-time video preview based on user input
    if crop_top > 0 or crop_bottom > 0 or crop_left > 0 or crop_right > 0:
        cropped_video = crop_video(video, crop_top, crop_bottom, crop_left, crop_right)
        
        # --- CHANGED HERE ---
        # Save the cropped video with reduced quality for real-time preview
        preview_tempfile = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False)
        cropped_video.write_videofile(
            preview_tempfile.name, 
            codec="libx264", 
            bitrate="500k",  # Lower bitrate for faster preview
            preset="fast",  # Fast rendering for preview
            ffmpeg_params=["-vf", "scale=iw/2:ih/2"]  # Reduce resolution by half for preview
        )

        st.video(preview_tempfile.name)

    if st.button("Finalize Cropping and Download"):
        cropped_video = crop_video(video, crop_top, crop_bottom, crop_left, crop_right)
        
        # --- CHANGED HERE ---
        # Export the final cropped video with original quality settings
        final_tempfile = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False)
        cropped_video.write_videofile(
            final_tempfile.name, 
            codec="libx264",  # Preserve the original codec
            preset="slow",    # Slow rendering for best quality
            ffmpeg_params=["-crf", "0"]  # CRF 0 means no quality loss
        )
        
        st.success("Video cropped and exported successfully!")

        # Provide option to export/download the cropped video
        with open(final_tempfile.name, 'rb') as f:
            st.download_button("Download Cropped Video", f, file_name="cropped_video.mp4")

    st.text(f"Original Video Dimensions: {video.size[0]}x{video.size[1]} (Width x Height)")
