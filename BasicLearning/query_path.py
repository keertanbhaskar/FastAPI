from fastapi import FastAPI

app =FastAPI()

all_customers = [
  {'id':100,'name':'keerti','city':'mumbai','risk':'low'},
  {'id':101,'name':'sam','city':'delhi','risk':'high'},
  {'id':102,'name':'suri','city':'mumbai','risk':'low'},
  {'id':103,'name':'keertana','city':'bengalore','risk':'medium'},
  {'id':104,'name':'sanjana','city':'delhi','risk':'high'},
  {'id':105,'name':'resh','city':'mangalore','risk':'medium'},

]


# always set limit for both path and query
# @app.get('/customer')
# def get_customer(city:str,risk:str):
