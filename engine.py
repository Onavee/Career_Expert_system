# Inference Engine
def forward_chain(facts,rules):
    new_fact_added=True
    explanation = []

    while new_fact_added:
        new_fact_added = False

        for rule in rules:
            if all(condition in facts for condition in rule["conditions"]):
                result = rule["conclusion"]

                if result not in facts:
                    facts.add(result)

                    explanation.append({
                        "rule":rule["conditions"],
                        "result":result
                    })
                    print(f"Rule Fired -> {["conditions"]} =>{result}")
                    new_fact_added= True

    return facts, explanation