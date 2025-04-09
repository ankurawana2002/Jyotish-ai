
import streamlit as st
import pyttsx3
import datetime

st.set_page_config(page_title="Jyotish", layout="centered")

st.markdown("<h1 style='text-align: center; color: orange;'>✨ जय श्री कृष्ण ✨</h1>", unsafe_allow_html=True)
st.markdown("## 🙏 आपका स्वागत है *Jyotish AI* में")
st.markdown("### 📿 एक पूर्णतः भारतीय सनातन AI जो बताए जन्म कुंडली, राशिफल, शुभ मुहूर्त, मंत्र और ग्रंथों का ज्ञान!")

option = st.selectbox("आप क्या जानना चाहते हैं?", [
    "🔮 आज का राशिफल",
    "📿 मंत्र सुनें (11 बार)",
    "📖 ग्रंथों से ज्ञान"
])

# Daily Rashifal
if option == "🔮 आज का राशिफल":
    rashi = st.selectbox("अपनी राशि चुनें:", [
        "मेष", "वृषभ", "मिथुन", "कर्क", "सिंह", "कन्या",
        "तुला", "वृश्चिक", "धनु", "मकर", "कुंभ", "मीन"
    ])

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    st.image(f"https://www.astrosage.com/images/zodiac/{rashi}.jpg", width=150)
    st.success(f"🔆 {rashi} का राशिफल ({today}):\nआज का दिन आपके लिए शुभ रहेगा। आत्मविश्वास बना रहेगा। परिवार का सहयोग मिलेगा।")

# Mantra Playback
elif option == "📿 मंत्र सुनें (11 बार)":
    mantra = st.selectbox("मंत्र चुनें:", [
        "🕉️ गायत्री मंत्र",
        "🔱 महामृत्युंजय मंत्र",
        "🚩 हनुमान चालीसा"
    ])

    mantra_text = {
        "🕉️ गायत्री मंत्र": "ॐ भूर् भुवः स्वः।\nतत्सवितुर्वरेण्यं।\nभर्गो देवस्य धीमहि।\nधियो यो नः प्रचोदयात्॥",
        "🔱 महामृत्युंजय मंत्र": "ॐ त्र्यम्बकं यजामहे\nसुगन्धिं पुष्टिवर्धनम्\nउर्वारुकमिव बन्धनान्मृत्योर्मुक्षीय माऽमृतात्॥",
        "🚩 हनुमान चालीसा": "श्रीगुरु चरन सरोज रज...\n(पूरा पाठ जोड़ें)"
    }

    st.text_area("📿 मंत्र:", value=mantra_text[mantra], height=150)
    if st.button("🔊 आवाज में सुनें (11 बार)"):
        engine = pyttsx3.init()
        engine.setProperty('rate', 140)
        for i in range(11):
            engine.say(mantra_text[mantra])
        engine.runAndWait()
        st.success("✅ 11 बार मंत्र का उच्चारण हो गया।")

# Scriptures Section
elif option == "📖 ग्रंथों से ज्ञान":
    granth = st.selectbox("ग्रंथ चुनें:", [
        "📘 भगवद गीता", "📕 रामायण", "📗 श्रीमद्भागवत", "📙 शिव पुराण"
    ])

    slokas = {
        "📘 भगवद गीता": "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन।",
        "📕 रामायण": "धर्मो रक्षति रक्षितः।",
        "📗 श्रीमद्भागवत": "सर्व धर्मान परित्यज्य मामेकं शरणं व्रज।",
        "📙 शिव पुराण": "नमः पार्वती पतये हर हर महादेव॥"
    }

    st.markdown(f"### ✨ {granth} से श्लोक:")
    st.info(slokas[granth])
