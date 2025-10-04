import time
import streamlit as st
from gradient import Gradient
from gtts import gTTS
import base64
import os
from io import BytesIO

# Set your API key
GRADIENT_MODEL_ACCESS_KEY = "sk-do-oAn_SN0lZsh_vyBsRiLs69ZdYP5j2m7Ch2kdEFoUpv1J4PGdlE0QPI4y6q"

# Configure Gradient client
gradient_client = Gradient(model_access_key=GRADIENT_MODEL_ACCESS_KEY)

# Language code mapping for gTTS
LANGUAGE_CODES = {
    "Hindi": "hi",
    "Bengali": "bn",
    "Telugu": "te",
    "Marathi": "mr",
    "Tamil": "ta",
    "Urdu": "ur",
    "Gujarati": "gu",
    "Malayalam": "ml",
    "Kannada": "kn",
    "Punjabi": "pa",
    "Assamese": "as",
    "Odia": "or",
    "Maithili": "hi",  # Using Hindi as fallback
    "Manipuri": "hi",  # Using Hindi as fallback
    "Santhali": "hi",  # Using Hindi as fallback
    "Kashmiri": "hi",  # Using Hindi as fallback
    "Konkani": "hi",  # Using Hindi as fallback
    "Dogri": "hi",     # Using Hindi as fallback
    "Rajasthani": "hi", # Using Hindi as fallback
    "Bodo": "hi",      # Using Hindi as fallback
    "Sindhi": "sd",
    "Haryanvi": "hi",  # Using Hindi as fallback
    "Khasi": "hi",     # Using Hindi as fallback
    "Mizo": "hi",      # Using Hindi as fallback
    "Nagamese": "hi",  # Using Hindi as fallback
    "Sorbian": "de",   # Using German as fallback
}


# Function to convert text to speech
def text_to_speech(text, language):
    """Convert text to speech and return audio bytes"""
    try:
        # Create audio folder if it doesn't exist
        audio_folder = "audio"
        if not os.path.exists(audio_folder):
            os.makedirs(audio_folder)
        
        # Get language code
        lang_code = LANGUAGE_CODES.get(language, "en")
        
        # Create gTTS object
        tts = gTTS(text=text, lang=lang_code, slow=False)
        
        # Save to BytesIO object for download
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        
        # Also save to audio folder
        audio_file_path = os.path.join(audio_folder, f"prescription_audio_{language}.mp3")
        tts.save(audio_file_path)
        
        return audio_bytes.getvalue()
    except Exception as e:
        st.error(f"Error generating speech: {e}")
        return None


# Function to get a response from Gradient AI LLM
def gradient_ai_response(text, target_language):
    prompt = f"""
        You are a professional medical translator. Your task is to accurately translate the following medical prescriptions into {target_language}.

        Ensure that you maintain the exact medical terminology, dosage instructions, and any special notes related to the prescriptions. Provide a clear and concise translation that a pharmacist or healthcare professional would understand.

        Here are the prescription texts:
        {text}
    """
    try:
        response = gradient_client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama3.3-70b-instruct",
        )
        return response.choices[0].message.content
    except Exception as e:
        # Handle quota exceeded or other errors
        print(f"Error: {e}")
        st.error("An error occurred. Please try again after a short wait.")
        time.sleep(5)  # Wait for 5 seconds before retrying
        return None


# Function to create a download link
def create_download_link(text, filename):
    import base64
    b64 = base64.b64encode(text.encode()).decode()
    href = f'data:file/txt;base64,{b64}'
    return href


# Streamlit app layout
st.set_page_config(page_title="NeuroGrid ScriptSense", layout="wide")
st.title("🌟 NeuroGrid ScriptSense 🌟")
st.subheader("Translate your medical prescriptions accurately into Indian languages")

# Gradient AI shoutout
st.markdown("This app leverages **DigitalOcean Gradient AI** for high-quality medical translations!")

# Instructions for users
st.markdown("""
**Instructions:**
1. Fill in the patient details below.
2. Add medications with their dosage and instructions.
3. Select your target language from the dropdown.
   **You can choose from a variety of Indian languages, including Hindi, Bengali, Telugu, and many more!**
4. Click the "Translate" button to get the translated prescription.
5. **NEW! 🔊** Listen to the audio version of the translated prescription.
6. Download both the text and audio versions of the translation.
7. If you find that the translation is incorrect, feel free to click the "Translate" button again for a new translation.
8. Ensure to include all necessary details for better accuracy.
""")

# Input fields for patient details using columns
col1, col2, col3 = st.columns([1, 1, 1])  # Three equal columns
with col1:
    patient_name = st.text_input("Patient Name:")
with col2:
    patient_id = st.text_input("Patient ID:")
with col3:
    age = st.number_input("Age:", min_value=0, max_value=120)

# Input fields for doctor's information in two columns
col4, col5 = st.columns([1, 1])  # Two equal columns
with col4:
    doctor_name = st.text_input("Doctor's Name:")
with col5:
    doctor_contact = st.text_input("Doctor's Contact:")

# Input field for diagnosis
diagnosis = st.text_area("Diagnosis:", height=68)

# Input fields for treatment details in two rows of two columns each
treatment_col1, treatment_col2 = st.columns(2)  # First row
with treatment_col1:
    treatment_type = st.selectbox("Treatment Type:", ["Medication", "Therapy", "Consultation"])
with treatment_col2:
    treatment_start_date = st.date_input("Treatment Start Date:")

treatment_col3, treatment_col4 = st.columns(2)  # Second row
with treatment_col3:
    treatment_end_date = st.date_input("Treatment End Date:")
with treatment_col4:
    follow_up_date = st.date_input("Follow-Up Appointment Date:")

# Initialize a list to store medication details
medications = []
num_medications = st.number_input("Number of Medications:", min_value=1, max_value=10, value=1)

# Medication input section
for i in range(num_medications):
    st.markdown(f"### Medication {i + 1}")

    # Create a grid for medication details
    medication_col1, dosage_col, frequency_col, duration_col = st.columns(
        [1, 2, 1, 1])  # Adjust column widths as needed

    with medication_col1:
        medication_name = st.text_input("Medication Name:", key=f"medication_name_{i}")

    with dosage_col:
        dosage = st.text_area("Dosage Instructions:", height=100, key=f"dosage_{i}")

    with frequency_col:
        frequency = st.text_input("Frequency:", key=f"frequency_{i}")

    with duration_col:
        duration = st.text_input("Duration:", key=f"duration_{i}")

    # Store medication details if medication name is provided
    if medication_name:
        medications.append({
            "medication_name": medication_name,
            "dosage": dosage,
            "frequency": frequency,
            "duration": duration,
        })

# Known Allergies and Special Notes in two columns
col_allergies, col_notes = st.columns(2)  # Two columns for allergies and notes
with col_allergies:
    allergies = st.text_area("Known Allergies (if any):", height=68)
with col_notes:
    special_notes = st.text_area("Special Notes (if any):", height=100)

# Dropdown for language selection
languages = [
    "Hindi", "Bengali", "Telugu", "Marathi", "Tamil", "Urdu",
    "Gujarati", "Malayalam", "Kannada", "Punjabi", "Assamese",
    "Odia", "Maithili", "Manipuri", "Santhali", "Kashmiri",
    "Konkani", "Dogri", "Rajasthani", "Bodo", "Sindhi", "Haryanvi",
    "Khasi", "Mizo", "Nagamese", "Sorbian", "Urdu"
]
selected_language = st.selectbox("Select a language for translation:", languages)

# Button to trigger translation
if st.button("Translate"):
    if patient_name and medications:  # Check if patient name and at least one medication is filled
        # Construct the prescription text with the desired format
        prescription_text = f"Patient Details:\n\n"
        prescription_text += f"Patient Name: {patient_name}\n"
        prescription_text += f"Patient ID: {patient_id}\n"
        prescription_text += f"Age: {age}\n"
        prescription_text += f"Doctor's Name: {doctor_name}\n"
        prescription_text += f"Doctor's Contact: {doctor_contact}\n"
        prescription_text += f"Diagnosis: {diagnosis}\n"
        prescription_text += f"Treatment Type: {treatment_type}\n"
        prescription_text += f"Treatment Start Date: {treatment_start_date.strftime('%d-%m-%Y')}\n"
        prescription_text += f"Treatment End Date: {treatment_end_date.strftime('%d-%m-%Y')}\n"
        prescription_text += f"Follow-Up Appointment Date: {follow_up_date.strftime('%d-%m-%Y')}\n\n"
        prescription_text += f"Medications:\n\n"

        for index, medication in enumerate(medications, start=1):
            prescription_text += f"Medication {index}:\n"
            prescription_text += f"Medication Name: {medication['medication_name']}\n"
            prescription_text += f"Dosage Instructions: {medication['dosage']}\n"
            prescription_text += f"Frequency: {medication['frequency']}\n"
            prescription_text += f"Duration: {medication['duration']}\n\n"

        # Append special notes and allergies at the end
        prescription_text += f"Known Allergies:\n{allergies if allergies else 'None'}\n"
        prescription_text += f"Special Notes:\n{special_notes if special_notes else 'None'}\n"

        with st.spinner("Translating..."):
            translated_text = gradient_ai_response(prescription_text.strip(), selected_language)

            # Check if translation was successful
            if translated_text is None:
                st.error("Translation failed. Please check your API key and try again.")
            else:
                # Remove any unwanted '**' symbols from the translated text
                cleaned_translated_text = translated_text.replace("**", "")

                st.success("Translation Complete!")

                # Format the output for download: Translated language first, followed by English
                download_content = f"Translated Prescription in {selected_language}:\n\n{cleaned_translated_text}\n\n----------\n\nOriginal Prescription in English:\n\n{prescription_text.strip()}"

                # Display the cleaned translated text
                st.subheader(f"Translated Prescription in {selected_language}:")
                st.text(cleaned_translated_text)

                # Generate Text-to-Speech
                st.subheader("🔊 Audio Playback:")
                with st.spinner("Generating audio..."):
                    audio_data = text_to_speech(cleaned_translated_text, selected_language)
                    
                    if audio_data:
                        st.audio(audio_data, format='audio/mp3')
                        st.success("Audio generated successfully! Click play to listen.")
                        
                        # Create download button for audio
                        st.download_button(
                            label="📥 Download Audio (MP3)",
                            data=audio_data,
                            file_name=f"prescription_audio_{selected_language}.mp3",
                            mime="audio/mp3"
                        )
                    else:
                        st.warning("Could not generate audio. Text translation is still available.")

                # Create a download link for the cleaned translated text
                download_link = create_download_link(download_content, f"translated_prescription_{selected_language}.txt")
                st.markdown(
                    f'<a href="{download_link}" download="translated_prescription_{selected_language}.txt"><button style="color: white; background-color: #4CAF50; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer;">Download Translated Prescription</button></a>',
                    unsafe_allow_html=True)
    else:
        st.error("Please fill in the patient details and at least one medication before translating.")

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 50px;">
    <p style='font-size: 12px; color: grey;'>Disclaimer: While this AI translation tool aims for accuracy, please note that AI translations can make mistakes. Always consult with a healthcare professional for critical decisions.</p>
    <hr>
    <p style="font-size: 12px; color: #888;">&copy; 2025 NeuroGrid. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)

