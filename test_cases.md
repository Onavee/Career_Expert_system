# Test Cases -Career Expert Systems 
 This document shows sample inputs and expected outputs for the Career Recommendation System.

## Test Case 1: Software Development Path

 ### input
 ```text
Enter your Interests separated by comma

Your interests: mathematics,programming

Intial Facts: {'mathematics', 'programming'}

 Running Inference Engine

Rule Fired -> ['conditions'] =>software_skills
Rule Fired -> ['conditions'] =>Software Developer

 Final Career Recommendations

Software Developer

 Reasoning Process

['programming', 'mathematics'] => software_skills
['software_skills'] => Software Developer
```

## Test Case 2: Psychology Path

### input
```text
Enter your Interests separated by comma

Your interests: psychology,critical_thinking                            

Intial Facts: {'psychology', 'critical_thinking'}

 Running Inference Engine

Rule Fired -> ['psychology', 'critical_thinking'] => psychology_skills
Rule Fired -> ['psychology_skills'] => counselling_candidate
Rule Fired -> ['counselling_candidate'] => Psychologist

 Final Career Recommendations

Psychologist

 Reasoning Process

['psychology', 'critical_thinking'] => psychology_skills
['psychology_skills'] => counselling_candidate
['counselling_candidate'] => Psychologist
```
## Test Case 3: Medicine Path

### Input
```text
Enter your Interests separated by comma

Your interests: biology, research

Intial Facts: {'research', 'biology'}

 Running Inference Engine

Rule Fired -> ['biology', 'research'] => life_science_skills
Rule Fired -> ['life_science_skills'] => medical_candidate
Rule Fired -> ['medical_candidate'] => Doctor

 Final Career Recommendations

Doctor

 Reasoning Process

['biology', 'research'] => life_science_skills
['life_science_skills'] => medical_candidate
['medical_candidate'] => Doctor
```
## Test Case 4: International Relations Path
 ### Input
 ```text
 Enter your Interests separated by comma

Your interests: film, creativity

Intial Facts: {'creativity', 'film'}

 Running Inference Engine

Rule Fired -> ['film', 'creativity'] => film_candidate
Rule Fired -> ['film_candidate'] => Film Director

 Final Career Recommendations

Film Director

 Reasoning Process

['film', 'creativity'] => film_candidate
['film_candidate'] => Film Director
```
## Test Case 5: No strong Match

### Input
```test
Enter your Interests separated by comma

Your interests: music, singing

Intial Facts: {'singing', 'music'}

 Running Inference Engine


 Final Career Recommendations

No strong career match found. 
```

## Summary
The system correctly:

-Applies forward chaining inference

-Generates Intermediate facts

-Produces final career recommendations

-Handles unmatched inputs gracefully






