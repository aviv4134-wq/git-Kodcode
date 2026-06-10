from fastapi import FastAPI,HTTPException
import reports

app = FastAPI()

@app.get('/stats/summary')
def get_summery():
    return reports.get_summery()

@app.get('/stats/units')
def get_stats_units():
    return reports.count_by_unit()

@app.get('/stats/understaffed')
def get_stats_understaffed():
    return reports.get_units_with_multiple_soldiers()

@app.get('/soldiers/missing-rank')
def get_soldiers_missing_rank():
    return reports.get_missing_data()

@app.get('/soldiers/by-rank')
def get_soldiers_byrank():
    return reports.soldiers_by_rank()

@app.get('/stats/units/top')
def get_max_units():
     return reports.stats_units_top()
