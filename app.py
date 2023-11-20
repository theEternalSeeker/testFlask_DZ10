from flask import Flask
import utils

app = Flask(__name__)
candidates = utils.load_candidates()

@app.route("/")
def page_index():
    str_candidates = '<pre>'
    for candidate in candidates.values():
        str_candidates += f"{candidate['name']}\n{candidate['position']}\n{candidate['skills']}\n"
    str_candidates += '</pre>'
    return str_candidates

@app.route("/candidates/<int:id>")
def profile(id):
    candidate = candidates[id]
    str_candidate = f"<img src={candidate['picture']}></img><br><br>{candidate['name']}<br>{candidate['position']}<br>{candidate['skills']}<br><br>"
    return str_candidate

@app.route("/skills/<skill>")
def skill_(skill):
    str_skill = '<pre>'

    for candidate in candidates.values():
        candidate_skills = candidate['skills'].split(', ')
        candidate_skills = [x.lower() for x in candidate_skills]
        if skill in candidate_skills:
            str_skill += f"<br>{candidate['name']}<br><br>{candidate['position']}<br>{candidate['skills']}<br>"
    str_skill +='</pre>'
    return str_skill

app.run(host='127.0.0.2', port=80)







