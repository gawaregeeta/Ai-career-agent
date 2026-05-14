import re

def tailor_resume(resume_text, job_description):
    print("AI Agent is analyzing engineering skills...")
    
    # Common Indian Engineering keywords
    keywords = ["AutoCAD", "Thermodynamics", "React", "Python", "SolidWorks", "MATLAB"]
    found_skills = [skill for skill in keywords if skill.lower() in job_description.lower()]
    
    if found_skills:
        summary = f"Results-oriented Engineer with specialized skills in {', '.join(found_skills)}."
    else:
        summary = "Proactive Engineering student focused on technical excellence and industry application."
    
    return summary

# Example test
sample_job = "Looking for a Mechanical Intern with knowledge of AutoCAD and Thermodynamics."
new_summary = tailor_resume("My old resume text", sample_job)

print("-" * 30)
print("TAILORED SUMMARY GENERATED:")
print(new_summary)
print("-" * 30)
