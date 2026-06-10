# Test Cases -Career Expert Systems 
 This document shows sample inputs and expected outputs for the Career Recommendation System.

## Test Case 1: Software Development Path

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
