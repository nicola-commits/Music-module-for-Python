allnotes = ["Dobb", "Dob", "Do", "Do#", "Do##", "Rebb", "Reb", "Re", "Re#", "Re##", "Mibb", "Mib", "Mi", "Mi#", "Mi##", "Fabb", "Fab", "Fa", "Fa#", "Fa##", "Solbb", "Solb", "Sol", "Sol#", "Sol##", "Labb", "Lab", "La", "La#", "La##", "Sibb", "Sib", "Si", "Si#", "Si##"]
validnotes = ["Dob", "Do", "Do#", "Reb", "Re", "Re#", "Mib", "Mi", "Mi#", "Fab", "Fa", "Fa#", "Solb", "Sol", "Sol#", "Lab", "La", "La#", "Sib", "Si", "Si#"]

def isvalidnote(note):
    return note in validnotes

def raiseerror(note, mode):
    if not isvalidnote(note) or mode not in ['M', 'm', 'dim', 'aum', 'perfect']:
        raise SyntaxError("Wrong Syntax! notes:Re# (no ## or bb), modes:'M', 'm', 'aum', 'dim', 'perfect'")

def second_lenght(note, mode="M"):
    raiseerror(note, mode)
    return allnotes[allnotes.index(note) + {"M":5, "m":4}.get(mode)] + "/" + allnotes[allnotes.index(note) + {"M":2, "m":1}.get(mode)] if note not in [allnotes[9:14]] else allnotes[allnotes.index(note) + {"M":6, "m":5}.get(mode)] + "/" + allnotes[allnotes.index(note) + {"M":3, "m":2}.get(mode)]
def third_lenght(note, mode='M'):
    raiseerror(note, mode)
    return allnotes[allnotes.index(note) + {"M":10, "m":9}.get(mode)] + "/" + allnotes[allnotes.index(note) + {"M":5, "m":4}.get(mode)] if note not in [allnotes[9:14]] else allnotes[allnotes.index(note) + {'M':6, "m":5}.get(mode)] + "/" + allnotes[allnotes.index(note) + {"M":3, "m":2}.get(mode)]
def fourth_lenght(note, mode='M'):
    raiseerror(note, mode)
    return allnotes[allnotes.index(note) + {"M":5, "m":4}.get(mode)] + "/" + allnotes[allnotes.index(note) + {"M":2, "m":1}.get(mode)] if note not in [allnotes[9:14]] else allnotes[allnotes.index(note) + {"M":6, "m":5}.get(mode)] + "/" + allnotes[allnotes.index(note) + {"M":3, "m":2}.get(mode)]
def fifth_lenght(note, mode='M'):
    raiseerror(note, mode)
    return allnotes[allnotes.index(note) + {'dim':19, 'aum':21}.get(mode, 20)]
def sixth_lenght(note, mode="M"):
    raiseerror(note, mode)
    return allnotes[allnotes.index(note) + {"M":5, "m":4}.get(mode)] + "/" + allnotes[allnotes.index(note) + {"M":2, "m":1}.get(mode)] if note not in [allnotes[9:14]] else allnotes[allnotes.index(note) + {"M":6, "m":5}.get(mode)] + "/" + allnotes[allnotes.index(note) + {"M":3, "m":2}.get(mode)]
def seventh_lenght(note, mode="M"):
    raiseerror(note, mode)
    return allnotes[allnotes.index(note) + {"M":5, "m":4}.get(mode)] + "/" + allnotes[allnotes.index(note) + {"M":2, "m":1}.get(mode)] if note not in [allnotes[9:14]] else allnotes[allnotes.index(note) + {"M":6, "m":5}.get(mode)] + "/" + allnotes[allnotes.index(note) + {"M":3, "m":2}.get(mode)]