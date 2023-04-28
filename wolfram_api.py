import wolframalpha as w

def query(entry):
    client = w.Client('UTKURY-EAG5LRERLP')
    res = client.query(entry)
    output = next(res.results).text
    return output


