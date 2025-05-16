# AI Persona Writer

AI Persona Writer is a prototype application demonstrating how language models can adopt distinct personas to generate and comment on content. Designed as part of a technical assessment for an AI/prompt-engineering role, it showcases end-to-end integration between a frontend UI and the OpenAI API.

## Features

- Generate persona-specific articles (300–500 words)
- Leave persona-driven comments (100–150 words) on generated articles
- Three distinct personas: Academic, Creative Optimist, Critical Pragmatist
- Responsive frontend built with HTML, CSS, and JavaScript
- Flask backend integrated with OpenAI API

## Available Personas

Academic

- Style: Formal, evidence-based
- Worldview: Rationalist, data-driven

Creative Optimist

- Style: Imaginative, enthusiastic
- Worldview: Visionary, hopeful

Critical Pragmatist

- Style: Skeptical, grounded
- Worldview: Realist, solution-oriented

## Project Structure
```
backend/
├── app.py - Flask API endpoints
├── prompts.py - Functions to build persona-aware prompts
├── personas.py - Persona tone & worldview definitions
├── utils.py - OpenAI API wrapper
├── requirements.txt - Python dependencies
├── .env.example - Sample environment file (not tracked in Git)
└── static/ - Frontend files
├── index.html - Main interface
├── styles.css - Styling for UI
└── scripts.js - Frontend logic
```
## Getting Started

1. Clone the repository:

```bash
   git clone https://github.com/Ceciliali1205/ai-persona-writer.git
   cd ai-persona-writer/backend
```

2. Create a virtual environment:

```bash
   python3 -m venv venv
   source venv/bin/activate     (Windows CMD: venv\Scripts\activate.bat)
```

3. Install dependencies:

```bash
   pip install -r requirements.txt
```

4. Add your OpenAI API key:

```bash
   cp .env.example .env
   Then edit .env and insert:
   OPENAI_API_KEY=sk-...
```

## Running the App

```bash
   python app.py --port 5001
```

Then visit in your browser: http://localhost:5001

## How It Works


- Users select a persona and enter a topic.
- The backend builds a persona-specific prompt and sends it to the OpenAI API.
- The model returns a generated article, which is displayed.
- Users can then choose another persona to automatically generate a comment on the article.

## Prompt Engineering Notes

- Articles are 300–500 words, styled by persona tone and worldview.
- Comments are concise (100–150 words), opinionated, and reflective of the selected perspective.
- Backend ensures consistency and separation between generation and commentary.

## Author

Cecilia Li  
GitHub: https://github.com/Ceciliali1205
