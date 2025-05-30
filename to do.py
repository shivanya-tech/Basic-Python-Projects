from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)
tasks = []

TEMPLATE = '''
<!doctype html>
<title>To-Do List</title>
<h1>To-Do List</h1>

<form action="/" method="POST">
  <input name="task" placeholder="Enter new task" required>
  <button type="submit">Add Task</button>
</form>

<ul>
  {% for task in tasks %}
    {% set i = loop.index0 %}
    <li>
      {{ task['task'] }} - {{ '✅ Done' if task['status'] else '❌ Not Done' }}
      {% if not task['status'] %}
        <a href="{{ url_for('mark_done', task_id=i) }}">Mark as Done</a>
      {% endif %}
    </li>
  {% endfor %}
</ul>

'''

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task_text = request.form.get("task")
        tasks.append({"task": task_text, "status": False})
        return redirect(url_for("home"))
    return render_template_string(TEMPLATE, tasks=tasks)

@app.route("/done/<int:task_id>")
def mark_done(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]["status"] = True
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
