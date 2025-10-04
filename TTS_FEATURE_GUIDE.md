# 🔊 Text-to-Speech Feature Documentation

## Overview

NeuroGrid ScriptSense now includes **Text-to-Speech (TTS)** functionality that converts translated medical prescriptions into audio format. This helps patients who may have difficulty reading or prefer to listen to their prescriptions.

---

## 🎯 Features

### 1. **Automatic Audio Generation**

- After translating a prescription, the app automatically generates audio
- Supports all 27+ Indian languages in the application
- Uses Google Text-to-Speech (gTTS) for high-quality audio

### 2. **Audio Playback**

- Built-in audio player in the web interface
- Play/pause controls
- Volume adjustment
- Seek/scrub through audio

### 3. **Audio Download**

- Download audio as MP3 file
- Filename format: `prescription_audio_{language}.mp3`
- Compatible with all devices and media players

---

## 📝 How to Use

### Step 1: Translate Prescription

1. Fill in all patient and medication details
2. Select your target language
3. Click "Translate" button

### Step 2: Listen to Audio

1. After translation completes, scroll down to "🔊 Audio Playback" section
2. Click the play button to listen
3. Adjust volume as needed

### Step 3: Download Audio (Optional)

1. Click "📥 Download Audio (MP3)" button
2. Save the file to your device
3. Share with patients or play on other devices

---

## 🌍 Supported Languages

All languages have TTS support with appropriate language codes:

| Language  | TTS Code      | Native Support |
| --------- | ------------- | -------------- |
| Hindi     | hi            | ✅ Full        |
| Bengali   | bn            | ✅ Full        |
| Telugu    | te            | ✅ Full        |
| Marathi   | mr            | ✅ Full        |
| Tamil     | ta            | ✅ Full        |
| Urdu      | ur            | ✅ Full        |
| Gujarati  | gu            | ✅ Full        |
| Malayalam | ml            | ✅ Full        |
| Kannada   | kn            | ✅ Full        |
| Punjabi   | pa            | ✅ Full        |
| Assamese  | as            | ✅ Full        |
| Odia      | or            | ✅ Full        |
| Sindhi    | sd            | ✅ Full        |
| Others    | hi (fallback) | ⚠️ Uses Hindi  |

_Note: Languages without direct TTS support use Hindi as fallback for best quality._

---

## 🔧 Technical Details

### Technology Stack

- **gTTS (Google Text-to-Speech)** v2.5.4
- Python 3.10+
- Streamlit audio player
- MP3 audio format

### Audio Specifications

- **Format:** MP3
- **Quality:** Standard (optimized for speech)
- **Speed:** Normal speaking pace
- **Language:** Auto-detected from selection

### Code Implementation

```python
from gtts import gTTS
from io import BytesIO

def text_to_speech(text, language):
    """Convert text to speech and return audio bytes"""
    try:
        # Get language code
        lang_code = LANGUAGE_CODES.get(language, "en")

        # Create gTTS object
        tts = gTTS(text=text, lang=lang_code, slow=False)

        # Save to BytesIO object
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)

        return audio_bytes.getvalue()
    except Exception as e:
        st.error(f"Error generating speech: {e}")
        return None
```

---

## 💡 Use Cases

### 1. **Elderly Patients**

- Patients with vision problems can listen to prescriptions
- Easier to understand dosage instructions

### 2. **Language Accessibility**

- Patients can hear proper pronunciation
- Better comprehension in native language

### 3. **Documentation**

- Audio records for patient files
- Playback during medication administration

### 4. **Caregiver Support**

- Family members can listen to instructions
- Share audio with caregivers

---

## ⚠️ Limitations

1. **Internet Required:** gTTS needs internet connection to generate audio
2. **Fallback Languages:** Some regional languages use Hindi TTS
3. **Audio Quality:** Dependent on translation quality
4. **File Size:** Longer prescriptions create larger audio files

---

## 🐛 Troubleshooting

### Audio Not Generated

**Problem:** "Could not generate audio" message appears

**Solutions:**

1. Check internet connection
2. Ensure text translation was successful
3. Try a different language
4. Refresh the page and try again

### Audio Playback Issues

**Problem:** Audio player not working

**Solutions:**

1. Use a modern browser (Chrome, Firefox, Edge)
2. Enable audio in browser settings
3. Check device volume
4. Try downloading and playing externally

### Download Button Not Working

**Problem:** Can't download audio file

**Solutions:**

1. Check browser download settings
2. Allow downloads from localhost
3. Try right-click "Save As"
4. Check available disk space

---

## 🔄 Future Enhancements

Planned features for future releases:

- [ ] Multiple voice options (male/female)
- [ ] Adjustable speech speed
- [ ] Offline TTS support
- [ ] More regional language support
- [ ] Voice emphasis on important instructions
- [ ] Batch audio generation

---

## 📊 Benefits

### For Patients

✅ Easier to understand prescriptions  
✅ Better medication compliance  
✅ Accessible for visually impaired  
✅ Can replay instructions

### For Healthcare Providers

✅ Improved patient education  
✅ Reduced medication errors  
✅ Better communication  
✅ Professional documentation

---

## 🔐 Privacy & Security

- **No Audio Storage:** Audio generated on-demand
- **Local Processing:** Audio created in memory
- **No Cloud Upload:** Files not stored on servers
- **User Control:** Download/delete at will

---

## 📚 Additional Resources

- **gTTS Documentation:** https://gtts.readthedocs.io/
- **Streamlit Audio:** https://docs.streamlit.io/library/api-reference/media/st.audio
- **Language Codes:** ISO 639-1 standard

---

## ✨ Quick Tips

1. **Test Audio First:** Always preview before downloading
2. **Check Volume:** Adjust before playing in patient areas
3. **Save for Records:** Download for patient files
4. **Share Wisely:** Consider patient privacy when sharing

---

**Powered by:**

- 🔊 Google Text-to-Speech (gTTS)
- 🚀 DigitalOcean Gradient AI
- ⚡ Streamlit

**Created by:** NeuroGrid  
**Last Updated:** October 4, 2025

---

For more information, see the main README.md or contact support.
