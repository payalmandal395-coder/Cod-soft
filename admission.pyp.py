import sys

def school_admission_chat():
    
    print("*** Welcome to XYZ International School ***")
    print("Receptionist: Hello! Welcome to our school. How can I help you today?")
    
    
    guardian_intent = input("Guardian: ").lower()
    
    if "admission" in guardian_intent or "enroll" in guardian_intent or "register" in guardian_intent:
        print("\nReceptionist: Great! We are currently accepting admissions. May I know what grade you are looking for?")
    else:
        print("\nReceptionist: I see. For other queries, please visit our main office down the hall. Have a great day!")
        return

    
    try:
        grade = int(input("Guardian (Enter grade as a number, e.g., 1, 5, 9): "))
    except ValueError:
        print("\nReceptionist: Please enter a valid grade number. Let's try again later.")
        return

    print("\nReceptionist: Got it. And how old is your child?")
    try:
        age = int(input("Guardian (Enter age in years): "))
    except ValueError:
        print("\nReceptionist: Invalid age input. Process cancelled.")
        return

    if grade == 1 and (age < 5 or age > 7):
        print(f"\nReceptionist: I'm sorry. For Grade 1, the child must be between 5 and 7 years old. Your child is {age}.")
        print("Receptionist: We cannot proceed with the admission due to age criteria.")
        return
    elif grade > 1 and (age < (grade + 4)):
        print(f"\nReceptionist: Your child seems a bit too young for Grade {grade}. We recommend a lower grade.")
        return
    else:
        print("\nReceptionist: Perfect! Your child meets the age eligibility criteria for this grade.")
    if grade == 10:
        print("\nReceptionist: Oh, let me check our portal... Ah, unfortunately, seats for Grade 10 are completely full this term.")
        print("Receptionist: Would you like to be placed on our waiting list? (yes/no)")
        waitlist = input("Guardian: ").lower()
        if waitlist == "yes":
            print("Receptionist: Wonderful. I have noted your details. We will contact you if a seat opens up!")
        else:
            print("Receptionist: Thank you for stopping by anyway! Have a great day.")
        return
    else:
        print("Receptionist: I've checked our system, and we have a few spots remaining in that grade!")


    print("\nReceptionist: To finalize the registration, do you have the required documents with you?")
    print("Required: Birth Certificate, Previous Report Card, and Proof of Address.")
    print("1. Yes, I have all of them.")
    print("2. No, I am missing some.")
    
    doc_choice = input("Guardian (Enter 1 or 2): ").strip()
    
    if doc_choice == "1":
        print("\nReceptionist: Excellent. Everything looks perfectly in order!")
        print("Receptionist: Please fill out this final admission form and submit the processing fee at the counter on your left.")
        print("Receptionist: Welcome to the XYZ family!")
    elif doc_choice == "2":
        print("\nReceptionist: That's completely fine. I can give you a provisional admission slip.")
        print("Receptionist: You will just need to bring the missing documents by this Friday to secure the seat.")
        print("Guardian: Thank you, I will do that.")
        print("Receptionist: You're very welcome! See you on Friday.")
    else:
        print("\nReceptionist: Sorry, that wasn't a valid option. Please see the principal's office for manual processing.")

school_admission_chat()