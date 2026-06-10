# Knowledge base
FACT_LIST= [
    "programming",
    "problem_solving",
    "mathematics",
    "biology",
    "psychology",
    "film",
    "creativity",
    "storytelling",
    "helping_people",
    "research",
    "critical_thinking",
    "politics",
    "international_relations",
    "public_speaking",
    "ai"
]
RULES =[
     # Tech path
    {
        "conditions":["programming","problem_solving"],
        "conclusion":"technical_skills"
    },
    {
        "conditions":["technical_skills","ai"],
        "conclusion":"AI_Candidate"
    },
    {
        "conditions":["AI_Candidate"],
        "conclusions":"Artifical Intelligence Engineer"
    },
    {
        "conditions":["programming","mathematics"],
        "conclusion":"software_skills"
    },
    {
        "conditions":["software_skills"],
        "conclusion":"Software Developer"
    },

    # Medicine path
    {
        "conditions":["biology","research"],
        "conclusion":"life_science_skills"

    },
    {
        "conditions":["life_science_skills"],
        "conclusions":"medical_candidate"

    },
    {
        "conditions":["medical_candidate"],
        "conclusions":"Doctor"
    },
    # Psychology path
    {
        "conditions":["psychology","critical_thinking"],
        "conclusions":"psychology_skills"
    },
    {
       "conditions":["psychology_skills"],
       "conclusions":"counselling_candidate"
    },
    {
        "conditions":["counselling_candidate"],
        "conclusions":"Pyschologist"
    },
    # Film
    {
        "conditions":["film","creativity"],
        "conclusions":"film_candidate"

    },
    {
        "conditions":["film_candidate"],
        "conclusions":"Film Director"
    },
    
    # International Relations
    {
        "conditions":["politics","International_relations","public_speaking"],
        "conclusion":"Diplomat"
    }
]
   

