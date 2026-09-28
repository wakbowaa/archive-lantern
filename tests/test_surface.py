from pathlib import Path
s=(Path(__file__).parents[1]/'contracts'/'contract.py').read_text()
def test_surface():
 for n in ['install','draft_label','get_exhibit','get_reviews_page','get_exhibits_page','get_summary']:assert f'def {n}' in s
def test_guards():
 for n in ['actor in people','int(e.cursor)>=len(objects)','int(e.dims)>=3','run_nondet_unsafe']:assert n in s
