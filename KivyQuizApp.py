import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

questions_pool = [
    {"question": "What is the capital of India?", "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"], "answer": 2},
    {"question": "Which country is known as the Land of the Rising Sun?", "options": ["China", "Japan", "Thailand", "India"], "answer": 2},
    {"question": "Who is known as the 'Missile Man of India?'", "options": ["APJ Abdul Kalam", "Vikram Sarabhai", "Homi Bhabha", "Satish Dhawan"], "answer": 1},
    {"question": "What is the currency of Japan?", "options": ["Dollars", "Rupees", "Yen", "Yuan"], "answer": 3},
    {"question": "Which Indian city is known as the Pink City?", "options": ["Mumbai", "Jodhpur", "Jaipur", "Kolkata"], "answer": 3},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mercury", "Jupiter", "Mars"], "answer": 4},
    {"question": "Who is the current President of India? (as of 2025)", "options": ["Narendra Modi", "Droupadi Murmu", "Pranab Mukherjee", "Ram Nath Kovind"], "answer": 2},
    {"question": "What is the full form of ATM?", "options": ["Any Time Money", "Automated Teller Machine", "Automatic Transfer Mode", "Advanced Transaction Method"], "answer": 1},
    {"question": "Which bird is the national bird of India?", "options": ["Peacock", "Parrot", "Eagle", "Sparrow"], "answer": 1},
    {"question": "What is the tallest building in the world?", "options": ["Burj Khalifa", "Kutub Minar", "Twin Towar", "Trump Towar"], "answer": 1},
    {"question": "Who was the first President of India?", "options": ["Sardar Vallabhbhai Patel", "Rajendra Prasad", "Jawaharlal Nehru", "Dr. B. R. Ambedkar"], "answer": 2},
    {"question": "When did India gain independence?", "options": ["1945", "1946", "1947", "1948"], "answer": 3},
    {"question": "Who was the last Mughal emperor of India?", "options": ["Akbar", "Shah Jahan", "Bahadur Shah Zafar", "Aurangzeb"], "answer": 3},
    {"question": "In which year did the First World War start?", "options": ["1912", "1914", "1916", "1918"], "answer": 2},
    {"question": "Who was the founder of the Maurya Empire?", "options": ["Ashoka", "Chandragupta Maurya", "Bindusara", "Harshavardhana"], "answer": 2},
    {"question": "Which Indian freedom fighter gave the slogan “Give me blood and I shall give you freedom”?", "options": ["Mahatma Gandhi", "Subhas Chandra Bose", "Jawaharlal Nehru", "Bhagat Singh"], "answer": 2},
    {"question": "Who wrote the book Discovery of India?", "options": ["Sardar Patel", "Mahatma Gandhi", "Jawaharlal Nehru", "B. R. Ambedkar"], "answer": 3},
    {"question": "Who was the first woman Prime Minister of India?", "options": ["Sarojini Naidu", "Pratibha Patil", "Indira Gandhi", "Sushma Swaraj"], "answer": 3},
    {"question": "In which year was the Constitution of India adopted?", "options": ["1947", "1949", "1950", "1952"], "answer": 2},
    {"question": "Who led the Dandi March?", "options": ["Mahatma Gandhi", "Sardar Patel", "Jawaharlal Nehru", "Lala Lajpat Rai"], "answer": 1},
    {"question": "What is the longest river in the world?", "options": ["Amazon", "Yangtze", "Nile", "Mississippi"], "answer": 3},
    {"question": "Which continent is the Sahara Desert located in?", "options": ["Asia", "Africa", "Australia", "Europe"], "answer": 2},
    {"question": "What is the largest ocean on Earth?", "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"], "answer": 3},
    {"question": "Which is the smallest country in the world?", "options": ["Monaco", "San Marino", "Maldives", "Vatican City"], "answer": 4},
    {"question": "Mount Everest is located in which mountain range?", "options": ["Rockies", "Andes", "Alps", "Himalayas"], "answer": 4},
    {"question": "Which country has the most number of time zones?", "options": ["USA", "India", "Russia", "France"], "answer": 4},
    {"question": "Which Indian state has the longest coastline?", "options": ["Maharashtra", "Andhra Pradesh", "Gujarat", "Tamil Nadu"], "answer": 3},
    {"question": "What is the capital of Australia?", "options": ["Sydney", "Melbourne", "Perth", "Canberra"], "answer": 4},
    {"question": "Which planet is closest to the Sun?", "options": ["Mercury", "Venus", "Earth", "Mars"], "answer": 1},
    {"question": "What is the largest island in the world?", "options": ["Australia", "Greenland", "New Guinea", "Borneo"], "answer": 2},
    {"question": "What does CPU stand for?", "options": ["Central Power Unit", "Central Processing Unit", "Computer Processing Unit", "Core Processing Unit"], "answer": 2},
    {"question": "What is the full form of Wi-Fi?", "options": ["Wireless Fidelity", "Wired Field", "Wide Frequency", "Wireless Feature"], "answer": 1},
    {"question": "Which company developed the Windows operating system?", "options": ["Apple", "Microsoft", "Google", "IBM"], "answer": 2},
    {"question": "What is the full form of URL?", "options": ["Uniform Resource Locator", "Universal Remote Link", "User Resource Link", "Unified Retrieval Locator"], "answer": 1},
    {"question": "Who is known as the father of the computer?", "options": ["Alan Turing", "Charles Babbage", "John von Neumann", "Bill Gates"], "answer": 2},
    {"question": "Which programming language is known for its snake logo?", "options": ["Java", "Python", "C++", "Ruby"], "answer": 2},
    {"question": "What does HTML stand for?", "options": ["HyperText Markup Language", "HighText Machine Language", "HyperText Markdown Language", "None of the above"], "answer": 1},
    {"question": "What does RAM stand for?", "options": ["Read Access Memory", "Random Access Memory", "Run Active Memory", "Remote Access Module"], "answer": 2},
    {"question": "Which social media platform is owned by Meta?", "options": ["Twitter", "LinkedIn", "Facebook", "Snapchat"], "answer": 3},
    {"question": "Which key is used to refresh a webpage in most browsers?", "options": ["F5", "F11", "Ctrl", "Esc"], "answer": 1},
    {"question": "Which gas do humans need to breathe to survive?", "options": ["Carbon Dioxide", "Oxygen", "Nitrogen", "Hydrogen"], "answer": 2},
    {"question": "How many bones are there in the adult human body?", "options": ["206", "210", "198", "216"], "answer": 1},
    {"question": "What is H2O commonly known as?", "options": ["Salt", "Water", "Oxygen", "Ammonia"], "answer": 2},
    {"question": "Which part of the plant conducts photosynthesis?", "options": ["Roots", "Stem", "Leaves", "Flowers"], "answer": 3},
    {"question": "What vitamin do we get from sunlight?", "options": ["Vitamin A", "Vitamin C", "Vitamin D", "Vitamin B12"], "answer": 3},
    {"question": "Which metal is liquid at room temperature?", "options": ["Mercury", "Iron", "Aluminium", "Sodium"], "answer": 1},
    {"question": "What is the unit of electric current?", "options": ["Ohm", "Volt", "Ampere", "Watt"], "answer": 3},
    {"question": "Which animal is known as the 'Ship of the Desert'?", "options": ["Camel", "Horse", "Elephant", "Donkey"], "answer": 1},
    {"question": "Which is the fastest land animal?", "options": ["Cheetah", "Tiger", "Horse", "Deer"], "answer": 1},
    {"question": "How many planets are there in our solar system?", "options": ["7", "8", "9", "10"], "answer": 2},
]

class QuizApp(App):
    def build(self):
        self.total_money = 0
        self.correct_answers = 0
        self.selected_questions = random.sample(questions_pool, 5)
        self.current_question = 0

        self.layout = BoxLayout(orientation='vertical')

        # Welcome message Label
        self.welcome_label = Label(text="Welcome to the Python Quiz Game!",
                                   color=(0, 1, 1, 1))  # Cyan color (R, G, B, A)
        self.layout.add_widget(self.welcome_label)

        # Instructions Label
        self.instructions_label = Label(text="In this quiz, you'll earn ₹100 for every correct answer.\nChoose the correct option by entering the number (1-4).\nGood luck!",
                                        color=(1, 1, 1, 1))  # White color (R, G, B, A)
        self.layout.add_widget(self.instructions_label)

        # Label for displaying the question
        self.question_label = Label(text="Loading Question...")
        self.layout.add_widget(self.question_label)

        # Buttons for options
        self.option_buttons = []
        for i in range(4):
            button = Button(text=f"Option {i + 1}")
            button.bind(on_press=self.check_answer)
            self.option_buttons.append(button)
            self.layout.add_widget(button)

        # Label to show current score
        self.score_label = Label(text="Score: ₹0")
        self.layout.add_widget(self.score_label)

        # Display the first question
        self.display_question()

        return self.layout

    def display_question(self):
        question = self.selected_questions[self.current_question]
        self.question_label.text = question["question"]

        for i, button in enumerate(self.option_buttons):
            button.text = question["options"][i]

    def check_answer(self, instance):
        question = self.selected_questions[self.current_question]
        selected_option = self.option_buttons.index(instance) + 1

        if selected_option == question["answer"]:
            self.total_money += 100
            self.correct_answers += 1
            self.score_label.text = f"Score: ₹{self.total_money}"
        else:
            # Display popup with the points before closing
            self.display_popup(f"Game Over", f"You won ₹{self.total_money}.")
            return

        self.current_question += 1
        if self.current_question < len(self.selected_questions):
            self.display_question()
        else:
            self.display_popup("Congratulations", f"You answered {self.correct_answers} questions correctly! Final Score: ₹{self.total_money}")

    def display_popup(self, title, message):
        # Create the popup content (label + button)
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=message))
        close_button = Button(text="Close", on_press=self.close_app)
        content.add_widget(close_button)

        # Create the popup itself
        popup = Popup(title=title,
                      content=content,
                      size_hint=(None, None), size=(400, 200),
                      auto_dismiss=True)
        popup.open()

    def close_app(self, instance):
        App.get_running_app().stop()

if __name__ == "__main__":
    QuizApp().run()