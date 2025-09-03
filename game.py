# SNOWMAN_MIN_WORD_LENGTH = 5
# SNOWMAN_MAX_WORD_LENGTH = 8
# SNOWMAN_MAX_WRONG_GUESSES = 7

# SNOWMAN_GRAPHIC = [
#     '*   *   *  ',
#     ' *   _ *   ',
#     '   _[_]_ * ',
#     '  * (")    ',
#     '  \\( : )/ *',
#     '* (_ : _)  ',
#     '-----------'
# ]
# def print_snowman_graphic(wrong_guesses_count):
#     """This function prints out the appropriate snowman image 
#     depending on the number of wrong guesses the player has made.
#     """
    
#     for i in range(SNOWMAN_MAX_WRONG_GUESSES - wrong_guesses_count, SNOWMAN_MAX_WRONG_GUESSES):
#         print(SNOWMAN_GRAPHIC[i])


# def get_letter_from_user(correct_letter_guess_statuses, wrong_guesses_list):
#     """This function takes the snowman_word_dict and the list of characters 
#     that have been guessed incorrectly (wrong_guesses_list) as input.
#     It asks for input from the user of a single character until 
#     a valid character is provided and then returns this character.
#     """

#     valid_input = False
#     user_input_string = None

#     while not valid_input:
#         user_input_string = input("Guess a letter: ")
#         if not user_input_string.isalpha():
#             print("You must input a letter!")
#         elif len(user_input_string) > 1:
#             print("You can only input one letter at a time!")
#         elif (user_input_string in correct_letter_guess_statuses       
#                 and correct_letter_guess_statuses[user_input_string]): 
#             print("You already guessed that letter and it's in the word!")
#         elif user_input_string in wrong_guesses_list:
#             print("You already guessed that letter and it's not in the word!")
#         else:
#             valid_input = True

#     return user_input_string
    

# def build_letter_status_dict(snowman_word):
#     """This function takes snowman_word as input and returns 
#     a dictionary with a key-value pair for each letter in 
#     snowman_word where the key is the letter and the value is `False`.
#     """

#     letter_status_dict = {}
#     for letter in snowman_word:
#         letter_status_dict[letter] = False
#     return  letter_status_dict
    

# def print_word_progress_string(snowman_word, correct_letter_guess_statuses):
#     """
#     This function takes the snowman_word and snowman_word_dict as input.
#     It calls another function to generate a string representation of the  
#     user's progress towards guessing snowman_word and prints this string.
#     """

#     progress_string = generate_word_progress_string(snowman_word, correct_letter_guess_statuses)
#     print(progress_string)


# def generate_word_progress_string(snowman_word, correct_letter_guess_statuses):
#     """
#     This function takes the snowman_word and snowman_word_dict as input.
#     It creates and returns an output string that shows the correct letter 
#     guess placements as well as the placements for the letters yet to be 
#     guessed.
#     """

#     output_string = ""
#     is_not_first_letter = False

#     for letter in snowman_word:
#         if is_not_first_letter:
#             output_string += " "

#         if correct_letter_guess_statuses[letter]:
#             output_string += letter
#         else:
#             output_string += "_"

#         is_not_first_letter = True

#     return output_string


# def is_word_guessed(snowman_word, correct_letter_guess_statuses):
#     """
#     This function takes the snowman_word and snowman_word_dict as input.
#     It returns True if all the letters of the word have been guessed, and False otherwise.
#     """

#     for letter in snowman_word:
#         if not correct_letter_guess_statuses[letter]:
#             return False
#     return True

# def snowman(snowman_word):
#     wrong_guesses_list =[]
#     correct_letter_guess_statuses = build_letter_status_dict(snowman_word)
#     wrong_guesses_count = 0 
#     while wrong_guesses_count < SNOWMAN_MAX_WRONG_GUESSES and not is_word_guessed(snowman_word, correct_letter_guess_statuses):
#         print_word_progress_string(snowman_word, correct_letter_guess_statuses)
#         user_input = get_letter_from_user(correct_letter_guess_statuses, wrong_guesses_list)
#         if user_input in snowman_word:
#             correct_letter_guess_statuses[user_input] = True
#             print("You guessed the letter!")
#         else:  
#             wrong_guesses_list.append(user_input)  
#             wrong_guesses_count = len(wrong_guesses_list)
#             print("This letter is not in the snowman word.")
#             print_snowman_graphic(wrong_guesses_count)
#         if is_word_guessed(snowman_word, correct_letter_guess_statuses):
#             print('Congratulations, you win!')
#             break 
#     else:     
#         print(f"'Sorry, you lose! The word was {snowman_word}'")       
# snowman("apple") 

import random

SNOWMAN_MIN_WORD_LENGTH = 5
SNOWMAN_MAX_WORD_LENGTH = 8
SNOWMAN_MAX_WRONG_GUESSES = 7

SNOWMAN_GRAPHIC = [
    '*   *   *  ',
    ' *   _ *   ',
    '   _[_]_ * ',
    '  * (")    ',
    '  \\( : )/ *',
    '* (_ : _)  ',
    '-----------'
]
def print_snowman_graphic(wrong_guesses_count):
    """This function prints out the appropriate snowman image 
    depending on the number of wrong guesses the player has made.
    """
    
    for i in range(SNOWMAN_MAX_WRONG_GUESSES - wrong_guesses_count, SNOWMAN_MAX_WRONG_GUESSES):
        print(SNOWMAN_GRAPHIC[i])


def get_letter_from_user(correct_letter_guess_statuses, wrong_guesses_list):
    """This function takes the snowman_word_dict and the list of characters 
    that have been guessed incorrectly (wrong_guesses_list) as input.
    It asks for input from the user of a single character until 
    a valid character is provided and then returns this character.
    """

    valid_input = False
    user_input_string = None

    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        elif (user_input_string in correct_letter_guess_statuses       
                and correct_letter_guess_statuses[user_input_string]): 
            print("You already guessed that letter and it's in the word!")
        elif user_input_string in wrong_guesses_list:
            print("You already guessed that letter and it's not in the word!")
        else:
            valid_input = True

    return user_input_string
#TO DO    
def get_letter_automatically(correct_letter_guess_statuses, wrong_guesses_list): 
  computer_input_string = None
  valid_input = False
  letters = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z"
]
  
  while not valid_input:
      random_index = random.randint(0, 25)
      computer_input_string = letters[random_index]
      if (computer_input_string in correct_letter_guess_statuses       
                and correct_letter_guess_statuses[computer_input_string]): 
          continue
      elif computer_input_string in wrong_guesses_list:
          continue
      else:
          valid_input = True

  return computer_input_string
  

    

def build_letter_status_dict(snowman_word):
    """This function takes snowman_word as input and returns 
    a dictionary with a key-value pair for each letter in 
    snowman_word where the key is the letter and the value is `False`.
    """

    letter_status_dict = {}
    for letter in snowman_word:
        letter_status_dict[letter] = False
    return  letter_status_dict
    

def print_word_progress_string(snowman_word, correct_letter_guess_statuses):
    """
    This function takes the snowman_word and snowman_word_dict as input.
    It calls another function to generate a string representation of the  
    user's progress towards guessing snowman_word and prints this string.
    """

    progress_string = generate_word_progress_string(snowman_word, correct_letter_guess_statuses)
    print(progress_string)


def generate_word_progress_string(snowman_word, correct_letter_guess_statuses):
    """
    This function takes the snowman_word and snowman_word_dict as input.
    It creates and returns an output string that shows the correct letter 
    guess placements as well as the placements for the letters yet to be 
    guessed.
    """

    output_string = ""
    is_not_first_letter = False

    for letter in snowman_word:
        if is_not_first_letter:
            output_string += " "

        if correct_letter_guess_statuses[letter]:
            output_string += letter
        else:
            output_string += "_"

        is_not_first_letter = True

    return output_string


def is_word_guessed(snowman_word, correct_letter_guess_statuses):
    """
    This function takes the snowman_word and snowman_word_dict as input.
    It returns True if all the letters of the word have been guessed, and False otherwise.
    """

    for letter in snowman_word:
        if not correct_letter_guess_statuses[letter]:
            return False
    return True

def game_mode():
  valid_input = False
  user_mode_choice = None
  while not valid_input:
      user_mode_choice = input("Enter 't' to test or 'p' to play: ")
      if not user_mode_choice.isalpha():
          print("You must input a letter!")
      elif len(user_mode_choice) > 1:
          print("You can only input one letter: 'p' or 't'.")
      else:
        valid_input = True
  return user_mode_choice          



def snowman(snowman_word):
    user_mode_choice = game_mode()
    wrong_guesses_list =[]
    correct_letter_guess_statuses = build_letter_status_dict(snowman_word)
    wrong_guesses_count = 0 
    while wrong_guesses_count < SNOWMAN_MAX_WRONG_GUESSES and not is_word_guessed(snowman_word, correct_letter_guess_statuses):
        print_word_progress_string(snowman_word, correct_letter_guess_statuses)
        if user_mode_choice == "p":
            user_input = get_letter_from_user(correct_letter_guess_statuses, wrong_guesses_list)
        elif user_mode_choice == "t":
          # TO DO 
            user_input = get_letter_automatically(correct_letter_guess_statuses, wrong_guesses_list)     
        if user_input in snowman_word:
            correct_letter_guess_statuses[user_input] = True
            print("You guessed the letter!")
        else:  
            wrong_guesses_list.append(user_input)  
            wrong_guesses_count = len(wrong_guesses_list)
            print("This letter is not in the snowman word.")
            print_snowman_graphic(wrong_guesses_count)
        if is_word_guessed(snowman_word, correct_letter_guess_statuses):
            print('Congratulations, you win!')
            break 
    else:     
        print(f"'Sorry, you lose! The word was {snowman_word}'")       
snowman("apple") 