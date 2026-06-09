from fastapi import FastAPI,HTTPException
import queries

app = FastAPI()

@app.get('/soldiers')
def show_soldiers(mrank:str|None = None,ssort:str | None = None ,unit:str | None = None):
    if mrank:
       return queries.get_by_rank(mrank)
    elif unit:
        return queries.get_by_unit(unit)
    elif ssort:
        return queries.get_active_sorted(ssort)
    else:
        return queries.get_sorted_by_id()
@app.get('/soldiers/units')
def show_units():
    return queries.get_distent_unit()
@app.get('/soldiers/search')
def show_soldiers_by_names(name:str):
    return queries.search_by_name(name)
@app.get('/soldiers/missing-rank')
def show_empty_rank():
    return queries.get_missing_rank()


