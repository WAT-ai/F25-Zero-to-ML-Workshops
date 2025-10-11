# Final Challenge: Build Your Business Chatbot

Now it's time to apply what you've learned! Work in teams of two to create a chatbot for a business idea. You'll need to:

1. **Create one slide** explaining:
   - Your target customer (ideal demographic)
   - The problem your chatbot solves
   - How your chatbot helps

2. **Build the chatbot** using the techniques from this workshop

## Business Ideas to Choose From

### 1. Neighborhood Home Finder
- **Target Demographic**: First-time homebuyers (ages 25-35)
- **Problem**: Overwhelmed by choosing which neighborhoods to look at when house hunting
- **Technical Features**: Vectorstore with info about neighborhoods in 3-5 cities, city selector dropdown in frontend, frontend form which gets user preferences (schools, transit, nightlife, etc.)

### 2. College Application Coach
- **Target Demographic**: High school juniors and seniors applying to college
- **Problem**: Confused about which colleges match their profile
- **Technical Features**: Vectorstore with college data (acceptance rates, programs, campus culture), frontend form to get user info (academic interests, location, GPA, etc.), structured output to return top 5 college matches with reasoning.

### 3. Fitness Routine Builder
- **Target Demographic**: Busy professionals (ages 25-45) new to fitness
- **Problem**: Don't know how to create effective workout routines that fit their schedule
- **Technical Features**: Vectorstore with exercise descriptions and routines, structured output to generate weekly workout plans, frontend form for fitness level/goals/available time, Tool Use to calculate calories burned

### 4. Recipe Recommendation Assistant
- **Target Demographic**: College students and young adults learning to cook
- **Problem**: Limited ingredients and cooking skills but want healthy, affordable meals
- **Technical Features**: Vectorstore with recipe data, form on frontend to get budget, available ingredients, dietary restrictions, structured output for shopping list generation and recipe steps.

### 5. Career Path Explorer
- **Target Demographic**: University students unsure about their career direction
- **Problem**: Don't understand what different careers actually involve day-to-day
- **Technical Features**: Vectorstore with career profiles and job descriptions, frontend form to get industry, personality, hobbies, skills, etc., structured output and frontend displays career comparison table

### 6. Travel Destination Planner
- **Target Demographic**: Young professionals (25-35) planning their first international trip
- **Problem**: Overwhelmed by choosing destinations and planning itineraries that match their budget and interests
- **Technical Features**: Vectorstore with travel guides for 10-15 popular destinations, budget, hobbies, culture preferences form on frontend, structured output to generate day-by-day itinerary, PromptTemplate to compare destinations based on preferences (adventure, culture, relaxation, etc.)

### 7. Book Recommendation Engine
- **Target Demographic**: Casual readers looking to develop a reading habit
- **Problem**: Don't know what books to read next and often pick books they don't finish
- **Technical Features**: Vectorstore with book summaries and reviews across genres, genre/mood/other preference form on frontend, structured output for reading list with explanations, Tool Use to estimate reading time based on book length

### 8. Study Buddy for Standardized Tests
- **Target Demographic**: High school students preparing for SAT/ACT
- **Problem**: Need personalized practice and don't know which topics to focus on
- **Technical Features**: Vectorstore with test prep content and strategies, subject selector on frontend, structured output to generate practice questions, Tool Use to track progress across sessions

### Your own idea!

### Tips for Success
- Start simple - get the basic chatbot working first
- Use the techniques you learned: PromptTemplates for consistent responses, Vectorstores for knowledge, Structured Outputs for formatted data
- Test your chatbot with real questions your target demographic would ask
- Make the frontend user-friendly with clear instructions

P.S. **Want more inspiration?** Try finding data on [Kaggle](https://www.kaggle.com/datasets) related to your business idea. Here are [some examples](https://wataiteam.substack.com/p/onboarding-lessons-from-watais-political) of creative chatbots.

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
3. You can add multiple URLs, based on your chatbot topic. Ex: Sports chatbot:
   ```python
   WEBSITE_URLS = [
       "https://www.espn.com/nba/",
       "https://www.nba.com/celtics/",
       "https://www.basketball-reference.com/",
   ]
   ```
4. (Optional) Adjust `chunk_size` and `chunk_overlap` (lines 60-61). Each website's text is split into chunks for the vectorstore. (Slightly) Smaller chunks = more precise answers, but slower and more expensive. Overlap helps share similarity across chunks but (REALLY) increases cost.

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
cd project                      # Navigate to project folder
source venv/bin/activate        # Activate virtual environment
streamlit run frontend.py       # Launch the app
```


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
