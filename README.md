# GPT-2 Chatbot Project

This project is a chatbot application utilizing the GPT-2 model from the Transformers library by Hugging Face. The backend of the application is built using Flask, while the frontend interface is created with HTML.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## Introduction

This chatbot project demonstrates the capabilities of the GPT-2 model in generating human-like text responses. The project combines a Python-based Flask backend with an HTML frontend to provide a simple and interactive web interface for users to interact with the chatbot.

## Features

- **Natural Language Processing:** Utilizes the GPT-2 model for generating conversational responses.
- **Web Interface:** A user-friendly HTML interface for interacting with the chatbot.
- **REST API:** Flask-based backend serving the chatbot responses via API endpoints.

## Requirements

To run this project, you need the following software and libraries:

- Python 3.8+
- Flask
- Transformers (Hugging Face)
- Torch
- HTML and CSS for the frontend

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/AaftabAalam/chatBot.git
   cd chatBot
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the Required Packages:**

   ```bash
   pip install -r requirements.txt
   ```

   Ensure `requirements.txt` includes the following packages:
   ```
   Flask
   transformers
   torch
   ```

4. **Download GPT-2 Model:**

   The model will be automatically downloaded the first time you run the code, or you can manually download it using the following command:
   ```python
   from transformers import GPT2Tokenizer, GPT2LMHeadModel

   tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
   model = GPT2LMHeadModel.from_pretrained("gpt2")
   ```

## Usage

1. **Start the Flask Server:**

   ```bash
   python app.py
   ```

2. **Open the Web Interface:**

   Open your web browser and go to `http://127.0.0.1:5000/` to interact with the chatbot.

## File Structure

```
gpt2-chatbot/
├── app.py               # Main Flask application
├── templates/
│   └── index.html       # HTML file for the user interface
├── requirements.txt     # List of required packages
├── README.md            # Project documentation
```

### app.py

This file contains the Flask server code that loads the GPT-2 model and serves responses to user inputs.

### templates/index.html

The HTML file that creates the user interface for interacting with the chatbot.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please create an issue or submit a pull request.

## Acknowledgments

- [Hugging Face](https://huggingface.co/) for providing the Transformers library and pre-trained GPT-2 model.
- [Flask](https://flask.palletsprojects.com/) for the lightweight WSGI web application framework.
- Everyone who contributed to the open-source libraries used in this project.
