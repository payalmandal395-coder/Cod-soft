import sys

def get_bot_response(user_input):
    # Convert input to lowercase and remove extra spaces for consistent matching
    query = user_input.lower().strip()
    
    # 1. System Commands & Greetings
    if query in ["hi", "hello", "hey"]:
        return "Hello! I am ChatBot. Ask me about any engineering stream (e.g., CS, Mechanical, Civil) to learn more!"
        
    elif query in ["bye", "exit", "quit"]:
        print("ChatBot: Goodbye! Good luck with your studies!")
        sys.exit()
        
    elif "list" in query or "streams" in query or "options" in query:
        return "I can tell you about: Computer Science, Mechanical, Electrical, Civil, or Chemical Engineering."

    # 2. Computer Science Engineering Rule
    elif "computer" in query or "software" in query or "coding" in query or "programming" in query or "cs" in query:
        return (
            "\n[ COMPUTER SCIENCE ENGINEERING ]\n"
            "Focuses on software development, algorithms, data structures, AI, and cybersecurity. "
            "It's ideal for those who love logic, problem-solving, and building digital systems."
        )

    # 3. Mechanical Engineering Rule
    elif "mechanical" in query or "mech" in query or "machines" in query or "engines" in query or "cars" in query:
        return (
            "\n[ MECHANICAL ENGINEERING ]\n"
            "Deals with the design, analysis, and manufacturing of physical systems. "
            "Covers everything from automotive engines and aerospace tech to robotics and thermodynamics."
        )

    # 4. Electrical Engineering Rule
    elif "electrical" in query or "ee" in query or "power" in query or "circuits" in query or "electronics" in query:
        return (
            "\n[ ELECTRICAL ENGINEERING ]\n"
            "Focuses on the study and application of electricity, electronics, and electromagnetism. "
            "You'll work on power grids, renewable energy, microchips, and circuitry."
        )

    # 5. Civil Engineering Rule
    elif "civil" in query or "bridges" in query or "buildings" in query or "construction" in query or "roads" in query:
        return (
            "\n[ CIVIL ENGINEERING ]\n"
            "All about designing, constructing, and maintaining physical infrastructure. "
            "Includes building bridges, dams, highways, skyscrapers, and sustainable cities."
        )

    # 6. Chemical Engineering Rule
    elif "chemical" in query or "chemistry" in query or "materials" in query or "pharma" in query:
        return (
            "\n[ CHEMICAL ENGINEERING ]\n"
            "Bridges chemistry and engineering to transform raw materials into valuable products "
            "(like plastics, pharmaceuticals, and fuels) via large-scale industrial processes."
        )

    # 7. Fallback Rule (Runs if none of the above conditions are met)
    else:
        return "I didn't quite catch that. Try typing an engineering branch (like 'Mechanical'), or type 'list'!"

# --- Main Conversation Loop ---
def main():
    print("ChatBot: Active. Type 'list' to see available streams, or 'exit' to quit.")
    while True:
        try:
            user_msg = input("\nYou: ")
            response = get_bot_response(user_msg)
            print(f"ChatBot: {response}")
        except (KeyboardInterrupt, EOFError):
            print("\nMChatBot: Goodbye!")
            break

if __name__ == "__main__":
    main()