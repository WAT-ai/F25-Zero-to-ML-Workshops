# 🤖 Build Your Own Website Chatbot!

Turn any website into a chatbot that can answer questions about it. Perfect for sports stats, TV show info, or anything you're interested in!

## 🚀 Quick Start

### 1. Run the setup.sh script I created
If you have any trouble, run `chmod +x setup.sh` first to make it executable:

```bash
./setup.sh
```

### 2. Set Up Your API Key
- Copy `.env.example` to `.env`
- Add your OpenAI API key:
```
OPENAI_API_KEY=sk-your-actual-key-here
```

### 3. Choose Your Website & Create Vectorstore
Open `prep_vectorstore.py` and:
- Replace `WEBSITE_URL` with your chosen site
- (Optional) Adjust `chunk_size` and `chunk_overlap`

Run:
```bash
python prep_vectorstore.py
```

### 4. Customize Your Chatbot
Open `frontend.py` and personalize:
- Page title and emoji
- Welcome message
- Colors and styling (check Streamlit docs!)

### 5. Launch!
```bash
streamlit run frontend.py
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
