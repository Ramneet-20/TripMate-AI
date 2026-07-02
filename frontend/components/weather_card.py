import streamlit as st


def render_weather_card(weather):
    st.markdown("### 🌦️ Weather Forecast")

    if weather and "current_weather" in weather:
        current = weather["current_weather"]

        c1, c2 = st.columns(2)
        c1.metric("Temperature", f"{current.get('temperature')}°C")
        c2.metric("Wind Speed", f"{current.get('windspeed')} km/h")

        if "daily" in weather:
            daily = weather["daily"]
            st.write("#### Upcoming Weather")

            for i in range(min(3, len(daily.get("time", [])))):
                st.markdown(
                    f"""
                    <div class="glass-card">
                        <b>{daily['time'][i]}</b><br>
                        Max: {daily['temperature_2m_max'][i]}°C |
                        Min: {daily['temperature_2m_min'][i]}°C |
                        Rain Chance: {daily['precipitation_probability_max'][i]}%
                    </div>
                    """,
                    unsafe_allow_html=True
                )
    else:
        st.write("Weather data not available.")