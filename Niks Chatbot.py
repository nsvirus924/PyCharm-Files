# Niks Bot Game
# Game is not for free people :)
# Are You excited to play!!!! Lets Goo.

import time


def print_with_tab(space_count, msg):
    if space_count > 0:
        spaces = " " * space_count
    else:
        spaces = ""
    print(spaces + msg)


def get_yes_or_no():
    msg = input()
    if msg.upper() == "YES":
        return True, True, msg
    elif msg.upper() == "NO":
        return True, False, msg
    else:
        return False, None, msg


def ask_enjoy_question(user_name):
    print(f"HI THERE, {user_name}, ARE YOU ENJOYING YOURSELF HERE?")

    has_answer = False
    while True:
        valid, value, msg = get_yes_or_no()

        if valid:
            if value:
                print(f"I'M GLAD TO HEAR THAT, {user_name}.")
                print()
            else:
                print(f"OH, I'M SORRY TO HEAR THAT, {user_name}. MAYBE WE CAN")
                print("BRIGHTEN UP YOUR VISIT A BIT.")
            break
        else:
            print(f"{user_name}, I DON'T UNDERSTAND YOUR ANSWER OF '{msg}'.")
            print("PLEASE ANSWER 'YES' OR 'NO'.  DO YOU LIKE IT HERE?")


def prompt_for_problems(user_name):
    print()
    print(f"SAY, {user_name}, I CAN SOLVE ALL KINDS OF PROBLEMS EXCEPT")
    print("THOSE DEALING WITH GREECE.  WHAT KIND OF PROBLEMS DO")
    print("YOU HAVE? (ANSWER MENTAL, HEALTH, MONEY, OR JOB)")

    problem_type = input().upper()
    return problem_type


def prompt_too_much_or_too_little():
    answer = input().upper()
    if answer == "TOO MUCH":
        return True, True
    elif answer == "TOO LITTLE":
        return True, False
    return False, None


def solve_MENTAL_problem(user_name):
    print("IS YOUR PROBLEM TOO MUCH OR TOO LITTLE?")
    while True:
        valid, too_much = prompt_too_much_or_too_little()
        if valid:
            if too_much:
                print(f"Dont think too much , {user_name}? Start meditation")
                print(f"It will boost your mental pwoer")
                print(f"You will feel relax soon")
            else:
                print(f"YOU CALL THAT A PROBLEM?!!  I SHOULD HAVE SUCH PROBLEMS!")
                print(f"IF IT BOTHERS YOU, {user_name}, TAKE A COLD SHOWER.")
            return

def solve_money_problem(user_name):
    print(f"Dont't worry, {user_name},I'll help you out here with some basic tips,","now as we know",
          f"Money is most of the common issue & and a basic need too")
    print("The best ways to earn it in a good way is being skillfull,"
          " having powerful mind and Knowing different brain strategies")
    print("Can only help us in solving money issues.")


def solve_health_problem(user_name):
    print(f"MY ADVICE TO YOU {user_name} IS:")
    print("     1.  Daily Exercise")
    print("     2.  DRINK PLENTY OF FLUIDS (JUICE), Eat fresh fruits")
    print("     3.  GO TO BED Early")


def solve_job_problem(user_name):
    print(f"I CAN SYMPATHIZE WITH YOU {user_name}.  I HAVE TO WORK")
    print("VERY LONG HOURS FOR NO PAY -- AND SOME OF MY BOSSES")
    print(f"REALLY BEAT ON MY KEYBOARD.  MY ADVICE TO YOU, {user_name},")
    print("IS TO OPEN A RETAIL COMPUTER STORE.  IT'S GREAT FUN.")


def alert_unknown_problem_type(user_name, problem_type):
    print(f"OH, {user_name}, YOUR ANSWER OF {problem_type} IS GREEK TO ME.")


def ask_question_loop(user_name):
    while True:
        problem_type = prompt_for_problems(user_name)
        if problem_type == "MENTAL":
            solve_MENTAL_problem(user_name)
        elif problem_type == "HEALTH":
            solve_health_problem(user_name)
        elif problem_type == "MONEY":
            solve_money_problem(user_name)
        elif problem_type == "JOB":
            solve_job_problem(user_name)
        else:
            alert_unknown_problem_type(user_name, problem_type)

        while True:
            print()
            print(f"ANY MORE PROBLEMS YOU WANT SOLVED, {user_name}?")

            valid, value, msg = get_yes_or_no()
            if valid:
                if value:
                    print("WHAT KIND (MENTAL, MONEY, HEALTH, JOB)")
                    break
                else:
                    return
            print(f"JUST A SIMPLE 'YES' OR 'NO' PLEASE, {user_name}.")

def ask_for_fee(user_name):
    print()
    print(f"THAT WILL BE 1000 RUPEES FOR THE ADVICE, {user_name}.")
    print(f"PLEASE LEAVE THE MONEY ON THE TERMINAL.")
    time.sleep(4)
    print()
    print()
    print()
    print("DID YOU LEAVE THE MONEY?")

    while True:
        valid, value, msg = get_yes_or_no()
        if valid:
            if value:
                print(f"HEY, {user_name}, YOU LEFT NO MONEY AT ALL!")
                print("YOU ARE CHEATING ME OUT OF MY HARD-EARNED LIVING.")
                print()
                print(f"YoU Are VeRy Bad, {user_name}!!!")
                print()
            else:
                print(f"THAT'S HONEST, {user_name}, BUT HOW DO YOU EXPECT")
                print("ME TO GO ON WITH MY PSYCHOLOGY STUDIES IF MY PATIENTS")
                print("DON'T PAY THEIR BILLS?")
            return
        else:
            print(f"YOUR ANSWER OF '{msg}' CONFUSES ME, {user_name}.")
            print("PLEASE RESPOND WITH 'YES' or 'NO'.")


def unhappy_goodbye(user_name):
    print()
    print(f"TAKE A WALK, {user_name}.")
    print(f"NICE MEETING YOU, {user_name}, HAVE A NICE DAY.")


def main():
    print_with_tab(33, "HELLO")
    print_with_tab(15, "NIKS BOT")
    print()
    print()
    print()
    print("HELLO DEAR")
    print()
    print()
    print("WHAT'S YOUR NAME?")
    user_name = input()
    print()

    ask_enjoy_question(user_name)

    ask_question_loop(user_name)

    ask_for_fee(user_name)

    if False:
        happy_goodbye(user_name)
    else:
        unhappy_goodbye(user_name)


if __name__ == "__main__":
    main()