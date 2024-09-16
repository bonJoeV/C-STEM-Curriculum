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

def update_readme():
    directory = './LessonPlans/Grades1-3/'
    files = os.listdir(directory)

    readme_content = "# STEM Lesson Plans Directory\n\n"
    readme_content += "Here are the available lesson plans for Grades 1-3. Each plan includes activities, Catholic integration, and technology tools available for checkout.\n\n"

    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(directory, file)
            lesson_info = extract_lesson_info(filepath)
            
            if lesson_info["name"]:
                readme_content += f"### [{lesson_info['name']}]({directory}{file})\n"
                readme_content += f"- **Grade**: {lesson_info['grade']}\n"
                readme_content += f"- **Duration**: {lesson_info['duration']}\n"
                readme_content += f"- **Topic**: {lesson_info['topic']}\n"
                readme_content += f"- **Overview**: {lesson_info['overview']}\n"
                readme_content += f"- **Materials**: {lesson_info['materials']}\n"
                readme_content += f"- **Catholic Integration**: {lesson_info['catholic_integration']}\n"
                readme_content += f"- **Assessment**: {lesson_info['assessment']}\n\n"

    with open("READMEd.md", "w") as readme_file:
        readme_file.write(readme_content)

if __name__ == "__main__":
    update_readme()
