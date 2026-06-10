from knowledge_base import RULES, FACT_LIST
from engine import forward_chain
print("CAREER EXPERT SYSTEM(FORWARD CHAINING)\n")

print("Available Interests:")
print(",".join(FACT_LIST))
print("\nEnter your Interests separated by comma")

# User Input
user_input = input("\nYour interests: ").lower()

facts = set(i.strip() for i in user_input.split(","))

print("\nIntial Facts:", facts)

print("\n Running Inference Engine\n")

# running the forward chaining
final_facts, explanation = forward_chain(facts, RULES)

careers = [
    "Artificial Intelligence Developer",
    "Software Developer",
    "Doctor",
    "Psychologist",
    "Film Director",
    "Diplomat",
]

print("\n Final Career Recommendations\n")
found = False

for career in careers:
 if career in final_facts:
  print(career)
  found = True

if not found:
 print("No strong career match found. Try adding more interests.")
# Explanation section
print("\n Reasoning Process\n")

for step in explanation:
 print(f"{step["rule"]} => { step["result"]}")
 


 