# Flashlearn

Flashlearn is an AI-powered web application designed to help users efficiently summarize long paragraphs and generate flashcards for study purposes. It features a clean, user-friendly interface and leverages advanced AI models to provide concise summaries and interactive flashcards.

## Features

- **Summarization**: Quickly summarize long paragraphs into concise text.
- **Flashcard Generation**: Automatically create flashcards from the summarized content.
- **Interactive UI**: Simple and clean design with a focus on usability.
- **Responsive Design**: Accessible on all devices, including desktops, tablets, and smartphones.

## Installation

### Prerequisites

- Python 3.8+
- Django 4.x
- Git

### Setup Instructions

1. **Clone the repository:**

    ```bash
    git clone https://github.com/perarulalan15/FlashLearn.git
    cd flashlearn
    ```

2. **Create and activate a virtual environment:**

    - On Windows:
      ```bash
      python -m venv env
      .\env\Scripts\activate
      ```

    - On macOS/Linux:
      ```bash
      python3 -m venv env
      source env/bin/activate
      ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

6. **Access the application:**

    Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

1. **Enter a Paragraph**: Input the paragraph you want to summarize into the provided text field.
2. **Generate Summary**: Click on the "Generate" button to create a summary.
3. **View Flashcards**: After generating the summary, flashcards will be displayed for interactive learning.

## Demo

https://github.com/user-attachments/assets/646a873a-5958-45ad-8537-008ef8a71357


## Contributing

Contributions are welcome! Please follow the steps below:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## Acknowledgements

- **Django**: For the robust and scalable web framework.
- **OpenAI GPT Models**: For powering the AI-driven summarization and flashcard generation.
- **Contributors**: Thanks to everyone who has contributed to this project.

## Contact

For further information or inquiries:

- **Email**: ksriram217@gmail.com
- **Email**: perarulalan01@gmail.com

