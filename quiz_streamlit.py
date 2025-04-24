import streamlit as st
import random

# Quiz interactif
st.title("🧠 Quiz interactif sur les maths")

# Générer une question aléatoire
def generate_question():
    operators = ["+", "-", "*", "/"]
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(operators)

    if operator == "/":
        question = f"Quelle est la division entière de {num1 * num2} ÷ {num2} ?"
        answer = num1
    elif operator == "*":
        question = f"Combien fait {num1} × {num2} ?"
        answer = num1 * num2
    elif operator == "+":
        question = f"Combien fait {num1} + {num2} ?"
        answer = num1 + num2
    else:
        question = f"Combien fait {num1} - {num2} ?"
        answer = num1 - num2

    return question, answer

# Session pour stocker la question et la réponse
if "question" not in st.session_state:
    st.session_state.question, st.session_state.answer = generate_question()

# Affichage de la question
st.write(f"**Question** : {st.session_state.question}")
user_answer = st.text_input("Entrez votre réponse :")

# Vérification de la réponse
if st.button("Vérifier la réponse"):
    if user_answer.strip().isdigit() and int(user_answer) == st.session_state.answer:
        st.success("Bonne réponse ! 🎉")
    else:
        st.error(f"Mauvaise réponse. La bonne réponse était : {st.session_state.answer}")
    # Générer une nouvelle question
    st.session_state.question, st.session_state.answer = generate_question()
