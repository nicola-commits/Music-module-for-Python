allnotes = ["Dobb", "Dob", "Do", "Do#", "Do##", "Rebb", "Reb", "Re", "Re#", "Re##", "Mibb", "Mib", "Mi", "Mi#", "Mi##", "Fabb", "Fab", "Fa", "Fa#", "Fa##", "Solbb", "Solb", "Sol", "Sol#", "Sol##", "Labb", "Lab", "La", "La#", "La##", "Sibb", "Sib", "Si", "Si#", "Si##"]
class lenght():
    def __init__(self, note):
        self.note = note
    def unisone(note):
        try:
            if note in allnotes: return note 
        except:
            raise ValueError("Invalid value")
    def second(note, tipo="M"):
        return allnotes[allnotes.index(note) + {"M":5, "m":4}.get(tipo)] + "/" + allnotes[allnotes.index(note) + {"M":2, "m":1}.get(tipo)] if note not in [allnotes[9:14]] else allnotes[allnotes.index(note) + {"M":6, "m":5}.get(tipo)] + "/" + allnotes[allnotes.index(note) + {"M":3, "m":2}.get(tipo)]
    def third(note, tipo='M'):
        return allnotes[allnotes.index(note) + {"M":10, "m":9}.get(tipo)] + "/" + allnotes[allnotes.index(note) + {"M":5, "m":4}.get(tipo)]