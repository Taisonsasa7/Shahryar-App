st.markdown("""
    <style>
    .room-card { background-color: #1E1A23; border-radius: 20px; padding: 15px; margin: 10px; color: white; }
    .live-badge { background-color: #FF4B4B; padding: 2px 6px; border-radius: 5px; font-size: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("شهريار")

# هنا السحر: نظام لتوزيع الغرف في أعمدة (2 في كل صف)
cols = st.columns(2)
for i, room in enumerate(rooms_data):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="room-card">
            <div style="height: 100px; background: #333; border-radius: 10px;"></div>
            <p><span class="live-badge">LIVE</span> 👁️ {room['viewers']} ❤️ {room['likes']}</p>
            <h4>{room['name']}</h4>
            <p>{room['title']}</p>
        </div>
        """, unsafe_allow_html=True)
        st.button(f"دخول {room['name']}", key=f"btn_{i}"
