# File: aky_voice_backend.py

# -*- coding: utf-8 -*-

import os

import struct

import subprocess

from google import genai

from google.genai import types

from tqdm import tqdm





def run_tts_generation(

    api_key: str, style_instructions: str, main_text: str, voice_name: str,

    output_folder: str, output_filename: str, temperature: float,

    ffmpeg_path: str,  # <-- [เพิ่ม] รับตำแหน่ง ffmpeg เข้ามา

    status_callback=print

):

    """ฟังก์ชันหลักที่จะรับการตั้งค่าทั้งหมดเข้ามา และส่งสถานะกลับผ่าน callback"""

    try:

        status_callback("🚀 Starting audio generation process...")

        if not api_key:

            raise ValueError("API Key is missing.")



        client = genai.Client(api_key=api_key)

        contents = prepare_prompt(style_instructions, main_text)

        config = prepare_api_config(temperature, voice_name)

        wav_path, mp3_path = determine_output_paths(

            output_folder, output_filename)



        status_callback(f"Final MP3 will be saved to: {mp3_path}")



        stream = client.models.generate_content_stream(

            model="gemini-2.5-pro-preview-tts", contents=contents, config=config

        )



        audio_buffer = b''

        for chunk in tqdm(stream, desc="Receiving audio chunks"):

            if chunk.candidates and chunk.candidates[0].content.parts[0].inline_data:

                audio_buffer += chunk.candidates[0].content.parts[0].inline_data.data



        if audio_buffer:

            final_wav_data = convert_to_wav(

                audio_buffer, "audio/L16;rate=24000")

            save_binary_file(wav_path, final_wav_data, status_callback)



            # [แก้ไข] ส่งตำแหน่ง ffmpeg ไปให้ฟังก์ชันแปลงไฟล์

            convert_with_ffmpeg(ffmpeg_path, wav_path,

                                mp3_path, status_callback)



            os.remove(wav_path)

            status_callback(

                f"🗑️ Temporary WAV file '{os.path.basename(wav_path)}' deleted.")

            status_callback("✨ Generation process complete!")

        else:

            status_callback("❌ No audio data received from the API.")



    except Exception as e:

        status_callback(f"❌ An error occurred: {e}")



# (ฟังก์ชัน Helper อื่นๆ ทั้งหมดยังคงเหมือนเดิม ยกเว้น convert_with_ffmpeg)





def convert_with_ffmpeg(ffmpeg_path, wav_path, mp3_path, status_callback=print):

    """แปลงไฟล์ .wav เป็น .mp3 โดยใช้ ffmpeg.exe จากตำแหน่งที่ระบุ"""

    status_callback(f"🎶 Converting {os.path.basename(wav_path)} to MP3...")

    try:

        if not os.path.exists(ffmpeg_path):

            status_callback(

                "❌ FFMPEG ERROR: 'ffmpeg.exe' not found at the specified path.")

            return



        # [แก้ไข] ใช้ตำแหน่งแบบเต็ม (absolute path) ที่ได้รับมา

        command = [ffmpeg_path, '-i', wav_path, '-y',

                   '-acodec', 'libmp3lame', '-q:a', '2', mp3_path]

        subprocess.run(command, check=True,

                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        status_callback(f"✅ MP3 file saved successfully to: {mp3_path}")

    except Exception as e:

        status_callback(f"❌ An error occurred during FFMPEG conversion: {e}")



# ... (ฟังก์ชันที่เหลือทั้งหมดเหมือนเดิมทุกประการ)





def prepare_prompt(style, text):

    return [types.Content(role="user", parts=[types.Part.from_text(text=style), types.Part.from_text(text=text)])]





def prepare_api_config(temp, voice):

    return types.GenerateContentConfig(temperature=temp, response_modalities=["audio"], speech_config=types.SpeechConfig(voice_config=types.VoiceConfig(prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name=voice))))





def determine_output_paths(folder, filename_base):

    os.makedirs(folder, exist_ok=True)

    mp3_folder = os.path.join(folder, "MP3_Output")

    os.makedirs(mp3_folder, exist_ok=True)

    file_base_path = os.path.join(folder, filename_base)

    mp3_base_path = os.path.join(mp3_folder, filename_base)

    wav_output = f"{file_base_path}.wav"

    mp3_output = f"{mp3_base_path}.mp3"

    counter = 1

    while os.path.exists(mp3_output):

        wav_output = f"{file_base_path} {counter}.wav"

        mp3_output = f"{mp3_base_path} {counter}.mp3"

        counter += 1

    return wav_output, mp3_output





def save_binary_file(file_name, data, status_callback=print):

    with open(file_name, "wb") as f:

        f.write(data)

    status_callback(

        f"✅ WAV saved successfully to: {os.path.basename(file_name)}")





def convert_to_wav(audio_data: bytes, mime_type: str) -> bytes:

    parameters = parse_audio_mime_type(mime_type)

    bits_per_sample = parameters["bits_per_sample"]

    sample_rate = parameters["rate"]

    header = struct.pack("<4sI4s4sIHHIIHH4sI", b"RIFF", 36 + len(audio_data), b"WAVE", b"fmt ", 16, 1, 1, sample_rate,

                         sample_rate * (bits_per_sample // 8), (bits_per_sample // 8), bits_per_sample, b"data", len(audio_data))

    return header + audio_data





def parse_audio_mime_type(mime_type: str) -> dict[str, int | None]:

    bits_per_sample = 16

    rate = 24000

    for param in mime_type.split(";"):

        if param.lower().strip().startswith("rate="):

            try:

                rate = int(param.split("=", 1)[1])

            except:

                pass

        elif param.strip().startswith("audio/L"):

            try:

                bits_per_sample = int(param.split("L", 1)[1])

            except:

                pass

    return {"bits_per_sample": bits_per_sample, "rate": rate}





และนี่คือโค้ดของ aky_voice_frontend_gui คือ

# File: aky_voice_frontend_gui.py

# -*- coding: utf-8 -*-

import tkinter as tk

from tkinter import ttk, scrolledtext, filedialog, messagebox

import threading

import ttkbootstrap as bstrap

import json

import os



# Import "ห้องครัว" หรือ Backend ของเราเข้ามา

try:

    from backend.aky_voice_backend import run_tts_generation

except ImportError:

    from aky_voice_backend import run_tts_generation



CONFIG_FILE = "config.json"





class App(bstrap.Window):

    def __init__(self):

        super().__init__(themename="darkly")

        self.title("Affiliate Voice Generator Pro")

        self.geometry("1550x1600")

        self.minsize(650, 650)



        self.create_widgets()

        self.configure_grid_weights()

        self.load_settings()

        self.protocol("WM_DELETE_WINDOW", self.on_closing)



    def create_widgets(self):

        main_frame = ttk.Frame(self, padding="15")

        main_frame.pack(fill=tk.BOTH, expand=True)



        ttk.Label(main_frame, text="Affiliate Voice Generator Pro", font=("Helvetica", 20,

                  "bold"), anchor="center").grid(row=0, column=0, columnspan=4, pady=10, sticky="ew")



        ttk.Label(main_frame, text="API Key:").grid(

            row=1, column=0, sticky="w", pady=5)

        api_frame = ttk.Frame(main_frame)

        api_frame.grid(row=1, column=1, columnspan=3, sticky="ew")

        self.api_key_entry = ttk.Entry(api_frame, show="*")

        self.api_key_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.make_text_field_right_clickable(self.api_key_entry)

        self.show_key_var = tk.BooleanVar(value=False)

        self.show_key_check = ttk.Checkbutton(

            api_frame, text="Show Key", variable=self.show_key_var, command=self.toggle_api_key_visibility, bootstyle="square-toggle")

        self.show_key_check.pack(side=tk.LEFT, padx=10)



        ttk.Label(main_frame, text="Style Instructions:").grid(

            row=2, column=0, sticky="nw", pady=5)

        self.style_text = scrolledtext.ScrolledText(

            main_frame, wrap=tk.WORD, width=70, height=10, font=("Tahoma", 10))

        self.style_text.grid(row=2, column=1, columnspan=3,

                             sticky="nsew", pady=5)

        self.make_text_field_right_clickable(self.style_text)



        ttk.Label(main_frame, text="Main Text (Script):").grid(

            row=3, column=0, sticky="nw", pady=5)

        self.main_text_entry = scrolledtext.ScrolledText(

            main_frame, wrap=tk.WORD, width=70, height=10, font=("Tahoma", 10))

        self.main_text_entry.grid(

            row=3, column=1, columnspan=3, sticky="nsew", pady=5)

        self.make_text_field_right_clickable(self.main_text_entry)



        clear_button_frame = ttk.Frame(main_frame)

        clear_button_frame.grid(

            row=4, column=1, columnspan=3, sticky="e", pady=(0, 5))

        ttk.Button(clear_button_frame, text="Clear Fields",

                   command=self.clear_text_fields, bootstyle="secondary-outline").pack()



        gemini_voices_data = {"Zephyr": "Bright", "Puck": "Upbeat", "Charon": "Informative", "Kore": "Firm", "Fenrir": "Excitable", "Leda": "Youthful", "Orus": "Firm", "Aoede": "Breezy", "Callirrhoe": "Easy-going", "Autonoe": "Bright", "Enceladus": "Breathy", "Iapetus": "Clear", "Umbriel": "Easy-going", "Algieba": "Smooth", "Despina": "Smooth",

                              "Erinome": "Clear", "Algenib": "Gravelly", "Rasalgethi": "Informative", "Laomedeia": "Upbeat", "Achernar": "Soft", "Alnilam": "Firm", "Schedar": "Even", "Gacrux": "Mature", "Pulcherrima": "Forward", "Achird": "Friendly", "Zubenelgenubi": "Casual", "Vindemiatrix": "Gentle", "Sadachbia": "Lively", "Sadaltager": "Knowledgeable", "Sulafat": "Warm"}

        voice_display_list = sorted(

            [f"{name} - {desc}" for name, desc in gemini_voices_data.items()])

        ttk.Label(main_frame, text="Voice:").grid(

            row=5, column=0, sticky="w", pady=10)

        self.voice_combo = ttk.Combobox(

            main_frame, values=voice_display_list, state="readonly", width=35)

        self.voice_combo.grid(row=5, column=1, sticky="w", pady=10, padx=5)



        ttk.Label(main_frame, text="Temperature:").grid(

            row=6, column=0, sticky="w", pady=10)

        self.temp_value_label = ttk.Label(

            main_frame, text="0.9", font=("Helvetica", 10, "bold"))

        self.temp_value_label.grid(row=6, column=2, sticky="e", padx=5)

        self.temp_scale = ttk.Scale(

            main_frame, from_=0.0, to=2.0, orient="horizontal", command=self.update_temp_label)

        self.temp_scale.grid(row=6, column=1, sticky="ew", pady=10, padx=5)



        ttk.Label(main_frame, text="Output Folder:").grid(

            row=7, column=0, sticky="w", pady=5)

        self.folder_path = tk.StringVar()

        self.folder_entry = ttk.Entry(

            main_frame, textvariable=self.folder_path, width=60)

        self.folder_entry.grid(row=7, column=1, sticky="ew", pady=5)

        browse_frame = ttk.Frame(main_frame)

        browse_frame.grid(row=7, column=2, columnspan=2, sticky="w")

        ttk.Button(browse_frame, text="Browse...",

                   command=self.browse_folder).pack(side=tk.LEFT, padx=5)

        ttk.Button(browse_frame, text="Open Folder", command=self.open_output_folder,

                   bootstyle="info-outline").pack(side=tk.LEFT)



        ttk.Label(main_frame, text="Filename:").grid(

            row=8, column=0, sticky="w", pady=5)

        self.filename_entry = ttk.Entry(main_frame, width=60)

        self.filename_entry.grid(row=8, column=1, sticky="ew", pady=5)

        self.make_text_field_right_clickable(self.filename_entry)



        # --- [ส่วนที่เพิ่มเข้ามา] แถว FFMPEG Path ---

        ttk.Label(main_frame, text="FFMPEG Path:").grid(

            row=9, column=0, sticky="w", pady=5)

        self.ffmpeg_path = tk.StringVar()

        self.ffmpeg_entry = ttk.Entry(

            main_frame, textvariable=self.ffmpeg_path, width=60)

        self.ffmpeg_entry.grid(row=9, column=1, sticky="ew", pady=5)

        self.ffmpeg_browse_button = ttk.Button(

            main_frame, text="Browse for ffmpeg.exe", command=self.browse_ffmpeg)

        self.ffmpeg_browse_button.grid(

            row=9, column=2, sticky="w", padx=5, pady=5)



        # --- แถวปุ่ม Generate (เลื่อนลำดับ) ---

        self.generate_button = ttk.Button(

            main_frame, text="🚀 Generate Audio", command=self.start_generation_thread, bootstyle="success")

        self.generate_button.grid(row=10, column=1, pady=15, sticky="ew")



        # --- แถว Status Bar (เลื่อนลำดับ) ---

        self.status_label = ttk.Label(

            main_frame, text="Status: Idle", style="info.TLabel")

        self.status_label.grid(

            row=11, column=0, columnspan=4, sticky="w", pady=5)



    def browse_ffmpeg(self):

        """[ฟังก์ชันใหม่] เปิดหน้าต่างเพื่อเลือกไฟล์ ffmpeg.exe"""

        filepath = filedialog.askopenfilename(

            title="Select ffmpeg.exe",

            filetypes=(("Executable files", "*.exe"), ("All files", "*.*"))

        )

        if filepath:

            self.ffmpeg_path.set(filepath.replace("\\", "/"))



    def start_generation_thread(self):

        if not self.api_key_entry.get():

            messagebox.showerror("Error", "กรุณาใส่ API Key ของคุณก่อนครับ!")

            return

        # <-- [เพิ่ม] ตรวจสอบว่าใส่ตำแหน่ง ffmpeg แล้ว

        if not self.ffmpeg_path.get():

            messagebox.showerror(

                "Error", "Please specify the path to ffmpeg.exe!")

            return



        self.generate_button.config(state="disabled")

        selected_voice_display = self.voice_combo.get()

        voice_name_for_api = selected_voice_display.split(' - ')[0]



        # --- [ส่วนที่แก้ไข] เพิ่ม ffmpeg_path เข้าไปใน params ---

        params = {

            "api_key": self.api_key_entry.get(),

            "style_instructions": self.style_text.get("1.0", tk.END),

            "main_text": self.main_text_entry.get("1.0", tk.END),

            "voice_name": voice_name_for_api,

            "output_folder": self.folder_path.get(),

            "output_filename": self.filename_entry.get(),

            "temperature": self.temp_scale.get(),

            "ffmpeg_path": self.ffmpeg_path.get(),  # <-- ส่งตำแหน่ง ffmpeg ไปด้วย

            "status_callback": self.update_status

        }

        threading.Thread(target=self.run_worker,

                         args=(params,), daemon=True).start()



    def save_settings(self):

        settings = {

            "api_key": self.api_key_entry.get(),

            "style": self.style_text.get("1.0", tk.END).strip(),

            "main_text": self.main_text_entry.get("1.0", tk.END).strip(),

            "voice": self.voice_combo.get(),

            "temp": self.temp_scale.get(),

            "folder": self.folder_path.get(),

            "filename": self.filename_entry.get(),

            # <-- [เพิ่ม] บันทึกตำแหน่ง ffmpeg

            "ffmpeg_path": self.ffmpeg_path.get()

        }

        with open(CONFIG_FILE, "w", encoding="utf-8") as f:

            json.dump(settings, f, indent=4)



    def load_settings(self):

        try:

            with open(CONFIG_FILE, "r", encoding="utf-8") as f:

                settings = json.load(f)

            self.api_key_entry.delete(0, tk.END)

            self.api_key_entry.insert(0, settings.get("api_key", ""))

            self.style_text.delete('1.0', tk.END)

            self.style_text.insert("1.0", settings.get("style", ""))

            self.main_text_entry.delete('1.0', tk.END)

            self.main_text_entry.insert("1.0", settings.get("main_text", ""))

            self.voice_combo.set(settings.get("voice", "Achernar - Soft"))

            self.temp_scale.set(settings.get("temp", 0.9))

            self.folder_path.set(settings.get("folder", "../Voice Output"))

            self.filename_entry.delete(0, tk.END)

            self.filename_entry.insert(

                0, settings.get("filename", "Voice Export"))

            # <-- [เพิ่ม] โหลดตำแหน่ง ffmpeg

            self.ffmpeg_path.set(settings.get("ffmpeg_path", ""))

            self.update_temp_label(self.temp_scale.get())

        except (FileNotFoundError, json.JSONDecodeError):

            self.voice_combo.set("Achernar - Soft")

            self.temp_scale.set(0.9)

            self.update_temp_label(0.9)



    # (ฟังก์ชันอื่นๆ ที่เหลือเหมือนเดิมทุกประการ)

    def make_text_field_right_clickable(self, widget):

        context_menu = tk.Menu(widget, tearoff=0)

        commands = {"Cut": "<<Cut>>", "Copy": "<<Copy>>", "Paste": "<<Paste>>"}

        for label, event in commands.items():

            context_menu.add_command(

                label=label, command=lambda w=widget, e=event: w.event_generate(e))

        if isinstance(widget, (scrolledtext.ScrolledText, ttk.Entry)):

            context_menu.add_separator()

            if isinstance(widget, scrolledtext.ScrolledText):

                context_menu.add_command(

                    label="Select All", command=lambda w=widget: w.tag_add(tk.SEL, "1.0", tk.END))

            else:

                context_menu.add_command(

                    label="Select All", command=lambda w=widget: w.select_range(0, tk.END))

        widget.bind(

            "<Button-3>", lambda event: context_menu.tk_popup(event.x_root, event.y_root))



    def configure_grid_weights(self):

        self.grid_rowconfigure(0, weight=1)

        self.grid_columnconfigure(0, weight=1)

        frame = self.winfo_children()[0]

        frame.grid_columnconfigure(1, weight=1)

        frame.grid_rowconfigure(2, weight=1)

        frame.grid_rowconfigure(3, weight=1)



    def toggle_api_key_visibility(self):

        if self.show_key_var.get():

            self.api_key_entry.config(show="")

        else:

            self.api_key_entry.config(show="*")



    def update_temp_label(self, value): self.temp_value_label.config(

        text=f"{float(value):.1f}")



    def browse_folder(self):

        folder = filedialog.askdirectory()

        if folder:

            self.folder_path.set(folder.replace("\\", "/"))



    def update_status(self, message): self.status_label.config(

        text=f"Status: {message}")



    def clear_text_fields(self):

        self.style_text.delete('1.0', tk.END)

        self.main_text_entry.delete('1.0', tk.END)

        messagebox.showinfo("Cleared", "Text fields have been cleared.")



    def open_output_folder(self):

        path = self.folder_path.get()

        if os.path.isdir(path):

            os.startfile(path)

        else:

            messagebox.showerror("Error", f"Folder not found:\n{path}")



    def run_worker(self, params):

        run_tts_generation(**params)

        self.generate_button.config(state="normal")



    def on_closing(self):

        self.save_settings()

        self.destroy()





if __name__ == "__main__":

    app = App()

    app.mainloop()





และนี่คือโค้ดของ run_desktop_app คือ

# File: run_desktop_app.py (Original Version)

from desktop_app.aky_voice_frontend_gui import App

import sys

import os



# บรรทัดนี้จะหาตำแหน่งของโปรเจกต์ (โฟลเดอร์ AKY_v1)

project_root = os.path.dirname(os.path.abspath(__file__))

# บรรทัดนี้จะเพิ่มตำแหน่งนั้นเข้าไปในระบบการค้นหาของ Python

sys.path.insert(0, project_root)



# แก้ไขชื่อโฟลเดอร์ตรงนี้ให้ถูกต้อง (desktop_app)



if __name__ == "__main__":

    print("Starting Affiliate Voice Generator...")

    app = App()

    app.mainloop()
