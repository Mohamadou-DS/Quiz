import streamlit as st

# Taux de conversion fixes (exemple - vous pouvez les mettre à jour dynamiquement)
conversion_rates = {
    "EUR": {"USD": 1.1, "MRU": 40.5, "XOF": 655.957},
    "USD": {"EUR": 0.91, "MRU": 37, "XOF": 594},
    "MRU": {"EUR": 0.025, "USD": 0.027, "XOF": 16.05},
    "XOF": {"EUR": 0.0015, "USD": 0.0017, "MRU": 0.0623},
}

# Interface principale
st.title("💱 Convertisseur de Devises")

# Entrées de l'utilisateur
amount = st.number_input("Montant à convertir", min_value=0.0, value=1.0, step=0.1)
from_currency = st.selectbox("Devises d'origine", list(conversion_rates.keys()))
to_currency = st.selectbox("Devises cible", list(conversion_rates.keys()))

# Conversion
if st.button("Convertir"):
    if from_currency == to_currency:
        st.write(f"Le montant reste le même : **{amount:.2f} {from_currency}**")
    else:
        rate = conversion_rates[from_currency][to_currency]
        converted_amount = amount * rate
        st.write(f"**{amount:.2f} {from_currency}** équivaut à **{converted_amount:.2f} {to_currency}**")

# Affichage des taux
st.subheader("Taux de conversion actuels")
st.write(conversion_rates)
