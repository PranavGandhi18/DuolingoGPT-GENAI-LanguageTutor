import streamlit as st

def app():

    # Embed the Lottie animation using an iframe
    st.markdown(
        """
        <iframe src="https://lottie.host/embed/faf4ce4a-ae46-4209-81b9-88eb918dd562/rjKJQUArkq.json" 
        style="width: 300px; height: 300px; border:none;" allowfullscreen></iframe>
        
        """,
        unsafe_allow_html=True
    )
    

    # Title and subtitle with custom fonts
    st.markdown(
        """
        <style>
        .title {
            font-family: 'Arial', sans-serif;
            font-size: 36px;
            font-weight: bold;
        }
        .subtitle {
            font-family: 'Verdana', sans-serif;
            font-size: 24px;
            color: #666;
        }
        </style>
        <div class="title">DuolingoGPT</div>
        <div class="subtitle">Your ultimate GEN AI powered language tutor, here to unlock your fluency like never before!</div>
        """,
        unsafe_allow_html=True
    )

    # st.title('DuolingoGPT')
    st.write(' ')
    st.write('Enhance your language skills with tailored exercises!')
    st.write('Go to different types of exercises available on the bottom left under the Navigation!')
    st.write('Have Fun & Happy Learning :)')
