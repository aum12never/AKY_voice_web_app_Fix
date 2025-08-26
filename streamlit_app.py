# File: streamlit_app.py (Final Version)
# -*- coding: utf-8 -*-
import streamlit as st
import os

try:
    from backend.aky_voice_backend import run_tts_generation
except ImportError:
    st.error("ไม่สามารถโหลด Backend ได้ กรุณาตรวจสอบไฟล์ backend/aky_voice_backend.py")
    st.stop()

def check_password():
    def password_entered():
        if st.session_state["password"] == st.secrets.get("APP_PASSWORD", ""):
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        st.error("😕 Password incorrect")
        return False
    else:
        return True

st.set_page_config(page_title="Affiliate Voice Generator", layout="wide")
st.title("🎙️ Affiliate Voice Generator Pro")
st.write("---")

if check_password():
    try:
        api_key = st.secrets["GOOGLE_API_KEY"]
    except KeyError:
        st.error("❌ ไม่พบ GOOGLE_API_KEY ในการตั้งค่า Secrets!")
        st.stop()

    with st.container(border=True):
        st.subheader("1. ใส่สคริปต์และคำสั่ง")
        col1, col2 = st.columns(2)
        with col1:
            style_instructions = st.text_area("Style Instructions:", height=250, placeholder="ตัวอย่าง: พูดด้วยน้ำเสียงตื่นเต้น สดใส มีพลัง...")
        with col2:
            main_text = st.text_area("Main Text (Script):", height=250, placeholder="ใส่สคริปต์หลักของคุณที่นี่...")

    with st.container(border=True):
        st.subheader("2. ตั้งค่าเสียงและไฟล์")
        col3, col4 = st.columns(2)
        with col3:
            gemini_voices_data = {"Zephyr": "Bright", "Puck": "Upbeat", "Charon": "Informative", "Kore": "Firm", "Fenrir": "Excitable", "Leda": "Youthful", "Orus": "Firm", "Aoede": "Breezy", "Callirrhoe": "Easy-going", "Autonoe": "Bright", "Enceladus": "Breathy", "Iapetus": "Clear", "Umbriel": "Easy-going", "Algieba": "Smooth", "Despina": "Smooth", "Erinome": "Clear", "Algenib": "Gravelly", "Rasalgethi": "Informative", "Laomedeia": "Upbeat", "Achernar": "Soft", "Alnilam": "Firm", "Schedar": "Even", "Gacrux": "Mature", "Pulcherrima": "Forward", "Achird": "Friendly", "Zubenelgenubi": "Casual", "Vindemiatrix": "Gentle", "Sadachbia": "Lively", "Sadaltager": "Knowledgeable", "Sulafat": "Warm"}
            voice_display_list = sorted([f"{name} - {desc}" for name, desc in gemini_voices_data.items()])
            selected_voice_display = st.selectbox("เลือกเสียงพากย์:", options=voice_display_list, index=20)
            temperature = st.slider("Temperature:", min_value=0.0, max_value=2.0, value=0.9, step=0.1)
        with col4:
            output_filename = st.text_input("ตั้งชื่อไฟล์ (ไม่ต้องใส่นามสกุล .mp3):", value="my_voiceover")

    st.write("---")

    if st.button("🚀 สร้างไฟล์เสียง (Generate Audio)", type="primary", use_container_width=True):
        if not main_text:
            st.warning("กรุณาใส่สคริปต์ในช่อง Main Text ก่อนครับ")
        else:
            with st.spinner("⏳ กำลังสร้างไฟล์เสียง..."):
                try:
                    voice_name_for_api = selected_voice_display.split(' - ')[0]
                    temp_output_folder = "temp_output"
                    final_mp3_path = run_tts_generation(
                        api_key=api_key,
                        style_instructions=style_instructions,
                        main_text=main_text,
                        voice_name=voice_name_for_api,
                        output_folder=temp_output_folder,
                        output_filename=output_filename,
                        temperature=temperature,
                        ffmpeg_path="ffmpeg"
                    )
                    st.success("🎉 สร้างไฟล์เสียงสำเร็จ!")
                    st.audio(final_mp3_path, format='audio/mp3')
                    with open(final_mp3_path, "rb") as file:
                        st.download_button("📥 ดาวน์โหลดไฟล์ MP3", data=file, file_name=os.path.basename(final_mp3_path), mime="audio/mp3", use_container_width=True)
                except Exception as e:
                    st.error(f"{e}")
