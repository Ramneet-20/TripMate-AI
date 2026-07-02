import streamlit as st


def render_news_card(latest_news):
    st.markdown("### 📰 Latest Travel News / Alerts")

    if latest_news:
        for news in latest_news:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)

            st.write(f"#### {news.get('title', 'No title')}")
            st.caption(f"{news.get('source', 'Unknown source')} | {news.get('date', '')}")

            if news.get("url"):
                st.markdown(f"[Read more]({news.get('url')})")

            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.write("No latest travel news found.")