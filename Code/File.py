import random
from kivy.app import App
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget

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
    # -------- colours & settings -----------
    BACKGROUND = (0.678, 0.847, 1.0, 0.6)       # warm, light blue
    BTN_BG      = (1.0, 0.992, 0.816, 1)        # white button
    BTN_TEXT    = (0.1, 0.1, 0.1, 1)            # near‑black text
    BTN_CORRECT = (0.20, 0.80, 0.25, 1)         # green
    BTN_WRONG   = (0.90, 0.15, 0.15, 1)         # red
    TIMER_START = 10
    Q_COUNT     = 10

    def build(self):
        Window.clearcolor = self.BACKGROUND
        self.root = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.total_money = 0
        self.correct_answers = 0
        self.selected_questions = random.sample(questions_pool, self.Q_COUNT)
        self.current_question = 0
        self.timer_event = None
        self.time_left = self.TIMER_START

        self.correct_sound = SoundLoader.load("correct.wav")
        self.wrong_sound = SoundLoader.load("wrong.wav")

        self.header = Label(
            text="Welcome to the Python Quiz Game!",
            font_size=48,
            bold=True,
            color=(0.1, 0.1, 0.3, 1),
            size_hint_y=None,
            height=40,
        )
        self.root.add_widget(self.header)

        self.root.add_widget(Widget(size_hint_y=None, height=20))

        self.instructions = Label(
            text="Answer quickly! ₹100 per correct answer.\n10 seconds per question.",
            font_size=24,
            halign="center",
            color=(0.2, 0.2, 0.2, 1),
            size_hint_y=None,
            height=60,
        )
        self.instructions.bind(size=self.instructions.setter('text_size'))
        self.root.add_widget(self.instructions)

        # Only timer (no progress bar)
        self.timer_label = Label(
            text=f"Time: {self.TIMER_START}",
            color=(0.5, 0, 0, 1),
            font_size=28,
            size_hint_y=None,
            height=40
        )
        self.root.add_widget(self.timer_label)

        self.question_label = Label(
            text="Loading question…",
            font_size=20,
            halign="center",
            valign="middle",
            size_hint_y=None,
            height=80,
            color=(0.1, 0.1, 0.1, 1),
        )
        self.question_label.bind(size=self.question_label.setter('text_size'))
        self.root.add_widget(self.question_label)

        self.option_buttons = []
        for i in range(4):
            btn = Button(
                text=f"Option {i + 1}",
                background_normal='',
                background_color=self.BTN_BG,
                color=self.BTN_TEXT,
                size_hint_y=None,
                height=50,
                font_size=18,
                border=(10, 10, 10, 10),
            )
            btn.bind(on_press=self.check_answer)
            self.option_buttons.append(btn)
            self.root.add_widget(btn)

        self.score_label = Label(text="Score: 0", font_size=28, color=(0, 0.3, 0, 1))
        self.root.add_widget(self.score_label)

        self.display_question()
        return self.root

    def display_question(self):
        self.stop_timer()
        self.time_left = self.TIMER_START
        self.timer_label.text = f"Time: {self.time_left}"
        self.start_timer()

        q = self.selected_questions[self.current_question]
        
        # Store the original correct answer text before shuffling
        correct_answer_text = q["options"][q["answer"] - 1]

        # Shuffle the options
        random.shuffle(q["options"])

        # Find the new index of the correct answer
        # The 'answer' key in the question dictionary needs to be updated
        # to reflect the new 1-based index of the correct answer after shuffling.
        q["answer"] = q["options"].index(correct_answer_text) + 1


        self.question_label.text = q["question"]

        for i, button in enumerate(self.option_buttons):
            button.text = q["options"][i]
            button.background_color = self.BTN_BG
            button.color = self.BTN_TEXT
            button.disabled = False

    def start_timer(self):
        self.timer_event = Clock.schedule_interval(self.update_timer, 1)

    def stop_timer(self):
        if self.timer_event:
            Clock.unschedule(self.timer_event)
            self.timer_event = None

    def update_timer(self, dt):
        self.time_left -= 1
        self.timer_label.text = f"Time: {self.time_left}"
        if self.time_left <= 0:
            self.stop_timer()
            self.end_round(time_out=True)

    def check_answer(self, instance):
        self.stop_timer()
        q = self.selected_questions[self.current_question]
        selected_index = self.option_buttons.index(instance)
        correct_index = q["answer"] - 1 # Get the 0-based correct index from the updated 'answer' key

        if selected_index == correct_index:
            instance.background_color = self.BTN_CORRECT
            if self.correct_sound:
                self.correct_sound.play()
            self.total_money += 100
            self.correct_answers += 1
            self.score_label.text = f"Score: {self.total_money}"
            Clock.schedule_once(lambda dt: self.next_question(), 0.6)
        else:
            self.option_buttons[selected_index].background_color = self.BTN_WRONG
            self.option_buttons[correct_index].background_color = self.BTN_CORRECT
            if self.wrong_sound:
                self.wrong_sound.play()
            self.disable_options()
            Clock.schedule_once(lambda dt: self.end_round(), 1.2)

        self.disable_options()

    def disable_options(self):
        for btn in self.option_buttons:
            btn.disabled = True

    def next_question(self):
        self.current_question += 1
        if self.current_question < self.Q_COUNT:
            self.display_question()
        else:
            self.end_round(all_correct=True)

    def end_round(self, time_out=False, all_correct=False):
        if time_out:
            title = "⏰ Time’s up!"
            message = f"You ran out of time.\nMoney won: ₹{self.total_money}"
        elif all_correct:
            title = "🎉 Perfect!"
            message = f"You answered every question!\nTotal: ₹{self.total_money}"
        else:
            title = "Game Over"
            message = f"You won ₹{self.total_money}."

        content = BoxLayout(orientation='vertical', spacing=10, padding=20)
        content.add_widget(Label(text=message, halign="center"))
        btn_row = BoxLayout(size_hint_y=None, height=40, spacing=10)

        restart_btn = Button(text="Play Again", background_color=(0.7, 0.9, 1, 1))
        restart_btn.bind(on_press=self.restart_quiz)
        btn_row.add_widget(restart_btn)

        quit_btn = Button(text="Quit", background_color=(1, 0.7, 0.7, 1))
        quit_btn.bind(on_press=lambda *_: self.stop())
        btn_row.add_widget(quit_btn)

        content.add_widget(btn_row)

        popup = Popup(
            title=title, content=content,
            size_hint=(None, None), size=(400, 240),
            auto_dismiss=False
        )
        popup.open()
        self.end_popup = popup

    def restart_quiz(self, instance):
        self.total_money = 0
        self.correct_answers = 0
        self.selected_questions = random.sample(questions_pool, self.Q_COUNT) # Resample questions for a new game
        self.current_question = 0
        self.score_label.text = "Score: 0"

        if hasattr(self, 'end_popup'):
            self.end_popup.dismiss()
        self.display_question()

    def on_stop(self):
        self.stop_timer()

if __name__ == "__main__":
    QuizApp().run()