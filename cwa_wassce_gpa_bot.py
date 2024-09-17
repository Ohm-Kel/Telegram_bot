import telebot
import time
from telebot import types

# Bot token
API_TOKEN = '7386952987:AAGzS2x36prNB1A0xk1SsXED4bHfgzq8Go4'
bot = telebot.TeleBot(API_TOKEN)

# Dictionary to keep track of user's current state
user_state = {}
course_details = {}
wassce_results = {}

# Programs and courses dictionary (placeholder - add actual data)
programs = {
    'Computer Engineering': {
        'LEVEL 100': {
            'First': ["Algebra", "Applied Electricity", "Technical Drawing", "Communication Skills",
                      "Engineering Technology", "Environmental Studies", "Basic Mechanics"],
            'Second': ["Calculus with Analysis", "Basic Electronics", "Electrical Engineering Drawing",
                       "Communication Skills II", "Electrical Machines", "Introduction to IT"],
        },
        'LEVEL 200': {
            'First': ["Calculus with Analysis", "Basic Electronics", "Electrical Engineering Drawing",
                      "Communication Skills II", "Electrical Machines", "Introduction to IT"],
            'Second': ['Course CE401', 'Course CE402']
        },
        'LEVEL 300': {
            'First': ['Course CE501', 'Course CE502'],
            'Second': ['Course CE601', 'Course CE602']
        },
        'LEVEL 400': {
            'First': ['Course CE701', 'Course CE702'],
            'Second': ['Course CE801', 'Course CE802']
        }
    },
    'Electrical Engineering': {
        'LEVEL 100': {
            'First': ["Algebra", "Applied Electricity", "Technical Drawing", "Communication Skills",
                      "Engineering Technology", "Environmental Studies", "Basic Mechanics"],
            'Second': ["Calculus with Analysis", "Basic Electronics", "Electrical Engineering Drawing",
                       "Communication Skills II", "Electrical Transformers", "Introduction to IT",
                       "Python Programming"],
        },
        'LEVEL 200': {
            'First': ['Course EE301', 'Course EE302'],
            'Second': ['Course EE401', 'Course EE402']
        },
        'LEVEL 300': {
            'First': ['Course EE501', 'Course EE502'],
            'Second': ['Course EE601', 'Course EE602']
        },
        'LEVEL 400': {
            'First': ['Course EE701', 'Course EE702'],
            'Second': ['Course EE801', 'Course EE802']
        }
    },
    'Aerospace Engineering': {
        'LEVEL 100': {
            'First': ["Algebra", "Applied Electricity", "Technical Drawing", "Communication Skills",
                      "Engineering Technology", "Environmental Studies", "Basic Mechanics"],
            'Second': ["Calculus with Analysis", "Basic Electronics", "Electrical Engineering Drawing",
                       "Communication Skills II", "Electrical Transformers", "Introduction to IT",
                       "Python Programming"],
        },
        'LEVEL 200': {
            'First': ['Course AE301', 'Course AE302'],
            'Second': ['Course AE401', 'Course AE402']
        },
        'LEVEL 300': {
            'First': ['Course AE501', 'Course AE502'],
            'Second': ['Course AE601', 'Course AE602']
        },
        'LEVEL 400': {
            'First': ['Course AE701', 'Course AE702'],
            'Second': ['Course AE801', 'Course AE802']
        }
    },
    'Materials Engineering': {
        'LEVEL 100': {
            'First': ["Algebra", "Applied Electricity", "Technical Drawing", "Communication Skills",
                      "Engineering Technology", "Environmental Studies", "Basic Mechanics"],
            'Second': ["Calculus with Analysis", "Basic Electronics", "Electrical Engineering Drawing",
                       "Communication Skills II", "Electrical Transformers", "Introduction to IT",
                       "Python Programming"],
        },
        'LEVEL 200': {
            'First': ['Course ME301', 'Course ME302'],
            'Second': ['Course ME401', 'Course ME402']
        },
        'LEVEL 300': {
            'First': ['Course ME501', 'Course ME502'],
            'Second': ['Course ME601', 'Course ME602']
        },
        'LEVEL 400': {
            'First': ['Course ME701', 'Course ME702'],
            'Second': ['Course ME801', 'Course ME802']
        }
    },
    'Industrial Engineering': {
        'LEVEL 100': {
            'First': ["Algebra", "Applied Electricity", "Technical Drawing", "Communication Skills",
                      "Engineering Technology", "Environmental Studies", "Basic Mechanics"],
            'Second': ["Calculus with Analysis", "Basic Electronics", "Electrical Engineering Drawing",
                       "Communication Skills II", "Electrical Transformers", "Introduction to IT",
                       "Python Programming"],
        },
        'LEVEL 200': {
            'First': ['Course IE301', 'Course IE302'],
            'Second': ['Course IE401', 'Course IE402']
        },
        'LEVEL 300': {
            'First': ['Course IE501', 'Course IE502'],
            'Second': ['Course IE601', 'Course IE602']
        },
        'LEVEL 400': {
            'First': ['Course IE701', 'Course IE702'],
            'Second': ['Course IE801', 'Course IE802']
        }
    },
    'Civil Engineering': {
        'LEVEL 100': {
            'First': ["Algebra", "Applied Electricity", "Technical Drawing", "Communication Skills",
                      "Engineering Technology", "Environmental Studies", "Basic Mechanics"],
            'Second': ["Calculus with Analysis", "Basic Electronics", "Electrical Engineering Drawing",
                       "Communication Skills II", "Electrical Transformers", "Introduction to IT",
                       "Python Programming"],
        },
        'LEVEL 200': {
            'First': ['Course CE301', 'Course CE302'],
            'Second': ['Course CE401', 'Course CE402']
        },
        'LEVEL 300': {
            'First': ['Course CE501', 'Course CE502'],
            'Second': ['Course CE601', 'Course CE602']
        },
        'LEVEL 400': {
            'First': ['Course CE701', 'Course CE702'],
            'Second': ['Course CE801', 'Course CE802']
        }
    },
    'Mechanical Engineering': {
        'LEVEL 100': {
            'First': ["Algebra", "Applied Electricity", "Technical Drawing", "Communication Skills",
                      "Engineering Technology", "Environmental Studies", "Basic Mechanics"],
            'Second': ["Calculus with Analysis", "Basic Electronics", "Electrical Engineering Drawing",
                       "Communication Skills II", "Electrical Transformers", "Introduction to IT",
                       "Python Programming"],
        },
        'LEVEL 200': {
            'First': ['Course ME301', 'Course ME302'],
            'Second': ['Course ME401', 'Course ME402']
        },
        'LEVEL 300': {
            'First': ['Course ME501', 'Course ME502'],
            'Second': ['Course ME601', 'Course ME602']
        },
        'LEVEL 400': {
            'First': ['Course ME701', 'Course ME702'],
            'Second': ['Course ME801', 'Course ME802']
        }
    },
    'Petroleum Engineering': {
        'LEVEL 100': {
            'First': ["Algebra", "Applied Electricity", "Technical Drawing", "Communication Skills",
                      "Engineering Technology", "Environmental Studies", "Basic Mechanics"],
            'Second': ["Calculus with Analysis", "Basic Electronics", "Electrical Engineering Drawing",
                       "Communication Skills II", "Electrical Transformers", "Introduction to IT",
                       "Python Programming"],
        },
        'LEVEL 200': {
            'First': ['Course PE301', 'Course PE302'],
            'Second': ['Course PE401', 'Course PE402']
        },
        'LEVEL 300': {
            'First': ['Course PE501', 'Course PE502'],
            'Second': ['Course PE601', 'Course PE602']
        },
        'LEVEL 400': {
            'First': ['Course PE701', 'Course PE702'],
            'Second': ['Course PE801', 'Course PE802']
        }
    },
    'Petrochemical Engineering': {
        'LEVEL 100': {
            'First': ["Algebra", "Applied Electricity", "Technical Drawing", "Communication Skills",
                      "Engineering Technology", "Environmental Studies", "Basic Mechanics"],
            'Second': ["Calculus with Analysis", "Basic Electronics", "Electrical Engineering Drawing",
                       "Communication Skills II", "Electrical Transformers", "Introduction to IT",
                       "Python Programming"],
        },
        'LEVEL 200': {
            'First': ['Course PCE301', 'Course PCE302'],
            'Second': ['Course PCE401', 'Course PCE402']
        },
        'LEVEL 300': {
            'First': ['Course PCE501', 'Course PCE502'],
            'Second': ['Course PCE601', 'Course PCE602']
        },
        'LEVEL 400': {
            'First': ['Course PCE701', 'Course PCE702'],
            'Second': ['Course PCE801', 'Course PCE802']
        }
    },
    'Biomedical Engineering': {
        'LEVEL 100': {
            'First': ["Algebra", "Applied Electricity", "Technical Drawing", "Communication Skills",
                      "Engineering Technology", "Environmental Studies", "Basic Mechanics"],
            'Second': ["Calculus with Analysis", "Basic Electronics", "Electrical Engineering Drawing",
                       "Communication Skills II", "Electrical Transformers", "Introduction to IT",
                       "Python Programming"],
        },
        'LEVEL 200': {
            'First': ['Course BE301', 'Course BE302'],
            'Second': ['Course BE401', 'Course BE402']
        },
        'LEVEL 300': {
            'First': ['Course BE501', 'Course BE502'],
            'Second': ['Course BE601', 'Course BE602']
        },
        'LEVEL 400': {
            'First': ['Course BE701', 'Course BE702'],
            'Second': ['Course BE801', 'Course BE802']
        }
    },
    'Telecommunication Engineering': {
        'LEVEL 100': {
            'First': ["Algebra", "Applied Electricity", "Technical Drawing", "Communication Skills",
                      "Engineering Technology", "Environmental Studies", "Basic Mechanics"],
            'Second': ["Calculus with Analysis", "Basic Electronics", "Electrical Engineering Drawing",
                       "Communication Skills II", "Electrical Transformers", "Introduction to IT",
                       "Python Programming"],
        },
        'LEVEL 200': {
            'First': ['Course BE301', 'Course BE302'],
            'Second': ['Course BE401', 'Course BE402']
        },
        'LEVEL 300': {
            'First': ['Course BE501', 'Course BE502'],
            'Second': ['Course BE601', 'Course BE602']
        },
        'LEVEL 400': {
            'First': ['Course BE701', 'Course BE702'],
            'Second': ['Course BE801', 'Course BE802']
        }
    },
    'Geographical Engineering': {
        'LEVEL 100': {
            'First': ["Algebra", "Applied Electricity", "Technical Drawing", "Communication Skills",
                      "Engineering Technology", "Environmental Studies", "Basic Mechanics"],
            'Second': ["Calculus with Analysis", "Basic Electronics", "Electrical Engineering Drawing",
                       "Communication Skills II", "Electrical Transformers", "Introduction to IT",
                       "Python Programming"],
        },
        'LEVEL 200': {
            'First': ['Course BE301', 'Course BE302'],
            'Second': ['Course BE401', 'Course BE402']
        },
        'LEVEL 300': {
            'First': ['Course BE501', 'Course BE502'],
            'Second': ['Course BE601', 'Course BE602']
        },
        'LEVEL 400': {
            'First': ['Course BE701', 'Course BE702'],
            'Second': ['Course BE801', 'Course BE802']
        }
    },
    'Geomatic Engineering': {
        'LEVEL 100': {
            'First': ["Algebra", "Applied Electricity", "Technical Drawing", "Communication Skills",
                      "Engineering Technology", "Environmental Studies", "Basic Mechanics"],
            'Second': ["Calculus with Analysis", "Basic Electronics", "Electrical Engineering Drawing",
                       "Communication Skills II", "Electrical Transformers", "Introduction to IT",
                       "Python Programming"],
        },
        'LEVEL 200': {
            'First': ['Course BE301', 'Course BE302'],
            'Second': ['Course BE401', 'Course BE402']
        },
        'LEVEL 300': {
            'First': ['Course BE501', 'Course BE502'],
            'Second': ['Course BE601', 'Course BE602']
        },
        'LEVEL 400': {
            'First': ['Course BE701', 'Course BE702'],
            'Second': ['Course BE801', 'Course BE802']
        }
    },
    'Metallurgical Engineering': {
        'LEVEL 100': {
            'First': ["Algebra", "Applied Electricity", "Technical Drawing", "Communication Skills",
                      "Engineering Technology", "Environmental Studies", "Basic Mechanics"],
            'Second': ["Calculus with Analysis", "Basic Electronics", "Electrical Engineering Drawing",
                       "Communication Skills II", "Electrical Transformers", "Introduction to IT",
                       "Python Programming"],
        },
        'LEVEL 200': {
            'First': ['Course BE301', 'Course BE302'],
            'Second': ['Course BE401', 'Course BE402']
        },
        'LEVEL 300': {
            'First': ['Course BE501', 'Course BE502'],
            'Second': ['Course BE601', 'Course BE602']
        },
        'LEVEL 400': {
            'First': ['Course BE701', 'Course BE702'],
            'Second': ['Course BE801', 'Course BE802']
        }
    },
    'Marine Engineering': {
        'LEVEL 100': {
            'First': ["Algebra", "Applied Electricity", "Technical Drawing", "Communication Skills",
                      "Engineering Technology", "Environmental Studies", "Basic Mechanics"],
            'Second': ["Calculus with Analysis", "Basic Electronics", "Electrical Engineering Drawing",
                       "Communication Skills II", "Electrical Transformers", "Introduction to IT",
                       "Python Programming"],
        },
        'LEVEL 200': {
            'First': ['Course BE301', 'Course BE302'],
            'Second': ['Course BE401', 'Course BE402']
        },
        'LEVEL 300': {
            'First': ['Course BE501', 'Course BE502'],
            'Second': ['Course BE601', 'Course BE602']
        },
        'LEVEL 400': {
            'First': ['Course BE701', 'Course BE702'],
            'Second': ['Course BE801', 'Course BE802']
        }
    },
    'Chemical Engineering': {
        'LEVEL 100': {
            'First': ["Algebra", "Applied Electricity", "Technical Drawing", "Communication Skills",
                      "Engineering Technology", "Environmental Studies", "Basic Mechanics"],
            'Second': ["Calculus with Analysis", "Basic Electronics", "Electrical Engineering Drawing",
                       "Communication Skills II", "Electrical Transformers", "Introduction to IT",
                       "Python Programming"],
        },
        'LEVEL 200': {
            'First': ['Course BE301', 'Course BE302'],
            'Second': ['Course BE401', 'Course BE402']
        },
        'LEVEL 300': {
            'First': ['Course BE501', 'Course BE502'],
            'Second': ['Course BE601', 'Course BE602']
        },
        'LEVEL 400': {
            'First': ['Course BE701', 'Course BE702'],
            'Second': ['Course BE801', 'Course BE802']
        }
    },
    'Agricultural Engineering': {
        'LEVEL 100': {
            'First': ["Algebra", "Applied Electricity", "Technical Drawing", "Communication Skills",
                      "Engineering Technology", "Environmental Studies", "Basic Mechanics"],
            'Second': ["Calculus with Analysis", "Basic Electronics", "Electrical Engineering Drawing",
                       "Communication Skills II", "Electrical Transformers", "Introduction to IT",
                       "Python Programming"],
        },
        'LEVEL 200': {
            'First': ['Course BE301', 'Course BE302'],
            'Second': ['Course BE401', 'Course BE402']
        },
        'LEVEL 300': {
            'First': ['Course BE501', 'Course BE502'],
            'Second': ['Course BE601', 'Course BE602']
        },
        'LEVEL 400': {
            'First': ['Course BE701', 'Course BE702'],
            'Second': ['Course BE801', 'Course BE802']
        }
    },
}


# Maximum number of subjects allowed
MAX_SUBJECTS = 8

# Dictionary for WASSCE grade to GPA conversion
wassce_to_gpa = {
    'A1': 4.0,
    'B2': 3.5,
    'B3': 3.0,
    'C4': 2.5,
    'C5': 2.0,
    'C6': 1.5,
    'D7': 1.0,
    'E8': 0.5,
    'F9': 0.0
}

# Placeholder for user state and course details (for CWA calculation)
user_state = {}
course_details = {}
wassce_results = {}


# Handle the /start and /hello commands
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    user_first_name = message.from_user.first_name
    welcome_message = f"Hi, {user_first_name}! Welcome to our platform as the CEO, Kelvin🤠. It's a pleasure to have you here!\n" \
                      "What would you like to do today?"

    # Send the welcome message
    bot.send_message(message.chat.id, welcome_message)

    # Introduce a delay before showing the program options
    time.sleep(2)  # delay for 2 seconds

    # Create the inline keyboard for options: CWA or WASSCE GPA
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton('Calculate CWA', callback_data='CWA'),
        types.InlineKeyboardButton('Convert WASSCE to GPA', callback_data='WASSCE')
    )

    # Send the message with options
    bot.send_message(message.chat.id, "Please choose an option:", reply_markup=markup)


# Function to send program selection options (for CWA)
def send_program_selection(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    for program in programs.keys():
        markup.add(types.InlineKeyboardButton(program, callback_data=program))
    bot.send_message(message.chat.id, "Please choose your program.", reply_markup=markup)


# Handle callback queries
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    user_id = call.from_user.id
    data = call.data

    # Handle choice between CWA and WASSCE GPA
    if data == 'CWA':
        user_state[user_id] = {'action': 'CWA'}
        bot.answer_callback_query(call.id, "You selected CWA calculation!")
        send_program_selection(call.message)
    elif data == 'WASSCE':
        user_state[user_id] = {'action': 'WASSCE'}
        bot.answer_callback_query(call.id, "You selected WASSCE GPA conversion!")
        start_wassce_conversion(call.message, user_id)

    # Handle program selection for CWA
    elif data in programs:
        user_state[user_id]['program'] = data
        bot.answer_callback_query(call.id, f"You selected {data}!")
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton('LEVEL 100', callback_data='LEVEL 100'),
            types.InlineKeyboardButton('LEVEL 200', callback_data='LEVEL 200'),
            types.InlineKeyboardButton('LEVEL 300', callback_data='LEVEL 300'),
            types.InlineKeyboardButton('LEVEL 400', callback_data='LEVEL 400')
        )
        bot.send_message(call.message.chat.id, "Please select your academic level.", reply_markup=markup)

    # Handle level selection
    elif data in ['LEVEL 100', 'LEVEL 200', 'LEVEL 300', 'LEVEL 400']:
        if 'program' in user_state[user_id]:
            program = user_state[user_id]['program']
            user_state[user_id]['level'] = data
            bot.answer_callback_query(call.id, f"You selected {data}!")
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(
                types.InlineKeyboardButton('First Semester', callback_data='First'),
                types.InlineKeyboardButton('Second Semester', callback_data='Second')
            )
            bot.send_message(call.message.chat.id, "Please select your semester.", reply_markup=markup)

    # Handle semester selection
    elif data in ['First', 'Second']:
        if 'program' in user_state[user_id] and 'level' in user_state[user_id]:
            program = user_state[user_id]['program']
            level = user_state[user_id]['level']
            user_state[user_id]['semester'] = data
            bot.answer_callback_query(call.id, f"You selected {data} Semester!")
            course_details[user_id] = {'program': program, 'level': level, 'semester': data, 'courses': {}}
            ask_for_course_details(call.message, user_id)
        else:
            bot.send_message(call.message.chat.id, "Please select your program and level first.")


# Function to start the WASSCE to GPA conversion process
def start_wassce_conversion(message, user_id):
    # Initialize user's WASSCE result state
    wassce_results[user_id] = {'grades': {}, 'subjects': [], 'current_subject': 0}
    bot.send_message(message.chat.id, f"Please enter the name of your first subject (maximum {MAX_SUBJECTS} subjects):")


# Function to ask for WASSCE grade for each subject after subject entry
def ask_for_wassce_grade(message, user_id):
    current_subject_index = wassce_results[user_id]['current_subject']

    # Ensure we don't exceed the maximum number of subjects
    if current_subject_index < MAX_SUBJECTS:
        current_subject = wassce_results[user_id]['subjects'][current_subject_index]
        bot.send_message(message.chat.id, f"Enter your grade for {current_subject} (A1, B2, B3, etc.):")
    else:
        calculate_gpa(message, user_id)


# Handle user input for WASSCE grades and subjects
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    text = message.text.upper()  # Convert to uppercase for easier comparison

    # Handle subject input
    if user_id in wassce_results and wassce_results[user_id]['current_subject'] < MAX_SUBJECTS:
        if len(wassce_results[user_id]['subjects']) <= wassce_results[user_id]['current_subject']:
            # Add the entered subject to the list
            wassce_results[user_id]['subjects'].append(text)
            bot.send_message(message.chat.id, f"Enter the grade for {text} (A1, B2, B3, etc.):")
        else:
            # Handle WASSCE grades input for the current subject
            current_subject = wassce_results[user_id]['subjects'][wassce_results[user_id]['current_subject']]

            if text in wassce_to_gpa:
                # Store the grade corresponding to the subject
                wassce_results[user_id]['grades'][current_subject] = wassce_to_gpa[text]
                wassce_results[user_id]['current_subject'] += 1

                if wassce_results[user_id]['current_subject'] < MAX_SUBJECTS:
                    bot.send_message(message.chat.id, f"Please enter the next subject name (or type 'done' to finish):")
                else:
                    # All subjects entered, calculate GPA
                    calculate_gpa(message, user_id)
            else:
                bot.send_message(message.chat.id, "Invalid grade. Please enter a valid grade (A1, B2, B3, etc.).")

    # Allow user to manually end the input before reaching the 8 subject limit
    elif text == "DONE":
        if wassce_results[user_id]['current_subject'] > 0:
            calculate_gpa(message, user_id)
        else:
            bot.send_message(message.chat.id, "Please enter at least one subject and grade.")

    else:
        bot.reply_to(message, "Please enter a subject name or a valid grade.")


# Function to calculate and display GPA
def calculate_gpa(message, user_id):
    if wassce_results[user_id]['grades']:
        total_gpa = sum(wassce_results[user_id]['grades'].values())
        gpa = total_gpa / len(wassce_results[user_id]['grades'])
        bot.send_message(message.chat.id, f"Your GPA based on your WASSCE results is: {gpa:.2f}")
    else:
        bot.send_message(message.chat.id, "No grades were entered.")

    # Clear user state after calculation
    del wassce_results[user_id]


# Function to ask for course details (score and credit hours) for CWA
def ask_for_course_details(message, user_id):
    program = user_state[user_id]['program']
    level = user_state[user_id]['level']
    semester = user_state[user_id]['semester']
    courses = programs[program][level][semester]

    current_course_index = len(course_details[user_id]['courses'])

    if current_course_index < len(courses):
        current_course = courses[current_course_index]
        course_details[user_id]['current_course'] = current_course
        bot.send_message(message.chat.id, f"Enter the exam score for {current_course} (between 0 and 100):")
    else:
        calculate_weighted_average(message, user_id)


# Function to calculate and display the weighted average (CWA)
def calculate_weighted_average(message, user_id):
    total_weighted_score = 0
    total_credit_hours = 0

    for course, details in course_details[user_id]['courses'].items():
        total_weighted_score += details['score'] * details['credit_hours']
        total_credit_hours += details['credit_hours']

    if total_credit_hours > 0:
        weighted_average = total_weighted_score / total_credit_hours
        bot.send_message(message.chat.id, f"The weighted average exam score is: {weighted_average:.2f}")
    else:
        bot.send_message(message.chat.id, "No valid credit hours provided.")

    # Clear user state after calculation
    del user_state[user_id]
    del course_details[user_id]


# Start polling
bot.infinity_polling()
