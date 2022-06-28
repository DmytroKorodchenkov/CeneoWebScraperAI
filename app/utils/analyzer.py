def analyzer(product_id):
    from opcode import opname
    import pandas as pd
    from numpy import average, product
    from fileinput import filename

    opinions = pd.read_json(f"opinions/{product_id}.json")

    opinions_count = len(opinions)
    pros_count = opinions["pros"].map(bool).sum()
    cons_count = opinions["cons"].map(bool).sum()
    average_score = opinions["score"].mean().round(2)
    data = {
        'id': product_id,
        'opinions_count': opinions_count,
        'pros_count': pros_count,
        'cons_count': cons_count,
        'average_score': average_score
    }
    return data 
