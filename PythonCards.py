import os
import random



def error_char_handler(error):
    unhandled_text = "[Character not readable]"
    return(unhandled_text, error.end)

flash_path = os.path.dirname(__file__)
flashcard = os.path.join(flash_path, "Pyflash.txt")

if not os.path.exists(flashcard):
    with open(flashcard, 'w', encoding='utf-8', errors='unhandled_text') as new_file:
        new_file.write("Python Flash Card Game \n")

    print("Flashcard file created. \n")

    with open(flashcard, 'w', encoding='utf-8', errors='unhandled_text') as qa_pop:
        for qa in range(100):
            qa_pop.write("Q: \n")
            qa_pop.write("A: \n")
            qa_pop.write("\n")
    print("QA populated in Pycard.txt \n")
    print("Refresh your folder, open pyflash.txt, add your questions and answers \n")
    exit()

else:
    with open (flashcard, 'r', encoding='utf-8', errors='unhandled_text') as flash:
        frontFace = [line.strip() for line in flash.readlines() if line.strip()]

cleaned_qs = []

for question in frontFace:
    if question.startswith("Q:") or question.startswith("A:"):
        remv_qa = question.split(":", 1)[1].strip()
        if remv_qa == "":
            continue

        cleaned_qs.append(remv_qa)
        continue
    
    print(f"Ignored unrecognized entry: {question}")

if len(cleaned_qs) % 2 != 0:
    print("Found question without matching answer. Skipping entry.")
    print("-->", cleaned_qs[-1])
    cleaned_qs = cleaned_qs[:-1]

if len(cleaned_qs) < 2:
    print("\nNo questions found in PyFlash.txt")
    print("\nPlease check same location as pythonCards.py and refresh folder if PyFlash.txt isn't visible.")
    print("\nEnsure entries look like:\n")
    print("Q: (Your question)\n")
    print("A: (Your correct answer)\n")
    print("Save the file and run again.")
    exit()

qa_pairs = []

for qa in range(0, len(cleaned_qs), 2):
    asked_qs = cleaned_qs[qa]
    strd_ans = cleaned_qs[qa + 1]
    qa_pairs.append([asked_qs, strd_ans])

while True:
    random.shuffle(qa_pairs)

    for showq in qa_pairs:
        show_the_q = showq[0]
        print(show_the_q)
        ask_ans = input("Answer: ")
        correct_ans = showq[1]
        print("Correct answer: ", correct_ans)

    run_it = input("Play again? Y/N: ")

    if run_it.lower() == "y":
        continue
    else:
        break