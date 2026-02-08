import streamlit as st
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="InkStroke: The Inspiration Engine", page_icon="⚡")

# --- SMART IMAGE SEARCH FUNCTION ---
def find_image_smart(target_filename):
    """
    Looks into the /images folder and finds a match regardless of 
    capitalization or whether it's .jpg or .jpeg.
    """
    folder = "images"
    if not os.path.exists(folder):
        return None
    
    # Get all files currently in the images folder on GitHub
    all_files = os.listdir(folder)
    
    # Clean the target name (e.g., 'Zoro.jpg' becomes 'zoro')
    clean_target = target_filename.split('.')[0].lower()
    
    for f in all_files:
        # Clean the actual file name found in folder
        clean_file = f.split('.')[0].lower()
        if clean_target == clean_file:
            return f"{folder}/{f}"
    return None

# --- ART DATABASE (Your 19 Sketches) ---
# Add all your 19 entries here. I've put a few examples to get you started.
art_db = [
    {
        "file": "Zoro.jpeg", 
        "tags": ["scars", "shame", "pride", "sword", "pain"], 
        "msg": "Scars on the back are a swordsman's shame. Face your challenges head-on!"
    },
    {
        "file": "GokuVegeta.jpeg", 
        "tags": ["hero", "tired", "limits", "training", "exhausted"], 
        "msg": "Even the strongest need to rest. Your effort today is the foundation for tomorrow's strength."
    },
    {
        "file": "Gojo.jpeg", 
        "tags": ["strongest", "confidence", "blindfold", "power"], 
        "msg": "Don't worry, you're doing great. Trust in your own process."
    },
    # --- ADD THE REST OF YOUR 19 ENTRIES BELOW THIS LINE ---
]

# --- USER INTERFACE ---
st.title("InkStroke: The Inspiration Engine ⚡")
st.markdown("### *How are you feeling? Let the characters speak to you.*")

user_input = st.text_input("Describe your vibe or struggle:", placeholder="e.g., 'I feel tired' or 'I need confidence'")

if user_input:
    user_input = user_input.lower()
    found_match = False
    
    for item in art_db:
        # Check if any tag matches the user's input
        if any(tag in user_input for tag in item['tags']):
            st.divider()
            
            # Use the Smart Search to find the path
            image_path = find_image_smart(item['file'])
            
            if image_path:
                st.image(image_path, use_container_width=True)
                st.success(f"**Mentor's Message:** {item['msg']}")
            else:
                st.error(f"Engine Error: I found the vibe, but I can't find the file '{item['file']}' in the images folder.")
                st.info("Make sure the file is uploaded to GitHub inside the 'images' folder!")
                
            found_match = True
            break
            
    if not found_match:
        st.warning("The engine couldn't find that specific vibe yet. Try words like 'tired', 'scars', or 'hero'.")

# --- SIDEBAR ---
with st.sidebar:
    st.header("About this Project")
    st.write("This application integrates AI, NLP, and Software Engineering to support mentor-learner relationships through motivational art.")
    st.write(f"**Total Artworks:** {len(art_db)}")
