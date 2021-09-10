from jotform import *
import os

JOT_KEY = os.environ['JOT_KEY']



jotformAPIClient = JotformAPIClient(JOT_KEY)

forms = jotformAPIClient.get_forms()

cep = []
for form in forms:

  new_cep = form["CEP"]
  cep.append(new_cep)
    
print(cep)