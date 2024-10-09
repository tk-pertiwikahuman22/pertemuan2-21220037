import streamlit as st
import pandas as pd

# Judul aplikasi
st.title("Visualisasi Dataset dengan Berbagai Jenis Chart di Streamlit")

# Penjelasan singkat
st.write("""
Aplikasi ini memungkinkan Anda untuk mengunggah file dataset CSV dan menampilkan data dalam berbagai jenis grafik seperti Line Chart, Bar Chart, atau Area Chart.
Anda bisa memilih kolom mana yang akan divisualisasikan dan jenis grafik yang ingin digunakan.
""")

# Fitur untuk mengunggah file CSV
uploaded_file = st.file_uploader("Pilih file CSV Anda", type=["csv"])

if uploaded_file is not None:
    try:
        # Membaca dataset
        df = pd.read_csv(uploaded_file)

        # Menampilkan dataframe
        st.write("Dataset yang diunggah:")
        st.dataframe(df)

        # Menampilkan informasi tentang dataset
        st.write("Informasi dataset:")
        st.write(df.describe())

        # Memastikan bahwa dataset memiliki setidaknya satu kolom numerik
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        
        if len(numeric_columns) > 0:
            # Memilih kolom untuk visualisasi
            selected_columns = st.multiselect("Pilih kolom untuk ditampilkan dalam grafik", numeric_columns, default=numeric_columns[:3])

            if len(selected_columns) > 0:
                # Pilihan jenis chart
                chart_type = st.selectbox(
                    "Pilih jenis grafik:",
                    ("Line Chart", "Bar Chart", "Area Chart")
                )

                # Menampilkan grafik sesuai pilihan jenis chart
                st.write(f"Menampilkan {chart_type} untuk kolom {', '.join(selected_columns)}")

                if chart_type == "Line Chart":
                    st.line_chart(df[selected_columns])
                elif chart_type == "Bar Chart":
                    st.bar_chart(df[selected_columns])
                elif chart_type == "Area Chart":
                    st.area_chart(df[selected_columns])
            else:
                st.write("Pilih setidaknya satu kolom untuk menampilkan grafik.")
        else:
            st.error("Dataset tidak mengandung kolom numerik yang valid. Silakan unggah dataset yang memiliki kolom numerik.")

    except Exception as e:
        st.error(f"Terjadi kesalahan saat membaca file CSV: {e}")
else:
    st.write("Silakan unggah file CSV untuk mulai.")

# Footer
st.write("""
---
Dikembangkan menggunakan Streamlit. Silakan unggah dataset CSV untuk memulai visualisasi data.
""")
