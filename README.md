# Snivy - A Simple Virtual Assistant for Small to Medium Hotels

Snivy helps hotels save time by answering frequently asked questions, and by
recording complaints, booking issues, and messages from guests in one place.
Guests chat with Snivy through a simple web interface; their questions get
answered instantly, and anything that needs staff attention gets logged for
later follow-up.

## Why this exists

- Many small and medium hotels spend a lot of time answering common questions
  that a virtual assistant like Snivy can handle instead. This frees up the
  front desk to focus on guests who are physically present and on other work.

- Snivy stores guests' general complaints, booking-related issues, and messages
  so hotel staff can review and address them later — no more manually
  recording issues in a notebook or maintaining a separate spreadsheet.

## Live Demo

https://snivy-g81o.onrender.com/

## Quick Start

```bash
git clone https://github.com/CY-Sparrow/Snivy---Hotel-Virtual-Assistant.git
cd Snivy---Hotel-Virtual-Assistant
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python flask run
```

Then open `http://localhost:5000` in your browser.

## Tech Stack

- Backend: Python (Flask)
- Database: Flask-SQLAlchemy
- Frontend: HTML/CSS/JS

## Status

Core functionality complete. Open to bug reports and suggestions.

## License

This project is licensed under the PolyForm Noncommercial License 1.0.0 — see
the [LICENSE](./LICENSE) file for details. In short: free to use, study, and
modify for personal, educational, or non-commercial purposes; commercial use
requires permission from the author.
