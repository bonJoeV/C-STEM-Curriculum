import os

def extract_lesson_info(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()

    lesson_info = {
        "name": None,
        "grade": None,
        "duration": None,
        "topic": None,
        "overview": None,
        "materials": None,
        "catholic_integration": None,
        "assessment": None
    }

    for i, line in enumerate(lines):
        if line.startswith("# "):
            lesson_info["name"] = line.replace("#", "").strip()
        elif line.startswith("### **Grade**"):
            lesson_info["grade"] = line.replace("### **Grade**:", "").strip()
        elif line.startswith("### **Duration**"):
            lesson_info["duration"] = line.replace("### **Duration**:", "").strip()
        elif line.startswith("### **Topic**"):
            lesson_info["topic"] = line.replace("### **Topic**:", "").strip()
        elif line.startswith("## **Overview**"):
            lesson_info["overview"] = lines[i+1].strip()  # Assuming next line contains the overview
        elif line.startswith("## **Materials**"):
            lesson_info["materials"] = lines[i+1].strip()  # Assuming next line contains materials
        elif line.startswith("## **Catholic Integration**"):
            lesson_info["catholic_integration"] = lines[i+1].strip()  # Catholic integration follows header
        elif line.startswith("## **Assessment**"):
            lesson_info["assessment"] = lines[i+1].strip()  # Assessment follows header

    return lesson_info

def update_readme2():
    # Change the path to navigate to LessonPlans from the scripts/ directory
    lessonplans_directory = '/LessonPlans/Grades1-3/'
    
    # Files in the LessonPlans/Grades1-3/ directory
    files = os.listdir(lessonplans_directory)

    readme2_content = "# Lesson Plans for Grades 1-3\n\n"
    readme2_content += "Here are the available lesson plans for Grades 1-3. Each plan includes activities, Catholic integration, and technology tools available for checkout.\n\n"

    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(lessonplans_directory, file)
            lesson_info = extract_lesson_info(filepath)
            
            if lesson_info["name"]:
                # Adjust the link to the lesson plan so it works correctly in the README2.md file
                readme2_content += f"### [{lesson_info['name']}]({file})\n"
                readme2_content += f"- **Grade**: {lesson_info['grade']}\n"
                readme2_content += f"- **Duration**: {lesson_info['duration']}\n"
                readme2_content += f"- **Topic**: {lesson_info['topic']}\n"
                readme2_content += f"- **Overview**: {lesson_info['overview']}\n"
                readme2_content += f"- **Materials**: {lesson_info['materials']}\n"
                readme2_content += f"- **Catholic Integration**: {lesson_info['catholic_integration']}\n"
                readme2_content += f"- **Assessment**: {lesson_info['assessment']}\n\n"

    # Write the updated content to LessonPlans/README2.md
    with open("../LessonPlans/README2.md", "w") as readme2_file:
        readme2_file.write(readme2_content)

if __name__ == "__main__":
    update_readme2()
