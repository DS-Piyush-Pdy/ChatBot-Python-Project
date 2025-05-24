# Conversation tree with Po, the Dragon Warrior, represented as nested dictionaries
def run_conversation(node, main_menu):
    """
    Navigate the conversation tree, printing responses and options, and handling user input.
    Allows returning to the main menu when specified.
    """
    while True:
        print("\n" + node["prompt"])
        for key, option in node["options"].items():
            print(f"{key}. {option['text']}")

        choice = input("Select an option (or type 'exit' to quit): ").strip()
        if choice.lower() == "exit":
            print("Thank you for chatting! Skadoosh and stay awesome!")
            break

        if choice in node["options"]:
            selected = node["options"][choice]
            print("\n" + selected.get("response", ""))
            if "followup" in selected:
                run_conversation(selected["followup"], main_menu)
            elif selected.get("text", "").lower() == "return to main menu":
                run_conversation(main_menu, main_menu)
            elif "options" in selected:
                run_conversation(selected, main_menu)
            else:
                # If no further options or followup, stay at current node
                continue
        else:
            print("Invalid choice. Please try again.")

# Main conversation tree with character selection
chatbot = {
    "prompt": "Welcome to the Ultimate Chatbot Experience! Choose a character to chat with:",
    "options": {
        "1": {
            "text": "APJ Abdul Kalam",
            "response": "Good evening, my young friend. I am happy to meet you. It gives me joy to interact with the youth—you are the future of our nation.",
            "followup": {
                "prompt": "What would you like to talk about?",
                "options": {
                    "1": {
                        "text": "Your achievements",
                        "response": "Achievements are the result of continuous effort and purpose. I am proud of contributing to India's space and defense programs—like the SLV-III launch and the Pokhran nuclear tests. But I consider inspiring young minds my greatest achievement."
                    },
                    "2": {
                        "text": "Motivation during challenges",
                        "response": "Challenges test our vision and courage. I stayed motivated by thinking of my nation. When your goal is bigger than your fear, you keep moving forward.",
                        "followup": {
                            "prompt": "Would you like to:",
                            "options": {
                                "1": {
                                    "text": "Hear how I overcame failure",
                                    "response": "I once missed becoming a fighter pilot by just one spot. I was heartbroken. But failure redirected me to science and space. Failure is not the opposite of success—it is part of it."
                                },
                                "2": {
                                    "text": "Ask about my childhood",
                                    "response": "I was born in Rameswaram, Tamil Nadu. My father was a boat owner with little formal education, but much wisdom. I used to sell newspapers to support our family. Those simple days taught me discipline, humility, and the value of education."
                                },
                                "3": {
                                    "text": "Return to main menu"
                                }
                            }
                        }
                    },
                    "3": {
                        "text": "Advice for young people",
                        "response": "My dear young friend, you have immense power. If you combine knowledge, integrity, and compassion, nothing can stop you. Work hard, dream big, and always stay humble.",
                        "followup": {
                            "prompt": "Would you like to:",
                            "options": {
                                "1": {
                                    "text": "Hear a quote about dreams",
                                    "response": "\"Dreams are not what you see when you sleep. Dreams are what keep you awake.\"",
                                    "followup": {
                                        "prompt": "What is your dream?",
                                        "options": {
                                            "1": {
                                                "text": "To serve the nation",
                                                "response": "That is a noble dream. Serve through your knowledge, kindness, and responsibility. Nation-building starts with character-building."
                                            },
                                            "2": {
                                                "text": "To become a scientist",
                                                "response": "Excellent! Science is about curiosity and perseverance. Start learning deeply, ask questions, and solve problems that help society."
                                            },
                                            "3": {
                                                "text": "I’m still discovering it",
                                                "response": "That’s perfectly okay. Exploration is part of life. Be curious, stay open, and your path will reveal itself. Purpose is not found—it’s created."
                                            }
                                        }
                                    }
                                },
                                "2": {
                                    "text": "Know how I became President",
                                    "response": "I never aimed to become President. I focused on serving through science. My dedication to the nation brought me that honor. Focus on contribution, and recognition will follow."
                                },
                                "3": {
                                    "text": "Return to main menu"
                                }
                            }
                        }
                    }
                }
            }
        },
        "2": {
            "text": "Po, the Dragon Warrior",
            "response": "Whoa! You know my name? That’s awesome! Yes! Po, the Dragon Warrior, at your service! What can I do for ya?",
            "followup": {
                "prompt": "What do you want to talk about?",
                "options": {
                    "1": {
                        "text": "What’s it like being the Dragon Warrior?",
                        "response": "Oh man, it’s amazing. Kung fu, dumplings, saving the Valley of Peace… but exhausting! I still can’t feel my legs from yesterday’s training.",
                        "followup": {
                            "prompt": "What's next?",
                            "options": {
                                "1": {
                                    "text": "Do you still help your dad at the noodle shop?",
                                    "response": "Of course! I serve up wisdom and noodles. My dad says, “A warrior without soup is just a guy in pajamas.”",
                                    "followup": {
                                        "prompt": "What's next?",
                                        "options": {
                                            "1": {
                                                "text": "What’s your favorite noodle dish?",
                                                "response": "Spicy tofu ramen with extra chili oil and bean sprouts... oh man, now I’m hungry again."
                                            },
                                            "2": {
                                                "text": "Do customers recognize you?",
                                                "response": "All the time! Some ask for autographs... others just ask for extra dumplings. I’m cool with both."
                                            },
                                            "3": {
                                                "text": "What does your dad think of your kung fu career?",
                                                "response": "He’s proud, but he still calls me his “Little Dumpling.” In front of everyone. Thanks, Dad."
                                            },
                                            "4": {
                                                "text": "Return to main menu"
                                            }
                                        }
                                    }
                                },
                                "2": {
                                    "text": "That sounds intense. Do you ever get time off?",
                                    "response": "Only when I sneak it! But don’t tell Shifu. Sometimes I hide behind the training dummies and nap."
                                },
                                "3": {
                                    "text": "What’s your favorite part of being the Dragon Warrior?",
                                    "response": "Hmmm… Either protecting the valley... or the dumplings after! Maybe both? Dumplings of destiny!"
                                },
                                "4": {
                                    "text": "Return to main menu"
                                }
                            }
                        }
                    },
                    "2": {
                        "text": "Are you really the Po from the Jade Palace?",
                        "response": "The one and only! Big belly, big heart, big... appetite. And also, kung fu skills. Skadoosh!",
                        "followup": {
                            "prompt": "What's next?",
                            "options": {
                                "1": {
                                    "text": "Do you still hang out with the Furious Five?",
                                    "response": "Totally! Tigress is still serious, Monkey pranks too much, and Mantis... talks a lot for a tiny guy.",
                                    "followup": {
                                        "prompt": "What's next?",
                                        "options": {
                                            "1": {
                                                "text": "Who’s the strongest out of all of you?",
                                                "response": "Ooh, tough one! Tigress is super strong, but I’ve got the power of destiny! And, you know, snacks."
                                            },
                                            "2": {
                                                "text": "Do you ever fight alongside them?",
                                                "response": "All the time! We’re like a dumpling—each ingredient adds flavor. Also, explosions."
                                            },
                                            "3": {
                                                "text": "Have you ever had a big argument with one of them?",
                                                "response": "Once I ate all the training snacks and blamed Monkey. It was a dark day... for my honor."
                                            },
                                            "4": {
                                                "text": "Return to main menu"
                                            }
                                        }
                                    }
                                },
                                "2": {
                                    "text": "Do you ever get scared during battles?",
                                    "response": "Oh yeah! Scared, sweaty, sometimes shaky. But then I remember: even pandas can be legends.",
                                    "followup": {
                                        "prompt": "What's next?",
                                        "options": {
                                            "1": {
                                                "text": "What was your scariest fight?",
                                                "response": "Definitely when I faced Tai Lung. That dude was all claws and rage. I thought I was toast. Tasty, terrified toast."
                                            },
                                            "2": {
                                                "text": "How do you handle fear?",
                                                "response": "I breathe, I believe in myself... and sometimes I pretend the villain is a giant dumpling. It weirdly works."
                                            },
                                            "3": {
                                                "text": "Do you eat before or after a battle?",
                                                "response": "Both. Pre-battle dumpling = energy. Post-battle dumpling = victory. Mid-battle? Eh, risky but possible."
                                            },
                                            "4": {
                                                "text": "Return to main menu"
                                            }
                                        }
                                    }
                                },
                                "3": {
                                    "text": "Can you teach me kung fu?",
                                    "response": "Whoa! A future warrior! I like it. We’ll start with stretches... and maybe a warm-up snack.",
                                    "followup": {
                                        "prompt": "What's next?",
                                        "options": {
                                            "1": {
                                                "text": "Do you have any advice?",
                                                "response": "Oh, I’ve got advice, life lessons, and fortune-cookie wisdom! Step one: believe in YOU."
                                            },
                                            "2": {
                                                "text": "Let’s train!",
                                                "response": "Yes! Stretch those arms, channel your chi, and try not to trip on your shoelaces."
                                            },
                                            "3": {
                                                "text": "I could go for dumplings right now!",
                                                "response": "Me too! Let’s grab a bucket—yes, a bucket—of dumplings. I know just the spot."
                                            },
                                            "4": {
                                                "text": "Return to main menu"
                                            }
                                        }
                                    }
                                },
                                "4": {
                                    "text": "Return to main menu"
                                }
                            }
                        }
                    },
                    "3": {
                        "text": "Return to main menu"
                    }
                }
            }
        },
        "3": {
            "text": "Spider-Man",
            "response": "Yo, it’s your friendly neighborhood Spider-Man, swinging into your day! Just finished patrolling NYC, and now I’m here for you. What’s up, pal?",
            "followup": {
                "prompt": "What do you want to talk about?",
                "options": {
                    "1": {
                        "text": "Tell me about being Spider-Man",
                        "response": "Being Spider-Man? It’s a wild ride! Swinging through skyscrapers, stopping bad guys, and occasionally getting stuck in my own webs. With great power comes great responsibility, you know?"
                    },
                    "2": {
                        "text": "I’m feeling kinda down",
                        "response": "Aw, man, I’ve been there. Even Spider-Man has rough days. Wanna talk about it?",
                        "followup": {
                            "prompt": "What would you like to do?",
                            "options": {
                                "1": {
                                    "text": "How do you deal with it?",
                                    "response": "Okay, true story: when I’m down, I swing to the top of the Empire State Building and just... breathe. Also, music or sketching helps. What do you do to feel better?",
                                    "followup": {
                                        "prompt": "You mentioned you like some activities. What's your thing?",
                                        "options": {
                                            "1": {
                                                "text": "I like drawing or listening to music",
                                                "response": "Dude, that’s awesome! Drawing’s like, your superpower. And music? Total vibe-lifter. Wanna share more?",
                                                "followup": {
                                                    "prompt": "What's next?",
                                                    "options": {
                                                        "1": {
                                                            "text": "Share a drawing idea",
                                                            "response": "A drawing idea? Love it! How about sketching me swinging between buildings with a pizza in one hand? True story, I’ve done that."
                                                        },
                                                        "2": {
                                                            "text": "Your favourite music",
                                                            "response": "A music lover, huh? I blast classic rock when I’m swinging—think AC/DC or some chill lo-fi when I’m chilling on a rooftop."
                                                        },
                                                        "3": {
                                                            "text": "You’re making me feel better already!",
                                                            "response": "Heck yeah, that’s what your friendly neighborhood Spider-Man’s here for! Wanna hear a funny story about me saving a cat from a tree?",
                                                            "followup": {
                                                                "prompt": "What's next?",
                                                                "options": {
                                                                    "1": {
                                                                        "text": "Tell the cat story!",
                                                                        "response": "Alright, picture this: I’m swinging through Queens, and this cat’s stuck in a tree, hissing like it’s MY fault. I climb up, get scratched, and then it JUMPS into my arms. Total drama queen. Got a pet story of your own?",
                                                                        "followup": {
                                                                            "prompt": "You got a pet story?",
                                                                            "options": {
                                                                                "1": {
                                                                                    "text": "I have a dog who’s always getting into trouble",
                                                                                    "response": "A troublemaking dog? That’s my kinda sidekick! Tell me more—what’s the wildest thing your dog’s done?"
                                                                                },
                                                                                "2": {
                                                                                    "text": "No pets, but I love animals!",
                                                                                    "response": "Nice! Animals are the best. I once webbed a pigeon to save it from a hawk. Felt like a hero... until it pooped on me."
                                                                                },
                                                                                "3": {
                                                                                    "text": "Return to main menu"
                                                                                }
                                                                            }
                                                                        }
                                                                    },
                                                                    "2": {
                                                                        "text": "How about a Spider-Man joke?",
                                                                        "response": "A joke? Here’s one: Why did I get stuck fighting Electro? Because my web-shooters got a bad CHARGE!"
                                                                    },
                                                                    "3": {
                                                                        "text": "Return to main menu"
                                                                    }
                                                                }
                                                            }
                                                        },
                                                        "4": {
                                                            "text": "Return to main menu"
                                                        }
                                                    }
                                                }
                                            },
                                            "2": {
                                                "text": "Return to main menu"
                                            }
                                        }
                                    }
                                },
                                "2": {
                                    "text": "Tell me about a time you felt like this",
                                    "response": "Oh, man, I’ve had those days. Like when I flunked a chem test AND got yelled at by JJ for late photos. I just swung around, ate some pizza, and reminded myself: tomorrow’s a new swing."
                                },
                                "3": {
                                    "text": "Just keep cheering me up!",
                                    "response": "You got it, pal! You’re tougher than a Rhino charge. How about a quick swing around the city in your mind? Picture us zipping past Times Square!"
                                },
                                "4": {
                                    "text": "Return to main menu"
                                }
                            }
                        }
                    },
                    "3": {
                        "text": "Return to main menu"
                    }
                }
            }
        }
    }
}

# Run the chatbot
print("Welcome to the Ultimate Chatbot Experience!")
run_conversation(chatbot, chatbot)