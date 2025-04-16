import tkinter as tk
from tkinter import ttk, messagebox, colorchooser
import random
import os
import time
from tkinter import font
from functools import partial
import webbrowser
from PIL import ImageGrab, Image, ImageDraw, ImageFont
import pyperclip


class PointlessConverter:
    """
    The most gloriously pointless unit converter in existence.
    If Einstein were alive, he would either cry or slow-clap.
    """

    def __init__(self, root):
        # Baseline conversion factors - every unit's relationship to feet
        # The true backbone of science, if science had a questionable sense of humor
        self.conversion_factors = {
            # Standard Units (boring but necessary)
            'Meter': 3.28084,
            'Centimeter': 0.0328084,
            'Millimeter': 0.00328084,
            'Kilometer': 3280.84,
            'Inch': 1 / 12,
            'Feet': 1,
            'Yard': 3,
            'Mile': 5280,
            'Nautical Mile': 6076.12,
            'Acre': 43560,  # Area unit, but it's chaotic so why not
            'Fen': 6.00394,  # Chinese unit
            'Furlong': 660,  # Because horses need representation too
            'Fathom': 6,  # Maritime measurement
            'Light Year': 31039437439370,  # For the truly ambitious converters
            'Parsec': 1.01171e+17,  # For when Star Wars fans visit
            'Angstrom': 3.28084e-10,  # For the microscopically inclined
            'League': 15840,  # Perfect for fantasy novel fans

            # Pop Culture Units
            'Football Field (US)': 360,
            'Soccer Field (UK)': 330,
            'Olympic Swimming Pool Length': 164.041995,
            'Wiener Mobile': 60,
            'Millennium Falcon': 114.829396,  # 35 meters in feet
            'TARDIS Exterior': 6.7,  # It's bigger on the inside
            'USS Enterprise': 2379.396,  # NCC-1701 length
            'AT-AT Walker Height': 143.045,  # For Star Wars measurements
            'Minecraft Block': 3.28084,  # 1 meter each
            'Banana For Scale': 0.541667,
            'Hot Dog': 0.5,
            'Hamburger Diameter': 0.333333,
            'Pizza Slice': 0.708,
            'Dorito': 0.125,
            'Xbox Game Pass Card': 0.281250,
            'Nintendo Switch': 0.656,
            'PlayStation 5': 15.35,  # Standing vertically
            'Average Gaming Setup': 5.8,
            'Gaming Mouse': 0.5,
            'DualSense Controller': 0.541,
            'Stack of Pancakes': 0.25,
            'Fortune Cookie': 0.125,
            'LEGO Minifigure': 0.131,
            'Rubiks Cube': 0.22,

            # Animals & Nature
            'Blue Whale': 98.425197,
            'Giraffe Height': 18,
            'Giraffe Neck': 6.0,
            'Elephant (African)': 24.0,
            'Giant Tortoise': 4.0,
            'Tyrannosaurus Rex': 40.0,
            'Velociraptor': 6.56,  # Not the Jurassic Park size
            'Bald Eagle Wingspan': 7.5,
            'Emperor Penguin': 3.94,
            'Lobster (Large)': 1.64,
            'Average House Cat': 1.5,
            'Cat Whisker': 0.0083,
            'Golden Retriever': 2.0,
            'Capybara': 3.28,
            'Hedgehog': 0.66,
            'Sloth': 2.3,
            'Red Ant': 0.0197,  # For extremely small measurements
            'Tardigrade': 0.00066,  # Water bear, virtually indestructible
            'Blue Whale Heart': 5.58,  # The largest heart in the animal kingdom
            'Ostrich Egg': 0.5,
            'Banana Slug': 0.328,
            'Koala': 2.46,
            'Platypus': 1.64,
            'Axolotl': 0.82,
            'Beaver': 2.3,
            'Raccoon': 2.62,
            'Sasquatch Step': 4.0,  # Cryptozoology measurements
            'Loch Ness Monster Neck': 23.0,  # As claimed by eyewitness reports

            # Food & Drink
            'Slice of Bread': 0.041667,
            'Baguette': 2.0833,
            'Croissant': 0.333,
            'Spaghetti Noodle': 0.83,  # Uncooked, standard length
            'Churro': 0.66,
            'Candy Cane': 0.5,
            'Ice Cream Cone': 0.41,
            'Ice Cream Scoop': 0.066667,
            'Chinese Takeaway Container': 0.333333,
            'Standard Burrito': 0.5,
            'California Roll': 0.208,
            'French Fry': 0.25,
            'Taco': 0.33,
            'Lasagna Layer': 0.016,
            'Pretzel': 0.33,
            'Pineapple': 0.66,
            'Watermelon': 1.0,
            'Pickle': 0.33,
            'Chopstick': 0.833,
            'Coffee Bean': 0.0041,
            'Strand of Spaghetti': 0.83,
            'Pizza Box': 1.5,
            'Cup Noodles': 0.333,
            'Cheeto': 0.083,
            'Chicken Nugget': 0.1,
            'Oreo Cookie': 0.0164,
            'Cake Pop': 0.246,

            # Tech & Gadgets
            'USB Port': 0.0459318,
            'iPhone 15': 0.585,
            'iPhone 4': 0.45,  # For retro measurements
            'Nokia 3310': 0.437,  # The indestructible one
            'AirPod': 0.0656,
            'Average Smartphone': 0.157480,
            'HDMI Cable (Standard)': 6.0,
            'Floppy Disk': 0.295,
            'CD/DVD': 0.393701,
            'Vinyl Record (12")': 1.0,
            'USB Flash Drive': 0.246,
            'Laptop (15-inch)': 1.15,
            'Keyboard (Full Size)': 1.5,
            'Apple AirTag': 0.105,
            'Raspberry Pi': 0.21,
            'Arduino Board': 0.246,
            'CPU Chip': 0.15,
            'Graphics Card': 0.9,
            'Ethernet Cable (1m)': 3.28,
            'Toilet Paper Roll': 0.3333,
            'Paper Clip': 0.0328,
            'Sticky Note': 0.25,
            'Tesla Cybertruck': 19.3,

            # Landmarks & Architecture
            'Empire State Building': 1454.0,
            'Eiffel Tower': 1063.0,
            'Great Pyramid of Giza': 481.0,
            'Statue of Liberty': 305.0,
            'Space Needle': 605.0,
            'Great Wall of China Width': 20.0,
            'Golden Gate Bridge Width': 90.0,
            'Stonehenge Stone': 13.12,
            'Mount Everest': 29032.0,
            'Burj Khalifa': 2722.0,
            'Easter Island Head (Moai)': 32.8,
            'Hollywood Sign Letter': 45.0,
            'Big Ben': 315.0,
            'Hollywood Walk of Fame Star': 2.0,
            'London Phone Booth': 8.2021,
            'Red London Telephone Box': 8.2021,  # Duplicate for search compatibility
            'Leaning Tower of Pisa': 183.27,
            'Sydney Opera House': 213.25,
            'Arc de Triomphe': 164.04,
            'Washington Monument': 555.0,
            'Taj Mahal': 240.0,
            'Christ the Redeemer Statue': 98.0,
            'Colosseum Height': 157.0,
            'Roman Colosseum Width': 6.5,
            'CN Tower': 1815.0,
            'Gateway Arch': 630.0,
            'Seattle Space Needle': 605.0,
            'London Eye Capsule': 13.12,
            'Hoover Dam': 726.4,
            'White House': 55.0,
            'Brooklyn Bridge': 1595.8,
            'Grand Canyon Depth': 5249.344,
            'Niagara Falls Height': 167.0,
            'Tokyo Tower': 1092.0,
            'St. Peters Basilica': 449.0,
            'The Shard': 1016.0,

            # Sports & Games
            'Basketball Court (NBA)': 94.0,
            'Hockey Rink': 200.0,
            'Tennis Court Length': 78.0,
            'Tennis Net Length': 42.0,
            'Tennis Racquet': 2.297,
            'Bowling Lane': 60.0,
            'Bowling Pin': 0.25,
            'Ping Pong Table': 9.0,
            'Golf Hole': 0.354,
            'Golf Tee': 0.008333,
            'Baseball Diamond': 90.0,
            'Soccer Goal Width': 24.0,
            'Olympic Diving Platform (10m)': 32.8,
            'Chess Board': 1.312,
            'Chess King Piece': 0.328,
            'Monopoly Board': 1.5,
            'Jenga Tower (Initial Setup)': 0.9,
            'Poker Chip': 0.014,
            'Billiard Ball': 0.085,
            'Billiard Table': 9.0,
            'Football (Soccer Ball)': 0.72,
            'American Football': 0.91,
            'Baseball': 0.246,
            'Hockey Puck': 0.033,
            'Basketball': 0.787,
            'Volleyball': 0.69,
            'Cricket Pitch': 66.0,
            'Badminton Court': 44.0,
            'Badminton Shuttlecock': 0.23,
            'Frisbee': 0.916,

            # Vehicles & Transportation
            'London Bus': 36.083333,
            'London Double Decker Bus': 27.88776,
            'New York City Subway Car': 51.0,
            'Boeing 747': 250.0,
            'Cruise Ship (Average)': 984.25,
            'Volkswagen Beetle (Classic)': 13.45,
            'Vespa Scooter': 5.25,
            'Shopping Cart': 3.28084,
            'Bicycle': 5.740157,
            'School Bus (US)': 40.0,
            'Fire Truck': 35.0,
            'Monster Truck Tire': 5.5,
            'Police Car': 16.4,
            'F1 Race Car': 16.0,
            'Kayak': 13.12,
            'Canoe': 16.4,
            'Jet Ski': 10.0,
            'Rickshaw': 8.2,
            'Segway': 5.249,
            'Hot Air Balloon Basket': 3.9,
            'Helicopter (Average)': 49.2,
            'Smart Car': 8.8,
            'Ambulance': 19.0,
            'Garbage Truck': 30.0,
            'Ice Cream Truck': 18.0,
            'Zamboni': 13.5,
            'Golf Cart': 8.0,
            'Titanic': 882.5,  # Length
            'Saturn V Rocket': 363.0,
            'Space Shuttle': 122.0,
            'International Space Station': 357.0,

            # Household Items
            'Standard Door Height': 6.67,
            'Doorway': 6.88889,
            'King Size Bed': 6.66667,
            'Standard Refrigerator': 6.0,
            'Microwave Oven': 1.5,
            'Grand Piano': 8.2,
            'Bath Tub': 5.0,
            'Shower Curtain': 6.0,
            'Curtain Rod': 5.0,
            'Coffee Table': 3.5,
            'Dining Chair': 3.0,
            'Sofa (3-Seater)': 7.0,
            'Lamp (Table)': 1.64,
            'Floor Lamp': 5.0,
            'Ceiling Fan': 4.0,
            'Standard Window': 5.0,
            'Kitchen Sink': 2.5,
            'Washing Machine': 3.0,
            'Dishwasher': 2.8,
            'Broom': 4.5,
            'Vacuum Cleaner': 4.0,
            'Ironing Board': 5.0,
            'Toilet': 2.5,
            'Towel Rack': 2.0,
            'Coffee Maker': 1.0,
            'Toaster': 0.8,
            'Blender': 1.3,
            'Television (65-inch)': 4.73,  # Diagonal measurement
            'Bookshelf (6ft)': 6.0,
            'Pillow': 2.0,
            'Blanket': 7.0,
            'Doormat': 2.0,
            'Area Rug (5x8)': 8.0,  # Length
            'Flatware (Fork)': 0.66,
            'Dinner Plate': 0.833,
            'Wine Glass': 0.66,
            'Photo Frame (8x10)': 0.833,

            # Clothing & Accessories
            'Sneaker': 0.833333,
            'Top Hat': 1.0,
            'Cowboy Hat': 1.5,
            'Necktie': 4.5,
            'Scarf': 6.0,
            'Belt': 3.5,
            'T-Shirt': 2.5,
            'Formal Dress': 5.0,
            'Wedding Dress Train': 10.0,
            'Sock': 1.0,
            'Glove': 0.833,
            'Wristwatch': 0.33,
            'Sunglasses': 0.5,
            'High Heel': 0.42,
            'Shoelace': 3.0,
            'Wallet': 0.3,
            'Handbag': 1.0,
            'Backpack': 1.5,
            'Umbrella (Open)': 3.5,
            'Umbrella (Closed)': 3.0,
            'Graduation Cap': 0.66,
            'Bowtie': 0.25,
            'Cufflink': 0.033,

            # Human & Anthropology
            'Average Human': 5.6,
            'Average Turkish Grandmother': 5.166667,
            'Average 5-Year-Old': 3.5,
            'NBA Player': 6.7,
            'Sumo Wrestler': 6.0,
            'Human Brain': 0.55,  # Length
            'Human Foot': 0.8,
            'Human Hand Span': 0.66,
            'Human Hair Width': 0.00033,
            'Fingernail': 0.05,
            'Adult Male Arm Span': 5.8,
            'Eyebrow': 0.25,
            'Human Eyelash': 0.042,
            'Beard (Average)': 0.3,
            'Mustache': 0.15,
            'Human Tooth': 0.083,
            'Human Smile': 0.25,
            'Human Step': 2.5,
            'Human Sneeze Distance': 27.0,  # Maximum distance
            'Human Tongue': 0.33,
            'Dad Joke': 0.0,  # Because they have no measurable value
            'British Queue': 3.28084,  # Standard 1 meter queue

            # Fictional & Mythical
            'Hobbit': 3.5,
            'Gandalfs Staff': 6.0,
            'Lightsaber': 4.0,
            'Harry Potters Wand': 1.1,
            'Elder Wand': 1.25,
            'Iron Throne': 13.0,
            'Thors Hammer': 1.5,
            'Captain Americas Shield': 2.5,
            'Infinity Gauntlet': 1.3,
            'Dragon Egg (GoT)': 1.0,
            'One Ring': 0.033,
            'Excalibur': 4.0,
            'Godzilla (2014)': 355.0,
            'King Kong (2005)': 85.0,
            'Unicorn': 8.2,
            'Centaur': 10.0,
            'Fairy': 0.5,
            'Wizards Hat': 1.5,
            'Magic Carpet': 6.0,
            'Dalek': 5.1,
            'Pikachu': 1.31,
            'Charizard': 5.58,
            'Yoda': 2.13,
            'Baby Yoda': 1.15,
            'Jabba the Hutt': 12.0,

            # Internet Culture & Memes
            'Keyboard Cat': 1.5,
            'Nyan Cat': 1.0,
            'Grumpy Cat': 1.0,
            'Doge': 1.0,
            'Big Chungus': 3.0,
            'Meme Attention Span': 0.001,  # Extremely short
            'Social Media Post Lifespan': 0.01,
            'TikTok Dance': 5.0,
            'YouTube Thumbnail': 0.0,  # Digital only
            'Viral Tweet': 0.0,  # Digital only
            'Instagram Influencer Ego': 100.0,  # Exaggerated for comedic effect
            'Reddit Thread': 12.0,  # Average scroll length
            'Karen Complaint': 7.0,  # Length of written complaint
            'Rick Roll': 3.5,  # Height of Rick Astley

            # Random & Absurd
            'Rubber Chicken': 1.5,
            'Stack of $1 Bills ($1 Million)': 358.0,
            'Stack of Printer Paper (500 sheets)': 2.0,
            'Lego Brick (2x4)': 0.11,
            'Broken IKEA Pencil': 0.25,
            'Grain of Rice': 0.022,
            'Human Patience at DMV': 0.001,  # Nearly non-existent
            'Average Attention Span': 0.33,  # Decreasing every year
            'The Space Between Songs': 0.0,  # Conceptual unit
            'Awkward Silence': 9.0,  # Feels much longer than it is
            'Monday Morning': 25.0,  # Feels longer than other mornings
            'Line at Starbucks': 5.0,
            'Public Bathroom Line': 15.0,
            'Traffic Jam': 100.0,  # Seems infinite
            'Waiting for Microwave': 10.0,  # Perception of time
            'Last Hour of Work Day': 15.0,  # Feels longer
            'Zoom Meeting That Could Be An Email': 30.0,
            'Waiting Room Magazine': 0.83,
            'Bed to Bathroom Distance (Night)': 50.0,  # Feels much longer in the dark
            'Empty Pizza Box Disappointment': 18.0,
            'Five More Minutes of Sleep': 0.1,  # Feels much shorter
            'First Coffee Sip Satisfaction': 100.0,  # Immeasurable but we tried
            'That One Song Stuck in Your Head': 24.0,  # Lasts all day
            'Distance to TV Remote When Comfortable': 12.0,  # Always just out of reach
            'Escalator Step': 1.0,
            'School Lunch Table': 8.0,
            'Classroom Chalkboard': 5.0,
            'Office Cubicle': 6.0,
            'Motivational Poster': 3.0,
            'Apple Core': 0.25,
            'Fortune Cookie Paper': 0.6,
            'Unused Gym Membership': 0.0,  # Exists only in principle
            'Belly Button Lint': 0.007,
            'Broken Guitar String': 3.0,
            'Grandpas War Story': 17.0,  # Gets longer each telling
            'Childrens Drawing Height': 2.0,
            'Dust Bunny': 0.15,
            'Bubble Wrap Bubble': 0.03,
            'Air Guitar': 3.5,
        }

        # Ridiculous factoids to display in tooltips
        # Each fact is at least 15% scientifically accurate and 85% fabricated nonsense
        self.pointless_facts = [
            "The T-Rex probably couldn't high-five itself. Tragic.",
            "Banana is the most misunderstood unit of length.",
            "If you stack 7 grandmothers, you'd reach a basketball hoop. Please don't try.",
            "The average person is 0.00000008 Eiffel Towers tall.",
            "Rubber chickens were briefly considered for the metric system.",
            "If the moon were made of cheese, it would be 1.2 trillion Hot Dogs wide.",
            "Scientists confirm: measuring in 'Doritos' is tastier than meters.",
            "A blue whale can swallow 10,000 USB ports in one gulp.",
            "The distance between Paris and New York is approximately 3.7 million baguettes.",
            "Ancient Romans measured roads in 'cat whiskers' until someone realized cats move.",
            "Before computers, people measured data in 'stacks of pancakes'.",
            "Light travels at exactly 983 million London buses per second.",
            "The Mona Lisa's smile is precisely 0.0043 tennis racquets wide.",
            "An average cloud weighs the same as 80 million Chinese takeaway containers.",
            "The human attention span is now shorter than the length of a hot dog. You're welcome.",
            "Antarctica is approximately 4.2 billion golf tees across. Probably.",
            "The deepest part of the ocean is 2.1 million slices of bread deep. Soggy.",
            "A sneeze travels at roughly 38,194 Doritos per second.",
            "If you stretched out all your DNA, it would reach the moon 217 times. Your body is weird.",
            "Statistically, every human has 0.5 croissants in their house right now.",
            "The sun is exactly one sun in diameter. This is the only perfectly precise unit.",
            "The average smartphone contains more bacteria than 6.7 toilet seats. You're touching one.",
            "In medieval France, distances were measured in 'royal nose lengths'. Vive la révolution!",
            "The Earth's core is approximately 7,926 London buses hot.",
            "If all the world's rubber chickens were laid end to end, scientists would have way too much time.",
            "The Internet weighs about as much as a large strawberry. Let that sink in.",
            "The Milky Way is expanding at a rate of 16 Sasquatch steps per century.",
            "An average human brain can store approximately 2.5 million Wiener Mobiles of information.",
            "Most toilets flush in the key of E-flat. You're welcome for this knowledge.",
            "The British queue has been the most consistent unit of measurement since 1066.",
        ]

        # The sacred meme captions for clipboard export
        # These are preserved in the ancient scrolls of internet culture
        self.meme_captions = [
            "My house is {value} {unit} long. Deal with it.",
            "When the teacher asks how tall you are: *{value} {unit}*",
            "Nobody: \nMe: I'm exactly {value} {unit} from the nearest coffee shop.",
            "That's not 6 feet apart, that's {value} {unit} apart!",
            "Dating profile: Must be at least {value} {unit} tall.",
            "When someone asks my weight: About {value} {unit}.",
            "Science class: *exists*\nMe: This room is approximately {value} {unit} wide.",
            "Mission failed successfully: Goal was 10 {unit}, I got {value}.",
            "What's the distance to the moon? About {value} {unit}, obviously.",
            "If I had a dollar for every {unit} in my height, I'd have ${value}.",
            "My online shopping addiction is about {value} {unit} serious.",
            "I'm not late, I was just {value} {unit} away.",
            "2020 felt like it was {value} {unit} long.",
            "Get yourself someone who looks at you from {value} {unit} away.",
            "Relationship status: {value} {unit} from finding love.",
            "Brain capacity: {value} {unit}. Not great, not terrible.",
            "Social distancing? I prefer to stay {value} {unit} away from people anyway.",
            "My patience: *exists*\nKids: We're going to test it for {value} {unit}",
            "My diet plan: Stay {value} {unit} away from the fridge.",
            "My bank account is {value} {unit} of emptiness.",
            "\"How much do you procrastinate?\" Me: About {value} {unit} worth.",
            "My TikTok scrolling session lasted approximately {value} {unit}.",
            "LinkedIn: *Requires 5 years experience*\nMe: I have {value} {unit} of experience.",
            "Boss: \"How's the project coming along?\"\nMe: We're about {value} {unit} from completion.",
            "Doctor: \"How much water do you drink daily?\"\nMe, lying: At least {value} {unit}.",
            "My cooking skills are roughly {value} {unit} on the Gordon Ramsay scale.",
            "Mom: \"How much longer?\"\nMe: Just {value} {unit} more!",
            "The distance between my motivation and my goals: {value} {unit}.",
            "Friend: \"How drunk were you last night?\"\nMe: About {value} {unit} on the scale.",
            "The gap between my expectations and reality: {value} {unit}.",
            "Gym trainer: \"How's your progress?\"\nMe: I've lost {value} {unit} so far!",
            "My existential crisis measures exactly {value} {unit} deep.",
            "When the barista asks for my name: *writes down something {value} {unit} wrong*",
            "That awkward moment when you're {value} {unit} into someone's personal space.",
            "My weekend plans: Sleep for {value} {unit} straight.",
            "Netflix: \"Are you still watching?\"\nMe, {value} {unit} deep in my couch: Yes.",
            "The length of my grocery store receipt: {value} {unit}.",
            "How far I'm willing to walk to avoid small talk: {value} {unit}.",
            "My to-do list is approximately {value} {unit} long, but my motivation is 0.5 {unit}.",
            "Therapist: \"Rate your anxiety\"\nMe: It's about {value} {unit} right now.",
        ]

        # Watermark templates for screenshots
        # Each one more unnecessarily dramatic than the last
        self.watermarks = [
            "Certified Pointless™",
            "Engineered by Baguette Logic",
            "Mathematically Ridiculous",
            "Scientifically Questionable",
            "Pointlessly Accurate",
            "Chaotic Neutral Measurements",
            "Approved by No One Important",
            "Not FDA Approved",
            "Precise Nonsense",
            "Calculated Absurdity",
            "Metric System? We Hardly Know Her",
            "YOLO Units",
            "60% of the Time, It Works Every Time",
            "That's What She Measured",
            "With Great Power Comes Great Convertibility",
            "May The Conversion Be With You",
        ]

        # GUI setup
        self.root = root
        self.root.title("✨ Pointless Converter Extraordinaire ✨")
        self.root.geometry("650x600")
        self.root.resizable(True, True)

        # Set default background color
        self.bg_color = "#f0f0f0"  # Light mode default
        self.text_color = "black"
        self.accent_color = "#4a86e8"  # Default accent color

        # Store current state for dark mode toggle
        self.dark_mode = False

        # Setup main frame with padding
        self.main_frame = tk.Frame(root, bg=self.bg_color, padx=20, pady=20)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create and apply the absurdly magnificent font
        # Comic Sans isn't a crime if used ironically... right?
        try:
            self.title_font = font.Font(family="Comic Sans MS", size=16, weight="bold")
            self.normal_font = font.Font(family="Comic Sans MS", size=11)
            self.result_font = font.Font(family="Comic Sans MS", size=14, weight="bold")
            self.button_font = font.Font(family="Comic Sans MS", size=10)
            self.tooltip_font = font.Font(family="Comic Sans MS", size=9, slant="italic")
        except:
            # Fallback fonts if Comic Sans is unavailable (tragic!)
            self.title_font = font.Font(size=16, weight="bold")
            self.normal_font = font.Font(size=11)
            self.result_font = font.Font(size=14, weight="bold")
            self.button_font = font.Font(size=10)
            self.tooltip_font = font.Font(size=9, slant="italic")

        # Title with unnecessarily dramatic flair
        self.title_label = tk.Label(
            self.main_frame,
            text="✨ Pointless Converter Extraordinaire ✨",
            font=self.title_font,
            bg=self.bg_color,
            fg=self.text_color
        )
        self.title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))

        # Input section
        self.value_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.value_frame.grid(row=1, column=0, columnspan=3, sticky="ew", pady=(0, 10))

        # Value entry
        self.value_label = tk.Label(
            self.value_frame,
            text="Enter Value:",
            font=self.normal_font,
            bg=self.bg_color,
            fg=self.text_color
        )
        self.value_label.pack(side=tk.LEFT, padx=(0, 10))

        # Entry widget with validation
        vcmd = (self.root.register(self.validate_number), '%P')
        self.value_entry = tk.Entry(
            self.value_frame,
            width=15,
            font=self.normal_font,
            validate='key',
            validatecommand=vcmd
        )
        self.value_entry.pack(side=tk.LEFT, padx=(0, 20))
        self.value_entry.insert(0, "42")  # Default value, because it's the answer

        # Conversion frame - contains both dropdown sections
        self.conversion_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.conversion_frame.grid(row=2, column=0, columnspan=3, sticky="ew", pady=(0, 10))

        # From unit frame
        self.from_frame = tk.Frame(self.conversion_frame, bg=self.bg_color)
        self.from_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        # From unit section with search
        self.from_label = tk.Label(
            self.from_frame,
            text="From Unit:",
            font=self.normal_font,
            bg=self.bg_color,
            fg=self.text_color
        )
        self.from_label.pack(anchor=tk.W)

        # Search entry for "from" units
        self.from_search_var = tk.StringVar()
        self.from_search_var.trace("w", self.update_from_dropdown)
        self.from_search_entry = tk.Entry(
            self.from_frame,
            textvariable=self.from_search_var,
            font=self.normal_font,
            width=25
        )
        self.from_search_entry.pack(fill=tk.X, pady=(5, 5))

        # From unit dropdown
        self.from_var = tk.StringVar()
        self.from_dropdown = ttk.Combobox(
            self.from_frame,
            textvariable=self.from_var,
            font=self.normal_font,
            width=25,
            state="readonly"
        )
        self.from_dropdown.pack(fill=tk.X)

        # To unit frame
        self.to_frame = tk.Frame(self.conversion_frame, bg=self.bg_color)
        self.to_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0))

        # To unit section with search
        self.to_label = tk.Label(
            self.to_frame,
            text="To Unit:",
            font=self.normal_font,
            bg=self.bg_color,
            fg=self.text_color
        )
        self.to_label.pack(anchor=tk.W)

        # Search entry for "to" units
        self.to_search_var = tk.StringVar()
        self.to_search_var.trace("w", self.update_to_dropdown)
        self.to_search_entry = tk.Entry(
            self.to_frame,
            textvariable=self.to_search_var,
            font=self.normal_font,
            width=25
        )
        self.to_search_entry.pack(fill=tk.X, pady=(5, 5))

        # To unit dropdown
        self.to_var = tk.StringVar()
        self.to_dropdown = ttk.Combobox(
            self.to_frame,
            textvariable=self.to_var,
            font=self.normal_font,
            width=25,
            state="readonly"
        )
        self.to_dropdown.pack(fill=tk.X)

        # Buttons Frame
        self.button_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.button_frame.grid(row=3, column=0, columnspan=3, pady=(10, 20))

        # Convert button
        self.convert_button = tk.Button(
            self.button_frame,
            text="Convert!",
            font=self.button_font,
            command=self.convert_units,
            bg=self.accent_color,
            fg="white",
            width=15,
            height=2,
            relief=tk.RAISED,
            cursor="hand2"
        )
        self.convert_button.grid(row=0, column=0, padx=5)
        self.setup_tooltip(self.convert_button, "Click to convert with scientific precision-ish")

        # Chaos mode button
        self.chaos_button = tk.Button(
            self.button_frame,
            text="CHAOS MODE",
            font=self.button_font,
            command=self.chaos_mode,
            bg="#ff5722",
            fg="white",
            width=15,
            height=2,
            relief=tk.RAISED,
            cursor="hand2"
        )
        self.chaos_button.grid(row=0, column=1, padx=5)
        self.setup_tooltip(self.chaos_button, "Click if you enjoy mathematical anarchy")

        # Copy to clipboard button
        self.copy_button = tk.Button(
            self.button_frame,
            text="Copy to Clipboard",
            font=self.button_font,
            command=self.copy_to_clipboard,
            width=15,
            height=2,
            relief=tk.RAISED,
            cursor="hand2",
            state=tk.DISABLED  # Initially disabled until conversion occurs
        )
        self.copy_button.grid(row=0, column=2, padx=5)
        self.setup_tooltip(self.copy_button, "Copy result with a meme-worthy caption")

        # Screenshot button
        self.screenshot_button = tk.Button(
            self.button_frame,
            text="Take Screenshot",
            font=self.button_font,
            command=self.take_screenshot,
            width=15,
            height=2,
            relief=tk.RAISED,
            cursor="hand2",
            state=tk.DISABLED  # Initially disabled until conversion occurs
        )
        self.screenshot_button.grid(row=0, column=3, padx=5)
        self.setup_tooltip(self.screenshot_button, "Save this masterpiece for posterity")

        # Add custom unit section
        self.custom_unit_frame = tk.LabelFrame(
            self.main_frame,
            text="Add Your Own Ridiculous Unit",
            font=self.normal_font,
            bg=self.bg_color,
            fg=self.text_color,
            padx=10,
            pady=10
        )
        self.custom_unit_frame.grid(row=4, column=0, columnspan=3, sticky="ew", pady=(0, 20))

        # Unit name entry
        self.unit_name_label = tk.Label(
            self.custom_unit_frame,
            text="Unit Name:",
            font=self.normal_font,
            bg=self.bg_color,
            fg=self.text_color
        )
        self.unit_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.unit_name_entry = tk.Entry(
            self.custom_unit_frame,
            font=self.normal_font,
            width=20
        )
        self.unit_name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Conversion factor entry
        self.factor_label = tk.Label(
            self.custom_unit_frame,
            text="Length in Feet:",
            font=self.normal_font,
            bg=self.bg_color,
            fg=self.text_color
        )
        self.factor_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        vcmd2 = (self.root.register(self.validate_number), '%P')
        self.factor_entry = tk.Entry(
            self.custom_unit_frame,
            font=self.normal_font,
            width=20,
            validate='key',
            validatecommand=vcmd2
        )
        self.factor_entry.grid(row=1, column=1, padx=5, pady=5)

        # Add unit button
        self.add_unit_button = tk.Button(
            self.custom_unit_frame,
            text="Add Unit",
            font=self.button_font,
            command=self.add_custom_unit,
            bg=self.accent_color,
            fg="white",
            width=15,
            relief=tk.RAISED,
            cursor="hand2"
        )
        self.add_unit_button.grid(row=1, column=2, padx=10, pady=5)
        self.setup_tooltip(self.add_unit_button, "Add your unit to the chaotic collection")

        # Result display (initially hidden)
        self.result_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.result_frame.grid(row=5, column=0, columnspan=3, sticky="ew", pady=(0, 10))
        self.result_frame.grid_remove()  # Initially hidden

        self.result_label = tk.Label(
            self.result_frame,
            text="",
            font=self.result_font,
            bg=self.bg_color,
            fg="#2e7d32",  # Green for results
            wraplength=600,
            justify=tk.CENTER
        )
        self.result_label.pack(fill=tk.X, pady=10)

        # Bottom toolbar frame
        self.toolbar_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.toolbar_frame.grid(row=6, column=0, columnspan=3, sticky="ew", pady=(10, 0))

        # Dark mode toggle
        self.dark_mode_btn = tk.Button(
            self.toolbar_frame,
            text="☀️ UNLEASH THE VOID ☀️",
            font=self.button_font,
            command=self.toggle_dark_mode,
            bg="#333333",
            fg="white",
            relief=tk.RAISED,
            cursor="hand2"
        )
        self.dark_mode_btn.pack(side=tk.LEFT, padx=5)
        self.setup_tooltip(self.dark_mode_btn, "Toggle between enlightenment and darkness")

        # Color picker for accent colors
        self.color_btn = tk.Button(
            self.toolbar_frame,
            text="🎨 Change Accent",
            font=self.button_font,
            command=self.choose_accent_color,
            relief=tk.RAISED,
            cursor="hand2"
        )
        self.color_btn.pack(side=tk.LEFT, padx=5)
        self.setup_tooltip(self.color_btn, "Make this app as colorful as your personality")

        # About button
        self.about_btn = tk.Button(
            self.toolbar_frame,
            text="ℹ️ About",
            font=self.button_font,
            command=self.show_about,
            relief=tk.RAISED,
            cursor="hand2"
        )
        self.about_btn.pack(side=tk.RIGHT, padx=5)
        self.setup_tooltip(self.about_btn, "Learn about this magnificent creation")

        # Create a tooltip variable that will store the tooltip window
        self.tooltip_window = None

        # Set default style for dropdowns
        self.style = ttk.Style()
        self.style.configure("TCombobox",
                             fieldbackground=self.bg_color,
                             background=self.bg_color)

        # Now that all UI elements are created, update dropdown lists and set defaults
        self.update_unit_lists()
        self.from_dropdown.set("Meter")  # Default value
        self.to_dropdown.set("Rubber Chicken")  # Default value

    def validate_number(self, value):
        """
        Ensures the user inputs only valid numbers.
        Because even in chaos, some rules must exist.
        """
        # Allow empty values
        if value == "":
            return True

        # Allow negative sign at beginning
        if value == "-":
            return True

        # Allow decimal point (but only one)
        if value.count('.') <= 1:
            # Check if value with possible decimal is a valid float
            try:
                # Remove decimal point for checking
                test_value = value.replace('.', '')
                # Allow negative sign at start
                if test_value.startswith('-'):
                    test_value = test_value[1:]
                # Check if remaining characters are all digits
                return test_value == '' or test_value.isdigit()
            except:
                return False
        return False

    def update_unit_lists(self):
        """
        Updates the dropdown lists with current units.
        Like restocking a shelf with increasingly absurd products.
        """
        unit_list = sorted(list(self.conversion_factors.keys()))
        self.from_dropdown['values'] = unit_list
        self.to_dropdown['values'] = unit_list

    def update_from_dropdown(self, *args):
        """
        Filters the "from" dropdown based on search input.
        Like using a metal detector to find specific rubber chickens.
        """
        search_term = self.from_search_var.get().lower()
        all_units = sorted(list(self.conversion_factors.keys()))
        if search_term:
            filtered_units = [unit for unit in all_units if search_term in unit.lower()]
            self.from_dropdown['values'] = filtered_units
        else:
            self.from_dropdown['values'] = all_units

    def update_to_dropdown(self, *args):
        """
        Filters the "to" dropdown based on search input.
        Because scrolling is so 2022.
        """
        search_term = self.to_search_var.get().lower()
        all_units = sorted(list(self.conversion_factors.keys()))
        if search_term:
            filtered_units = [unit for unit in all_units if search_term in unit.lower()]
            self.to_dropdown['values'] = filtered_units
        else:
            self.to_dropdown['values'] = all_units

    def convert_units(self):
        """
        The heart of our pointless science - converting one arbitrary unit to another.
        Einstein would be so proud. Or confused. Probably confused.
        """
        try:
            # Get input values
            value_str = self.value_entry.get()
            if not value_str:
                messagebox.showerror("Error", "Please enter a value! Even chaos needs numbers.")
                return

            value = float(value_str)
            from_unit = self.from_var.get()
            to_unit = self.to_var.get()

            if not from_unit or not to_unit:
                messagebox.showerror("Error", "Please select both units! I can't read minds... yet.")
                return

            # Convert from input unit to feet first
            feet_value = value * self.conversion_factors[from_unit]

            # Then convert from feet to target unit
            result = feet_value / self.conversion_factors[to_unit]

            # Round to 4 decimal places for sanity
            result_rounded = round(result, 4)

            # Generate a witty suffix
            suffixes = [
                "Cluck wisely.",
                "Science has spoken.",
                "Don't question it.",
                "Write that down! WRITE THAT DOWN!",
                "Nobel Prize pending.",
                "Your tax dollars at work.",
                "Mathematically dubious, but technically correct.",
                "The best kind of correct!",
                "Please don't cite this in your thesis.",
                "Peer-reviewed by my cat.",
                "That's just, like, the math, man.",
                "Even Einstein would be confused.",
                "Quantum mechanics explains the rest.",
                "Algorithms don't lie, people do.",
                "60% of the time, it's accurate every time.",
                "This has been a test of the emergency conversion system.",
                "I hope you're writing this down.",
                "Numbers don't lie, but this app might.",
                "Eureka! Or whatever.",
                "Just trust me on this one.",
            ]

            suffix = random.choice(suffixes)

            # Display result
            result_text = f"{value} {from_unit}{'' if from_unit.endswith('s') else ''} "
            result_text += f"= {result_rounded} {to_unit}{'' if to_unit.endswith('s') else 's'}. {suffix}"

            # Show result frame if it's hidden
            self.result_frame.grid()
            self.result_label.config(text=result_text)

            # Enable copy and screenshot buttons now that we have a result
            self.copy_button.config(state=tk.NORMAL)
            self.screenshot_button.config(state=tk.NORMAL)

            # Store the result for clipboard and screenshot functions
            self.last_result = {
                "value": value,
                "from_unit": from_unit,
                "to_unit": to_unit,
                "result": result_rounded,
                "text": result_text
            }

            # Flash the result with a delightful colorful celebration
            self.flash_result()

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number! Letters are for words, not math.")
        except Exception as e:
            messagebox.showerror("Error", f"Something went terribly wrong: {str(e)}")

    def chaos_mode(self):
        """
        Let the gods of randomness decide your units of measurement!
        The closest thing to mathematical anarchy you'll experience today.
        """
        # Get all available units
        all_units = list(self.conversion_factors.keys())

        # Select random units
        from_unit = random.choice(all_units)
        to_unit = random.choice(all_units)

        # Get a random value between 1 and 1000
        value = round(random.uniform(1, 1000), 2)

        # Update UI
        self.value_entry.delete(0, tk.END)
        self.value_entry.insert(0, str(value))

        # Set the selected units
        self.from_var.set(from_unit)
        self.to_var.set(to_unit)

        # Clear search fields
        self.from_search_var.set("")
        self.to_search_var.set("")

        # Convert the units with dramatic flair
        self.root.after(100, lambda: self.chaos_animation(5))

    def chaos_animation(self, remaining):
        """
        Creates a chaotic animation effect for Chaos Mode.
        Because normal conversions are too bourgeois.
        """
        if remaining <= 0:
            # Animation complete, perform the actual conversion
            self.convert_units()
            return

        # Temporary visual chaos
        all_units = list(self.conversion_factors.keys())
        self.from_var.set(random.choice(all_units))
        self.to_var.set(random.choice(all_units))

        # Flash background with random colors
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = f'#{r:02x}{g:02x}{b:02x}'

        # Flash the result frame
        self.result_frame.grid()
        self.result_label.config(text="CALCULATING CHAOS...", fg=color)

        # Schedule the next animation frame
        self.root.after(150, lambda: self.chaos_animation(remaining - 1))

    def add_custom_unit(self):
        """
        Allows users to add their own made-up units to the collection.
        Because freedom of measurement is a basic human right.
        """
        unit_name = self.unit_name_entry.get().strip()
        factor_str = self.factor_entry.get().strip()

        # Validate inputs
        if not unit_name:
            messagebox.showerror("Error", "Please enter a name for your unit! Even chaos needs labels.")
            return

        if not factor_str:
            messagebox.showerror("Error", "Please enter a conversion factor! How big is this thing?")
            return

        try:
            factor = float(factor_str)
            if factor <= 0:
                messagebox.showerror("Error",
                                     "Factor must be positive! Negative dimensions tear the fabric of space-time.")
                return

            # Check if unit already exists
            if unit_name in self.conversion_factors:
                overwrite = messagebox.askyesno("Unit exists",
                                                f"{unit_name} already exists! Would you like to redefine it?")
                if not overwrite:
                    return

            # Add the new unit
            self.conversion_factors[unit_name] = factor

            # Update the dropdowns
            self.update_unit_lists()

            # Clear the inputs
            self.unit_name_entry.delete(0, tk.END)
            self.factor_entry.delete(0, tk.END)

            # Select the new unit in the "to" dropdown
            self.to_var.set(unit_name)

            messagebox.showinfo("Success", f"'{unit_name}' has been added to the pantheon of pointless units!")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for the conversion factor!")

    def copy_to_clipboard(self):
        """
        Copies the result to clipboard with a meme-worthy caption.
        Because social media demands precision with attitude.
        """
        if not hasattr(self, 'last_result'):
            messagebox.showerror("Error", "Need to convert something first!")
            return

        # Get a random meme caption
        caption_template = random.choice(self.meme_captions)

        # Format with the conversion result
        caption = caption_template.format(
            value=self.last_result["result"],
            unit=self.last_result["to_unit"]
        )

        # Copy to clipboard
        pyperclip.copy(caption)

        # Flash the button to indicate success
        original_bg = self.copy_button.cget("background")
        self.copy_button.config(bg="green")
        self.root.after(500, lambda: self.copy_button.config(bg=original_bg))

        # Briefly show a success message
        temp_label = tk.Label(
            self.result_frame,
            text="Copied to clipboard! Spread the chaos!",
            font=self.tooltip_font,
            bg=self.bg_color,
            fg="green"
        )
        temp_label.pack(fill=tk.X)
        self.root.after(2000, temp_label.destroy)

    def take_screenshot(self):
        """
        Takes a screenshot of the app with a pointless watermark.
        Perfect for sharing your mathematical absurdity.
        """
        if not hasattr(self, 'last_result'):
            messagebox.showerror("Error", "Convert something first! Can't screenshot a void.")
            return

        try:
            # Get window position
            x = self.root.winfo_rootx()
            y = self.root.winfo_rooty()
            width = self.root.winfo_width()
            height = self.root.winfo_height()

            # Take screenshot
            screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))

            # Add watermark
            watermark_text = random.choice(self.watermarks)

            # Draw watermark
            draw = ImageDraw.Draw(screenshot)

            # Try to load a fun font, fall back to default
            try:
                # Try for Comic Sans first (of course)
                watermark_font = ImageFont.truetype("Comic Sans MS", 36)
            except:
                try:
                    # Try Arial as fallback
                    watermark_font = ImageFont.truetype("Arial", 36)
                except:
                    # Last resort: default font
                    watermark_font = ImageFont.load_default()

            # Get text size
            text_width, text_height = draw.textsize(watermark_text, font=watermark_font)

            # Position text in bottom right with slight angle
            position = (width - text_width - 20, height - text_height - 20)

            # Add semi-transparent background for watermark
            text_bg_coords = (
                position[0] - 10,
                position[1] - 10,
                position[0] + text_width + 10,
                position[1] + text_height + 10
            )
            draw.rectangle(text_bg_coords, fill=(255, 255, 255, 128))

            # Draw text with shadow effect
            draw.text((position[0] + 2, position[1] + 2), watermark_text, font=watermark_font, fill=(0, 0, 0, 128))
            draw.text(position, watermark_text, font=watermark_font, fill=(255, 0, 0, 255))

            # Save the screenshot
            # Generate filename based on the conversion
            filename = f"pointless_conversion_{int(time.time())}.png"
            save_path = os.path.join(os.path.expanduser("~"), "Pictures")

            # Try to save to Pictures folder, fall back to current directory
            try:
                if not os.path.exists(save_path):
                    os.makedirs(save_path)
                full_path = os.path.join(save_path, filename)
            except:
                # Fallback to current directory
                full_path = filename

            screenshot.save(full_path)

            # Show success message with path
            messagebox.showinfo("Screenshot Saved",
                                f"Your pointless conversion has been immortalized!\nSaved to: {full_path}")

        except Exception as e:
            messagebox.showerror("Screenshot Error", f"Failed to take screenshot: {str(e)}")

    def flash_result(self):
        """
        Flashes the result with colorful celebration.
        Because plain text results are for calculators, not ARTISTS.
        """
        colors = ["#4CAF50", "#2196F3", "#9C27B0", "#FF9800", "#E91E63"]
        original_color = self.result_label.cget("fg")

        def flash_step(step=0):
            if step >= 5:  # Number of flashes
                self.result_label.config(fg=original_color)
                return
            color = colors[step % len(colors)]
            self.result_label.config(fg=color)
            self.root.after(200, lambda: flash_step(step + 1))

        flash_step()

    def toggle_dark_mode(self):
        """
        Toggles between light and dark modes.
        Because even pointless apps need aesthetic options.
        """
        self.dark_mode = not self.dark_mode

        if self.dark_mode:
            # Dark mode
            self.bg_color = "#333333"
            self.text_color = "#FFFFFF"
            self.dark_mode_btn.config(text="🌙 RETURN TO LIGHT 🌙")
        else:
            # Light mode
            self.bg_color = "#F0F0F0"
            self.text_color = "#000000"
            self.dark_mode_btn.config(text="☀️ UNLEASH THE VOID ☀️")

        # Update main frame
        self.main_frame.config(bg=self.bg_color)

        # Update all widgets with background and text colors
        for widget in self.main_frame.winfo_children():
            widget_type = widget.winfo_class()
            if widget_type in ("Frame", "Labelframe"):
                widget.config(bg=self.bg_color)
                # Recursively update children
                for child in widget.winfo_children():
                    child_type = child.winfo_class()
                    if child_type in ("Label", "Frame"):
                        child.config(bg=self.bg_color)
                        if child_type == "Label":
                            child.config(fg=self.text_color)
            elif widget_type == "Label":
                widget.config(bg=self.bg_color, fg=self.text_color)

        # Special handling for result label to keep its color
        self.result_label.config(bg=self.bg_color)

        # Update the LabelFrame text color
        self.custom_unit_frame.config(bg=self.bg_color, fg=self.text_color)

        # Update combobox colors
        self.style.configure("TCombobox",
                             fieldbackground=self.bg_color,
                             background=self.bg_color)

        # Special handling for nested frames
        for frame in [self.value_frame, self.conversion_frame, self.from_frame,
                      self.to_frame, self.result_frame, self.toolbar_frame]:
            frame.config(bg=self.bg_color)
            for child in frame.winfo_children():
                if child.winfo_class() == "Label":
                    child.config(bg=self.bg_color, fg=self.text_color)

    def choose_accent_color(self):
        """
        Opens a color picker to customize the accent color.
        Because personalization is the essence of pointlessness.
        """
        color = colorchooser.askcolor(initialcolor=self.accent_color)
        if color[1]:  # If a color was selected (not canceled)
            self.accent_color = color[1]
            # Update buttons with the new accent color
            self.convert_button.config(bg=self.accent_color)
            self.add_unit_button.config(bg=self.accent_color)

    def setup_tooltip(self, widget, text):
        """
        Creates a tooltip for a widget.
        Because hovering should always be rewarded with useless information.
        """
        widget.bind("<Enter>", lambda event, t=text: self.show_tooltip(event, t))
        widget.bind("<Leave>", self.hide_tooltip)
        widget.bind("<Motion>", self.update_tooltip_position)

    def show_tooltip(self, event, text):
        """
        Displays a tooltip with text and a random pointless fact.
        Knowledge is power, even when it's completely irrelevant.
        """
        # Add a random fact to tooltips sometimes
        if random.random() < 0.3:  # 30% chance of showing a random fact
            fact = random.choice(self.pointless_facts)
            tooltip_text = f"{text}\n\nDID YOU KNOW? {fact}"
        else:
            tooltip_text = text

        x, y, _, _ = event.widget.bbox("insert")
        x += event.widget.winfo_rootx() + 25
        y += event.widget.winfo_rooty() + 25

        # Destroy existing tooltip if it exists
        self.hide_tooltip(None)

        # Create tooltip window
        self.tooltip_window = tk.Toplevel(event.widget)
        self.tooltip_window.wm_overrideredirect(True)  # Remove window decorations
        self.tooltip_window.wm_geometry(f"+{x}+{y}")

        # Create tooltip content
        tooltip_frame = tk.Frame(self.tooltip_window, bg="#FFFFDD", bd=1, relief="solid")
        tooltip_frame.pack(fill="both", expand=True)

        label = tk.Label(tooltip_frame, text=tooltip_text,
                         font=self.tooltip_font, bg="#FFFFDD",
                         fg="black", justify="left", wraplength=250,
                         padx=5, pady=5)
        label.pack()

    def hide_tooltip(self, event):
        """
        Hides the tooltip window.
        All good things must come to an end, including pointless tooltips.
        """
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None

    def update_tooltip_position(self, event):
        """
        Updates the tooltip position when mouse moves.
        It follows your cursor like an eager puppy.
        """
        if self.tooltip_window:
            x = event.x_root + 15
            y = event.y_root + 10
            self.tooltip_window.wm_geometry(f"+{x}+{y}")

    def show_about(self):
        """
        Displays information about this majestic app.
        History shall remember this day.
        """
        about_text = """
        ✨ The Pointless Converter Extraordinaire ✨

        A monument to beautiful mathematical chaos.

        Created with love, excessive caffeine, and 
        questionable life choices by WhiskeyCoder.

        Remember: All conversions are 100% accurate*

        * ±500% margin of error may apply
        """

        about_window = tk.Toplevel(self.root)
        about_window.title("About This Masterpiece")
        about_window.geometry("400x300")
        about_window.resizable(False, False)

        # Center the window
        about_window.geometry("+%d+%d" % (
            self.root.winfo_rootx() + self.root.winfo_width() // 2 - 200,
            self.root.winfo_rooty() + self.root.winfo_height() // 2 - 150
        ))

        # Add content
        frame = tk.Frame(about_window, padx=20, pady=20)
        frame.pack(fill=tk.BOTH, expand=True)

        # Title
        tk.Label(frame, text="✨ Pointless Converter Extraordinaire ✨",
                 font=("Comic Sans MS", 14, "bold")).pack(pady=(0, 20))

        # About text
        tk.Label(frame, text=about_text, justify=tk.CENTER,
                 font=("Comic Sans MS", 10)).pack(pady=10)

        # Version
        tk.Label(frame, text="Version 2.0 - Even More Pointless™",
                 font=("Comic Sans MS", 8, "italic")).pack(pady=(20, 5))

        # Close button
        tk.Button(frame, text="Magnifique!", font=("Comic Sans MS", 10, "bold"),
                  command=about_window.destroy).pack(pady=10)


def main():
    """
    The main function that launches our chaotic masterpiece.
    Witness the birth of pointless measurement history.
    """
    try:
        root = tk.Tk()
        app = PointlessConverter(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Critical Error", f"Something catastrophic happened: {str(e)}\n\nEven chaos has limits.")


if __name__ == "__main__":
    main()
