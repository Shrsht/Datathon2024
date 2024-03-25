import spacy
import skillset

def load_pipeline():
       
    nlp = spacy.load('Datathon_Final_Model') 

    return nlp   

def intialize_classes(skillset_obj, string_obj):

    nlp = load_pipeline()
    
    for doc in nlp.pipe([string_obj], disable=["tagger", "parser"]):
        for ent in doc.ents:
            if ent.label_ == 'TECHNICAL_SKILL':
                skillset_obj.tech_skill.append(ent.text) 
            elif ent.label_ == 'EDUCATION':
                skillset_obj.edu.append(ent.text)
            elif ent.label_ == 'PERSONALITY':
                skillset_obj.person.append(ent.text) 
            elif ent.label_ == 'EXPERIENCE':
                skillset_obj.exp.append(ent.text) 
            elif ent.label_ == 'PROJECT':
                skillset_obj.proj.append(ent.text) 
            elif ent.label_ == 'IMPACT':
                skillset_obj.impact.append(ent.text) 
            elif ent.label_ == 'ACHIEVEMENT':
                skillset_obj.achievement.append(ent.text) 
            elif ent.label_ == 'POSITION':
                skillset_obj.pos.append(ent.text) 
            elif ent.label_ == 'COMPANY':
                skillset_obj.company.append(ent.text) 
            elif ent.label_ == 'ACADEMICS':
                skillset_obj.acad.append(ent.text) 
            elif ent.label_ == 'TASK':
                skillset_obj.task.append(ent.text) 
            elif ent.label_ == 'NON TECHNICAL SKILL':
                skillset_obj.non_tech.append(ent.text)
            elif ent.label_ == 'TOOL':
                skillset_obj.tools.append(ent.text)
            elif ent.label_ == 'DEPARTMENT':
                skillset_obj.dept.append(ent.text)
            else:
                next
    return skillset_obj    
