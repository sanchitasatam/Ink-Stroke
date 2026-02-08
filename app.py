import streamlit as st

# 1. This is your 'art_db' - The Brain of the App
# Make sure the 'file' name matches your image filenames exactly!
art_db = [
    {
        "file": "asl.jpg", 
        "tags": ["lonely", "family", "brother", "loss", "friends", "bond"], 
        "msg": "Bonds aren't just about being together; they are about carrying each other's will. You are never walking alone."
    },
    {
        "file": "mha_canvas.jpg", 
        "tags": ["hero", "tired", "exhausted", "helping", "sacrifice", "burden", "trying"], 
        "msg": "Giving help that is not asked for is what makes a true hero. Your effort shines even when you're tired."
    },
    {
        "file": "gojo_sukuna.jpg", 
        "tags": ["power", "ego", "control", "chaos", "confident", "strongest", "win"], 
        "msg": "Master your inner chaos. Whether you are the hero or the monster today, do it with absolute conviction."
    },
    {
        "file": "spike.jpg", 
        "tags": ["past", "regret", "memory", "moving on", "sad", "yesterday"], 
        "msg": "One eye sees the past, the other sees the future. Don't let yesterday take up too much of today."
    },
    {
        "file": "zoro.jpg", 
        "tags": ["pride", "shame", "fear", "scar", "commitment", "training"], 
        "msg": "Scars on the back are a swordsman's shame. Face your challenges head-on; never turn your back."
    },
    {
        "file": "tanjiro.jpg", 
        "tags": ["kindness", "protect", "weak", "growth", "effort", "family"], 
        "msg": "True strength isn't for dominating; it's for lifting others up. Your kindness is your greatest power."
    }
    # You can keep adding more blocks here for Naruto, Itachi, etc.!
]

# 2. The User Interface (UI)
st.set_page_config(page_title="InkStroke Inspiration", page_icon="🎨")

st.title("InkStroke: The Inspiration Engine ⚡")
st.write("### *How are you feeling? Let the characters speak to you.*")

# 3. The NLP Interaction Layer
user_input = st.text_input("Describe your vibe or struggle:", placeholder="e.g., 'I feel like giving up' or 'I need confidence'")

if user_input:
    user_input = user_input.lower()
    
    # Logic to find the best matching sketch
    found_match = False
    
    for item in art_db:
        # Check if any keyword in the tags matches the user's input
        if any(keyword in user_input for keyword in item['tags']):
            st.divider()
            # This looks in your 'images' folder for the file
            st.image(f"images/{item['file']}", use_container_width=True)
            st.success(f"**The Message:** {item['msg']}")
            found_match = True
            break
            
    if not found_match:
        st.info("I don't have a specific sketch for that vibe yet, but remember: Even the greatest heroes had filler episodes. Keep moving forward!")

# Sidebar info for your research portfolio
st.sidebar.header("About this Project")
st.sidebar.write("Built as part of a research study on integrating NLP and AI into mentor-learner applications.")