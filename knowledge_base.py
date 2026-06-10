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
    "International_relations",
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
        "conclusion":"Artifical Intelligence Engineer"
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
        "conclusion":"medical_candidate"

    },
    {
        "conditions":["medical_candidate"],
        "conclusion":"Doctor"
    },
    # Psychology path
    {
        "conditions":["psychology","critical_thinking"],
        "conclusion":"psychology_skills"
    },
    {
       "conditions":["psychology_skills"],
       "conclusion":"counselling_candidate"
    },
    {
        "conditions":["counselling_candidate"],
        "conclusion":"Psychologist"
    },
    # Film
    {
        "conditions":["film","creativity"],
        "conclusion":"film_candidate"

    },
    {
        "conditions":["film_candidate"],
        "conclusion":"Film Director"
    },
    
    # International Relations
    {
        "conditions":["politics","International_relations","public_speaking"],
        "conclusion":"Diplomat"
    }
]
   