allnotes = ["Dobb", "Dob", "Do", "Do#", "Do##", "Rebb", "Reb", "Re", "Re#", "Re##", "Mibb", "Mib", "Mi", "Mi#", "Mi##", "Fabb", "Fab", "Fa", "Fa#", "Fa##", "Solbb", "Solb", "Sol", "Sol#", "Sol##", "Labb", "Lab", "La", "La#", "La##", "Sibb", "Sib", "Si", "Si#", "Si##"]
validnotes = ["Dob", "Do", "Do#", "Reb", "Re", "Re#", "Mib", "Mi", "Mi#", "Fab", "Fa", "Fa#", "Solb", "Sol", "Sol#", "Lab", "La", "La#", "Sib", "Si", "Si#"]

def isvalidnote(note):
    return note in validnotes

def raiseerror(note, mode, validmodes=['M', 'm']):
    if not isvalidnote(note) or mode not in validmodes:
        raise SyntaxError("Wrong Syntax! notes:Re# (no ## or bb), modes:'M', 'm', 'aum', 'dim', 'perfect'")

def second_lenght(note, mode="M"):
    raiseerror(note, mode)
    if mode == "M":
        return {"Do":"Re", "Re":"Mi", "Mi":"Fa#", "Fa":"Sol", "Sol":"La", "La":"Si", "Si":"Do#", "Do#":"Re#", "Re#":"Mi#", "Mi#":"Fa#", "Fa#":"Sol#", "Sol#":"La#", "La#":"Si#", "Si#":"Do#", "Dob":"Reb", "Reb":"Mib", "Mib":"Fa", "Fab":"Solb", "Solb":"Lab", "Lab":"Sib", "Sib":"Do"}.get(note)
    if mode == 'm':
        return {"Do":"Reb", "Re":"Mib", "Mi":"Fa", "Fa":"Solb", "Sol":"Lab", "La":"Sib", "Si":"Do", "Do#":"Re", "Re#":"Mi", "Mi#":"Fa", "Fa#":"Sol", "Sol#":"La", "La#":"Si", "Si#":"Do", "Dob":"Re", "Reb":"Mi", "Mib":"Fab", "Fab":"Sol", "Solb":"La", "Lab":"Si", "Sib":"Dob"}.get(note)
def third_lenght(note, mode='M'):
    raiseerror(note, mode)
    return allnotes[allnotes.index(note) + {"M":10, "m":9}.get(mode)] + "/" + allnotes[allnotes.index(note) + {"M":5, "m":4}.get(mode)] if note not in [allnotes[9:14]] else allnotes[allnotes.index(note) + {'M':6, "m":5}.get(mode)] + "/" + allnotes[allnotes.index(note) + {"M":3, "m":2}.get(mode)]
def fourth_lenght(note, mode='M'):
    raiseerror(note, mode)
    return allnotes[allnotes.index(note) + {"M":5, "m":4}.get(mode)] + "/" + allnotes[allnotes.index(note) + {"M":2, "m":1}.get(mode)] if note not in [allnotes[9:14]] else allnotes[allnotes.index(note) + {"M":6, "m":5}.get(mode)] + "/" + allnotes[allnotes.index(note) + {"M":3, "m":2}.get(mode)]
def fifth_lenght(note, mode='perfect', validmodes=['dim, aum, perfect']):
    raiseerror(note, mode)
    return allnotes[allnotes.index(note) + {'dim':19, 'aum':21}.get(mode, 20)]
def sixth_lenght(note, mode="M"):
    raiseerror(note, mode)
    return allnotes[allnotes.index(note) + {"M":5, "m":4}.get(mode)] + "/" + allnotes[allnotes.index(note) + {"M":2, "m":1}.get(mode)] if note not in [allnotes[9:14]] else allnotes[allnotes.index(note) + {"M":6, "m":5}.get(mode)] + "/" + allnotes[allnotes.index(note) + {"M":3, "m":2}.get(mode)]
def seventh_lenght(note, mode="M"):
    raiseerror(note, mode)
    return allnotes[allnotes.index(note) + {"M":5, "m":4}.get(mode)] + "/" + allnotes[allnotes.index(note) + {"M":2, "m":1}.get(mode)] if note not in [allnotes[9:14]] else allnotes[allnotes.index(note) + {"M":6, "m":5}.get(mode)] + "/" + allnotes[allnotes.index(note) + {"M":3, "m":2}.get(mode)]