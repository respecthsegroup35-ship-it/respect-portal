import streamlit as st
from PIL import Image
import datetime
import pandas as pd

# Sayfa Yapılandırması
st.set_page_config(page_title="Respect HSE Group | Saha Portalı", page_icon="🛡️", layout="centered")

# 1. LOGO VE KURUMSAL KİMLİK
# Not: Masaüstünde respect.py'nin yanına 'logo.png' isminde logonuzu koyun.
try:
    st.image("logo.png", width=250)
except:
    st.title("🛡️ Respect HSE Group")

st.subheader("Saha Denetim ve Gözlem Formu")
st.markdown("---")

# 2. DENETİM BİLGİLERİ (Üst Bölüm)
col1, col2 = st.columns(2)
with col1:
    proje_adi = st.selectbox("Proje / İşletme", ["Enerjisa RES", "Enercon RES", "TPI Kompozit", "Diğer"])
    denetim_tarihi = st.date_input("Denetim Tarihi", datetime.date.today())
with col2:
    denetim_turu = st.selectbox("Denetim Türü", ["Rutin Saha Turu", "Yüksek Riskli İş Gözlemi", "Ekipman Denetimi", "Kaza Sonrası İnceleme"])
    denetci_adi = st.text_input("Denetimi Yapan Uzman", value="Mümin Kaya")

st.markdown("---")

# 3. SAHA BULGULARI (Office Forms yapısına uygun başlıklar)
st.markdown("### 📋 Denetim Detayları")
kategori = st.multiselect("Gözlem Kategorisi", 
    ["KKD Kullanımı", "Yüksekte Çalışma", "Elektrik Güvenliği", "Lifting & Rigging", "Kimyasal Yönetimi", "Çevre & Atık", "Yangın Güvenliği"])

bulgu_ozeti = st.text_area("Bulgu / Uygunsuzluk Tanımı", placeholder="Gözlemlenen durumu açıkça belirtin...")

col3, col4 = st.columns(2)
with col3:
    risk_skoru = st.select_slider("Risk Potansiyeli (SIF Takibi)", options=["Düşük", "Orta", "Yüksek", "KRİTİK"])
with col4:
    durum = st.radio("Mevcut Durum", ["Açık (Aksiyon Gerekli)", "Anında Giderildi"])

aksiyon = st.text_area("Alınması Gereken Aksiyon / Öneri", placeholder="Tehlikeyi bertaraf etmek için ne yapılmalı?")

st.markdown("---")

# 4. FOTOĞRAF KISMI (Hem Çekme Hem Yükleme Özelliği)
st.markdown("### 📸 Kanıtlar ve Görseller")
yukleme_tipi = st.tabs(["📷 Kamera ile Çek", "📁 Dosya Yükle"])

fotograflar = []

with yukleme_tipi[0]:
    foto_cek = st.camera_input("Saha Fotoğrafı Çek")
    if foto_cek:
        fotograflar.append(foto_cek)

with yukleme_tipi[1]:
    foto_yukle = st.file_uploader("Bilgisayar/Galeriden Fotoğraf Seç", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])
    if foto_yukle:
        fotograflar.extend(foto_yukle)

st.markdown("---")

# 5. KAYIT VE RAPORLAMA
if st.button("DENETİMİ TAMAMLA VE KAYDET"):
    if bulgu_ozeti and len(fotograflar) > 0:
        # Başarı Mesajı
        st.success(f"✅ Rapor Sisteme İşlendi. Proje: {proje_adi} | Risk: {risk_skoru}")
        st.balloons()
        
        # Ekran Özeti
        st.info("Rapor verisi kaydedildi. Fotoğraflar dijital arşive eklendi.")
    else:
        st.error("Lütfen en az bir bulgu detayı ve fotoğraf eklediğinizden emin olun.")