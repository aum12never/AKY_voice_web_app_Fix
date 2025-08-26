# File: aky_voice_backend.py (The truly final, simplified version)
# -*- coding: utf-8 -*-
import os
import google.generativeai as genai

def run_tts_generation(
    api_key: str, style_instructions: str, main_text: str, voice_name: str,
    output_folder: str, output_filename: str, temperature: float,
    ffmpeg_path: str
):
    """
    ฟังก์ชันหลักที่ใช้ API text_to_speech ที่ทันสมัยและเรียบง่าย
    """
    try:
        genai.configure(api_key=api_key)

        full_prompt = f"{style_instructions}. {main_text}"

        response = genai.text_to_speech(
            text=full_prompt,
            voice_name=voice_name,
        )
        
        audio_buffer = response.audio_data

        if audio_buffer:
            _, mp3_path = determine_output_paths(output_folder, output_filename)
            save_binary_file(mp3_path, audio_buffer)
            return mp3_path
        else:
            raise ValueError("No audio data received from the API.")

    except Exception as e:
        raise ValueError(f"Backend Error: {e}")

def determine_output_paths(folder, filename_base):
    os.makedirs(folder, exist_ok=True)
    mp3_folder = folder
    mp3_base_path = os.path.join(mp3_folder, filename_base)
    mp3_output = f"{mp3_base_path}.mp3"
    counter = 1
    
    while os.path.exists(mp3_output):
        mp3_output = f"{mp3_base_path} ({counter}).mp3"
        counter += 1
    
    return mp3_output, mp3_output

def save_binary_file(file_name, data):
    with open(file_name, "wb") as f:
        f.write(data)
