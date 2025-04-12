from graphviz import Digraph

# Dane z tabeli: (rok, badacz, opis)
events = [
    ("1800", "W. Herschel", "Odkrycie promieniowania podczerwonego (IR)"),
    ("1801", "J.W. Ritter", "Odkrycie promieniowania ultrafioletowego (UV)"),
    ("1801", "T. Young", "Odkrycie interferencji światła"),
    ("1802", "W.H. Wollaston", "Obserwacja ciemnych prążków w widmie światła słonecznego"),
    ("1811–1813", "F. Arago", "Polaryzacja światła, filtr polaryzacyjny"),
    ("1814", "J. von Fraunhofer", "Siatka dyfrakcyjna, spektrometr, analiza linii widmowych"),
    ("1818", "A. Fresnel", "Wyjaśnienie polaryzacji światła"),
    ("1826", "Talbot, Herschel", "Barwa płomieni – podstawy spektrochemii"),
    ("1832", "J.K. Herschel", "Opis barw płomieni po dodaniu soli metali"),
    ("1837", "Knox", "Zależność przewodnictwa selenu od światła"),
    ("1840", "J.M. Petzval", "Budowa jasnego obiektywu"),
    ("1842", "C. Doppler", "Sformułowanie efektu Dopplera"),
    ("1845", "M. Faraday", "Zjawisko Faradaya – światło a pole magnetyczne"),
    ("1848", "L. Foucault", "Widmo absorpcyjne"),
    ("1850", "L. Foucault", "Światło wolniejsze w wodzie niż w powietrzu"),
    ("1855", "A.J. Ångström", "Linie absorpcyjne, wodór na Słońcu"),
    ("1859–1861", "Kirchhoff, Bunsen", "Podstawy spektroskopii, cez i rubid"),
    ("1861", "J.C. Maxwell", "Równania Maxwella – światło jako fala EM"),
    ("1866", "W. Huggins", "Spektroskopia astronomiczna"),
    ("1873", "E. Abbe, J.C. Maxwell", "Teorie optyczne, ograniczenia obrazowania"),
    ("1875", "P. de Boisbaudran", "Odkrycie pierwiastka gal (Ga)"),
    ("1877", "L.G. Gouy", "Pierwszy nebulizator pneumatyczny"),
    ("1882", "H. Rowland", "Udoskonalenie siatki dyfrakcyjnej"),
    ("1885", "J.J. Balmer", "Wzór na linie emisyjne wodoru"),
    ("1891", "G. Lippmann", "Reprodukcja barw metodą interferencyjną"),
    ("1895", "Geitel, Elster", "Fotokomórka próżniowa"),
    ("1897", "J.J. Thomson", "Odkrycie elektronu, spektrometr masowy"),
]

# Dodanie emoji do wydarzeń – uproszczone na potrzeby wizualizacji
emoji_map = {
    "odkrycie": "🔍",
    "widmo": "🌈",
    "światło": "💡",
    "spektroskopia": "🔬",
    "elektron": "⚛️",
    "teoria": "📘",
    "obiektyw": "📷",
    "dyfrakcja": "📐",
    "absorpcja": "🧪",
    "fotokomórka": "📸"
}

# Utwórz oś czasu jako graf skierowany
# Zmiana kierunku grafu na pionowy
dot = Digraph('TimelineXIXVertical', format='svg')
dot.attr(rankdir='TB', size='8')
dot.attr('node', shape='box', style='rounded,filled', fixedsize='true', width='3')  # Dodano fixedsize i width

# Modyfikacja: pionowy układ, ikony (jako emoji), zaokrąglone prostokąty



def assign_emoji(desc):
    for keyword, emoji in emoji_map.items():
        if keyword in desc.lower():
            return emoji + " "
    return "📎 "



# Dodaj węzły
for i, (year, person, desc) in enumerate(events):
    decade_key = year.split('–')[0][:3]
    #color = decade_colors.get(decade_key, "#FFFFFF")
    color="#ffaaff"
    label = f"{assign_emoji(desc)}{year}\n{person}\n{desc}"
    dot.node(str(i), label, fillcolor=color)


# Połącz w kolejności chronologicznej
for i in range(len(events) - 1):
    dot.edge(str(i), str(i + 1))

# Zapisz do pliku
output_path = "./timeline_xix_spektroskopia.svg"
dot.render(filename=output_path, cleanup=True)
output_path

