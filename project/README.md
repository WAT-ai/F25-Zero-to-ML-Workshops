# 🤖 Build Your Own Website Chatbot!

Turn any website into a chatbot that can answer questions about it. Perfect for sports stats, TV show info, or anything you're interested in!

## 🚀 Step-by-Step Setup Guide

### Step 0: Navigate to the Project Folder
**IMPORTANT**: Before running any commands, make sure you're in the `project` folder!

Open your terminal and run:
```bash
cd project
```

To verify you're in the right place, run:
```bash
pwd
```
You should see a path ending in `.../F25-Zero-to-ML-Workshops/project`

💡 **Tip**: All commands below assume you're in the `project` folder!

---

### Step 1: Set Up Your API Key
Create a file called `.env` in the `project` folder with your OpenAI API key.

**Option A: Using a text editor**
1. Create a new file called `.env` (note the dot at the start!)
2. Add this line: `OPENAI_API_KEY=sk-your-actual-key-here`
3. Save the file in the `project` folder

**Option B: Using terminal** (from inside the `project` folder)
```bash
echo "OPENAI_API_KEY=sk-your-actual-key-here" > .env
```
Replace `sk-your-actual-key-here` with your real API key.

⚠️ **Common Issue**: Make sure the file is named `.env` (not `env.txt` or `env` no dot)

---

### Step 2: Install Dependencies

**Option A: Using the setup script**
```bash
chmod +x setup.sh    # Make the script executable (only needed once)
./setup.sh           # Run the setup script
```

**Option B: Manual installation** (if setup script doesn't work)
```bash
python3 -m venv venv              # Create virtual environment
source venv/bin/activate          # Activate it (Mac/Linux/WSL)
pip install -r requirements.txt   # Install dependencies
```

💡 **How to know if it worked**: You should see `(venv)` at the start of your terminal prompt

⚠️ **Common Issues**:
- If you get "python3: command not found", try `python` instead of `python3`
- If you get "pip: command not found", try `python -m pip` instead of `pip`

---

### Step 3: Choose Your Websites & Create Vectorstore

1. Open `prep_vectorstore.py` in your text editor
2. Find the `WEBSITE_URLS` list (around line 17)
3. Replace `"https://example.com"` with your chosen website(s)
4. **NEW**: You can add multiple URLs! Just add more to the list:
   ```python
   WEBSITE_URLS = [
       "https://www.espn.com/nba/",
       "https://www.nba.com/celtics/",
       "https://www.basketball-reference.com/",
   ]
   ```
5. (Optional) Adjust `chunk_size` and `chunk_overlap` (lines 60-61)

**Run the script**:
```bash
# Make sure you're in the project folder!
# Make sure your virtual environment is activated (you should see "(venv)")
python prep_vectorstore.py
```

This will scrape the websites and create a searchable database. It may take 1-2 minutes depending on how many URLs you added.

⚠️ **Common Issues**:
- "No module named 'langchain'": Make sure you activated the virtual environment (`source venv/bin/activate`)
- "No API key found": Check that your `.env` file exists in the `project` folder
- "Error loading URL": The website might block scraping, try a different site

---

### Step 4: Customize Your Chatbot (Optional)
Open `frontend.py` and personalize:
- Line 8: Page title and emoji
- Line 10: Welcome message
- Colors and styling (check [Streamlit docs](https://docs.streamlit.io/)!)

---

### Step 5: Launch Your Chatbot!
```bash
# Make sure you're in the project folder!
# Make sure your virtual environment is activated!
streamlit run frontend.py
```

The app should open automatically in your browser at `http://localhost:8501`. If not, type that URL into your browser.

🎉 **Success!** You now have a working chatbot!

⚠️ **Common Issues**:
- "Vectorstore not found": Make sure you ran `prep_vectorstore.py` first (Step 3)
- Port already in use: Try `streamlit run frontend.py --server.port 8502`
- Page is blank: Check the terminal for error messages

---

## 🔄 Starting the App Later

After the initial setup, here's what you need to do each time:

```bash
cd project                       # Navigate to project folder
source venv/bin/activate        # Activate virtual environment
streamlit run frontend.py       # Launch the app
```

## 💡 Cool Website Ideas
- **Sports**: ESPN, NBA.com, your favorite team's site
- **Entertainment**: IMDb, Rotten Tomatoes
- **Gaming**: Game wikis, patch notes
- **Music**: Billboard charts, artist pages
- **News**: Tech blogs, science sites

## 🎨 Frontend Customization Tips
- Change emojis in the title
- Add a sidebar with `st.sidebar`
- Use `st.color_picker()` for theme colors
- Add images with `st.image()`
- Try different Streamlit themes in `.streamlit/config.toml`

## 🔧 How It Works
1. **prep_vectorstore.py** - Scrapes your website and creates searchable embeddings
2. **backend.py** - Handles the AI logic (retrieval + conversation)
3. **frontend.py** - Displays the chat interface

## 🆘 Troubleshooting
- **"No API key"**: Make sure `.env` file exists with your key
- **"Vectorstore not found"**: Run `prep_vectorstore.py` first
- **Boring responses**: Try a different website or adjust chunk_size

---

**Have fun and make it yours!** 🎉
