# Project Snivy: Virtual Assistant for Grand Stay Hotel

## 1. Overview
**Snivy** is a rule-based virtual assistant designed to facilitate guest interactions for the "Grand Stay Hotel". It provides a structured conversational interface for room booking information, hotel services, FAQs, and handles formal complaints and contact requests.

## 2. Technical Stack
- **Backend:** Python / Flask
- **Database:** SQLite3
- **Frontend:** HTML5, Vanilla CSS, Vanilla JavaScript
- **State Management:** Server-side session and client-side JSON-based transitions.

## 3. Core Architecture

### 3.1 Backend (`app.py`)
- **Routing:** Manages API endpoints for chat flow (`/chat`, `/click`) and form submissions (`/submit-complaint`, `/submit-message`).
- **Integration:** Bridges the chatbot logic (`chatbot/flow.py`) with the database layer (`database.py`).
- **Session Handling:** Uses Flask sessions to track the user's current position in the chat flow.

### 3.2 Chatbot Logic (`chatbot/flow.py`)
- **Rule-Based Engine:** Defined by a large `Flow` dictionary.
- **Node Structure:** Each node contains:
  - `message`: HTML-formatted string for the assistant's response.
  - `buttons`: A list of options, each linking to a `next` node key.
- **Key States:** `START`, `book_menu`, `services_menu`, `faq_menu`, `complaint`, `contact_menu`.

### 3.3 Data Layer (`database.py` & `snivy_database.db`)
- **Tables:**
  - `guests`: `id, name, email, phone, created_date`
  - `complaints`: `id, guest_id, complaint_text, complaint_date, status`
  - `contact_messages`: `id, guest_id, message_text, email, message_date, status`
  - `sessions`: `id, guest_id, last_visit, chat_history, preferences`

## 4. Key Workflows

### 4.1 Chat Interaction
1. User hits `/chat` -> returns `START` node.
2. User clicks a button -> calls `/click` with `nextNode` key.
3. Server updates session and returns the message/buttons for the new node.

### 4.2 Complaint/Message Submission
1. Chat flow directs user to a "complaint" or "contact" node.
2. Frontend collects data (Name, Email, Phone, Text).
3. POST request to `/submit-complaint` or `/submit-message`.
4. Backend checks for existing guest by email (via `get_guest_by_email`), creates a new guest if necessary, and logs the entry into the respective table.

## 5. Directory Structure
- `app.py`: Entry point and API routes.
- `database.py`: SQL schema and DB utility functions.
- `chatbot/flow.py`: Conversational decision tree logic.
- `static/`: CSS and JS assets for the chat UI.
- `templates/`: HTML templates (Flask/Jinja2).
- `leaf/`: Python virtual environment.

## 6. Design Philosophy
The system prioritizes **simplicity and speed**. By using a predefined decision tree, it ensures guests get immediate, accurate answers to common queries without the hallucinations or latency of LLMs, while still providing a path to human intervention via the complaint/contact logging system.
