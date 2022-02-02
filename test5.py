import json


# פונקציה המוסיפה נתונים לקובץ גיסון
def write_json_test(new_data, filename='data.json'):
    with open(filename, 'r+') as file:
        # טעינת נתונים ראשונים לתוך המילון
        file_data = json.load(file)

        # הכנסת ערכים לתוך שדה פירטי עובדים
        file_data["emp_details"].append(new_data)
        # להגיד את המיקום הנוכחי של הקובץ בהסט
        file.seek(0)
        # המר בחזרה לגסון
        json.dump(file_data, file, indent=4)

y = {"emp_name": "koral hazan",
     "email": "koral760@geeksforgeeks.org",
     "job_profile": "Full Time"
     }
z={"pin":2525,
   "gme":"eden"
   }
# קריאה לפונקציה
y.update(z)
write_json_test(y)
