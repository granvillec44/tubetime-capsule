
import streamlit as st
from datetime import datetime

st.title("📺 TubeTime Capsule")
st.write("Enter a historical date and some keywords to generate smart YouTube and Google search links.")

# User Inputs
date_input = st.text_input("Enter a date (e.g., January 10, 1985):", "January 10, 1985")
keywords_input = st.text_area("Enter keywords (comma-separated):", "Letterman, Prince, NBC News")

if st.button("Generate Search Links"):
    try:
        # Parse and format the date
        parsed_date = datetime.strptime(date_input, "%B %d, %Y")
        date_formats = [
            "%B %d, %Y",  # January 10, 1985
            "%b %d, %Y",  # Jan 10, 1985
            "%m/%d/%y",   # 01/10/85
            "%Y-%m-%d",   # 1985-01-10
            "%m-%d-%y"    # 01-10-85
        ]
        formatted_dates = [parsed_date.strftime(fmt) for fmt in date_formats]

        keywords = [kw.strip() for kw in keywords_input.split(",") if kw.strip()]
        search_queries = [f"{kw} {df}" for kw in keywords for df in formatted_dates]

        st.subheader("🔍 YouTube Links")
        for query in search_queries:
            yt_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
            st.markdown(f"- [{query}]({yt_url})")

        st.subheader("🔎 Google Site Search (More Accurate)")
        for query in search_queries:
            g_url = f"https://www.google.com/search?q=site:youtube.com+{query.replace(' ', '+')}"
            st.markdown(f"- [{query}]({g_url})")

    except ValueError:
        st.error("Please enter the date in a valid format like 'January 10, 1985'")
