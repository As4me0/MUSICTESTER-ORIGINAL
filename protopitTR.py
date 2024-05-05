
import tkinter as tk


music_suggestions = {
    ('piyano', 'mavi', 'kedi'): "Yarım enerjik piyano parçalarını seviyorsunuz. Örneğin, 'Suburbia Overture / Greetings from Mary Bell Township! / (Vampire) Culture / Love Me, Normally' dinlemeyi deneyebilirsiniz.",
    ('piyano', 'kırmızı', 'köpek'): "Enerjik dokunuşlu piyano bestelerinden hoşlanıyorsunuz. Love, Me Normally adlı parçayı beğenebilirsiniz.",
    ('piyano', 'sarı', 'balık'): "Tadınız yumuşak piyano melodilerine kayıyor. 'Yiruma - River Flows in You' adlı eseri beğenebilirsiniz.",

    ('gitar', 'mavi', 'kedi'): "Canlı ama sakin gitar parçalarını tercih ediyorsunuz. Yürek-Duman adlı parçayı beğenebilirsiniz.",
    ('gitar', 'kırmızı', 'köpek'): "Tadınız rock gitarına kayıyor. Laplace's Angel adlı parçayı beğenebilirsiniz.",
    ('gitar', 'sarı', 'balık'): "Akustik gitar melodilerinden hoşlanıyorsunuz. 'Fleetwood Mac - Landslide' adlı parçayı beğenebilirsiniz.",

    ('keman', 'mavi', 'kedi'): "Klasik keman bestelerini takdir ediyorsunuz. 'Ludwig van Beethoven - Violin Concerto in D major' adlı eseri beğenebilirsiniz.",
    ('keman', 'kırmızı', 'köpek'): "Tadınız duygusal keman parçalarına kayıyor. 'Tchaikovsky - Violin Concerto in D major' adlı eseri beğenebilirsiniz.",
    ('keman', 'sarı', 'balık'): "Halk müziği etkisi olan keman parçalarından hoşlanıyorsunuz. 'Lindsey Stirling - Shadows' adlı eseri beğenebilirsiniz.",
    
    ('piyano', 'kırmızı', 'kedi'): "Tadınız HEYECANLI piyano parçalarına kayıyor!!! 2econd 2ight 2eer adlı parçayı beğenebilirsiniz. (Bu eğlenceliydi, hoşça kal.)",
    ('piyano', 'mavi', 'köpek'): "Romantik bir hava yayan piyano bestelerinden hoşlanıyorsunuz. 'Claude Debussy - Clair de Lune' adlı eseri beğenebilirsiniz.",
    ('piyano', 'sarı', 'kedi'): "Tadınız eğlenceli piyano melodilerine kayıyor. 'Scott Joplin - The Entertainer' adlı eseri beğenebilirsiniz.",
    
    ('gitar', 'kırmızı', 'kedi'): "Blues tarzı gitar riflerinden hoşlanıyorsunuz. 'B.B. King - The Thrill Is Gone' adlı eseri beğenebilirsiniz.",
    ('gitar', 'mavi', 'köpek'): "Tadınız ruhani gitar sololarına kayıyor. 'Pink Floyd - Comfortably Numb' adlı eseri beğenebilirsiniz.",
    ('gitar', 'sarı', 'kedi'): "Akustik gitar baladlarını tercih ediyorsunuz. 'Ed Sheeran - Thinking Out Loud' adlı eseri beğenebilirsiniz.",
    
    ('keman', 'kırmızı', 'kedi'): "Tadınız tutkulu keman performanslarına kayıyor. 'Pablo de Sarasate - Zigeunerweisen' adlı eseri beğenebilirsiniz.",
    ('keman', 'mavi', 'köpek'): "Virtüöz keman parçalarından hoşlanıyorsunuz. Masquerade by Lindsey Stirling adlı eseri beğenebilirsiniz.",
    ('keman', 'sarı', 'kedi'): "Keman melodilerini sakin temalı buluyorsunuz. Chanson de Nuit adlı eseri beğenebilirsiniz.",

    ('piyano', 'mavi', 'balık'): "Tadınız piyano performanslarıyla sakin parçalara kayıyor! Clair de Lune adlı eseri beğenebilirsiniz.",
    ('keman', 'mavi', 'balık'): "Tadınız keman performanslarıyla sakin parçalara kayıyor! Massenet: (Thaïs) adlı eseri beğenebilirsiniz.",
    ('gitar', 'mavi', 'balık'): "Tadınız gitar performanslarıyla sakin parçalara kayıyor! Lovesong by beabadoobee adlı eseri beğenebilirsiniz.",

    ('gitar', 'mavi', 'balık'): "Tadınız gitar performanslarıyla sakin parçalara kayıyor! Lovesong by beabadoobee adlı eseri beğenebilirsiniz.",

    ('piyano', 'kırmızı', 'balık'): "Tadınız hüzünlü piyano performanslarına kayıyor. Epilogue by Justin Hurwitz adlı eseri beğenebilirsiniz!",
    ('keman', 'kırmızı', 'balık'): "Tadınız hüzünlü keman performanslarına kayıyor. Nocturne by Lili Boulanger adlı eseri beğenebilirsiniz!",
    ('gitar', 'kırmızı', 'balık'): "Tadınız derin gitar performanslarına kayıyor. Heart Shape Box by Nirvana adlı eseri beğenebilirsiniz!",

    ('diğer', 'kırmızı', 'balık'): "Geleneksel olmayan seslerden hoşlanıyorsunuz. 'Daft Punk - Get Lucky' adlı eseri beğenebilirsiniz.",
    ('diğer', 'mavi', 'balık'): "Deneysel müziği takdir ediyorsunuz. 'Pink Floyd - Comfortably Numb' adlı eseri beğenebilirsiniz.",
    ('diğer', 'sarı', 'köpek'): "Tadınız çeşitlidir. 'The Rolling Stones - Paint It Black' adlı eseri beğenebilirsiniz.",

    ('diğer', 'kırmızı', 'kedi'): "Maceralı bir müzik zevkiniz var. 'Mind Brand -- MARETU' adlı eseri beğenebilirsiniz.",
    ('diğer', 'mavi', 'köpek'): "Enerjik ritimleri seviyorsunuz. 'Queen - We Will Rock You' adlı eseri beğenebilirsiniz.",
    ('diğer', 'sarı', 'kedi'): "Müzik zevkiniz çeşitlidir. 'The Doors - Light My Fire' adlı eseri beğenebilirsiniz.",
    
    ('diğer', 'kırmızı', 'köpek'): "Maceralı bir müzik zevkiniz var. 'AISHITE AISHITE AISHITE -- KIKUO' adlı eseri beğenebilirsiniz.",
    ('diğer', 'mavi', 'köpek'): "Enerjik ritimleri seviyorsunuz. 'イイコと妖狐 Kikuo' adlı eseri beğenebilirsiniz.",
    ('diğer', 'sarı', 'köpek'): "Müzik zevkiniz daha pozitiftir. 'Ac-cent-tchu-ate the Positive' adlı eseri beğenebilirsiniz.",

    ('diğer', 'mavi', 'kedi'): "Sakin ama ritmik ritimleri seviyorsunuz. 'Jamiroquai Bee Gees Mashup' adlı eseri beğenebilirsiniz.",
    
    ('piyano', 'diğer', 'balık'): "Tadınız sakin temalara kayıyor. 'From The Start' adlı eseri beğenebilirsiniz.",
    ('keman', 'diğer', 'balık'): "Tadınız hüzünlü ancak ritmik performanslara kayıyor. 'Nazınla Dünya' adlı eseri beğenebilirsiniz.",
    ('gitar', 'diğer', 'balık'): "Tadınız derin gitar performanslarına kayıyor. 'Laplace's Angel' adlı eseri beğenebilirsiniz.",

    ('piyano', 'diğer', 'kedi'): "Tadınız daha eğlenceli performanslara kayıyor. 'Feeling Good' adlı eseri beğenebilirsiniz.",
    ('keman', 'diğer', 'kedi'): "Tadınız yumuşak şarkılara kayıyor. '2 Days Into collage' adlı eseri beğenebilirsiniz.",
    ('gitar', 'diğer', 'kedi'): "Tadınız enerjik ama yormayan türlere kayıyor. 'Lovefool' adlı eseri beğenebilirsiniz.",

    ('diğer', 'diğer', 'kedi'): "Tadınız daha eğlenceli performanslara kayıyor. 'Feeling Good' adlı eseri beğenebilirsiniz.",
    ('diğer', 'diğer', 'köpek'): "Bateri sever misiniz? 'WHİPLASH' adlı eseri beğenebilirsiniz.",
    ('diğer', 'diğer', 'balık'): "Tadınız enerjik ama yormayan türlere kayıyor. 'Careless Whisper' adlı eseri beğenebilirsiniz.",

    ('piyano', 'diğer', 'diğer'): "Blues ya da Jazz sever misiniz? Tadınız daha eğlenceli performanslara kayıyor. 'Feeling Good' adlı eseri beğenebilirsiniz.",
    ('keman', 'diğer', 'diğer'): "Tadınız yumuşak şarkılara kayıyor. '2 Days Into collage' adlı eseri beğenebilirsiniz.",
    ('gitar', 'diğer', 'diğer'): "Tadınız enerjik ama yormayan türlere kayıyor. 'Lovefool' adlı eseri beğenebilirsiniz."
}



def get_music_suggestion():
    # Seçimleri alalım
    instrument = instrument_var.get()
    color = color_var.get()
    animal = animal_var.get()
    
    # Öneriyi alalım
    suggestion = music_suggestions.get((instrument, color, animal), "Üzgünüz, cevaplarınıza dayalı bir öneri bulamadık.")
    
    result_label.config(text=suggestion)

window = tk.Tk()
window.geometry("600x400")
window.title("Müzik Türü Seçici")

# Soruları oluşturalım
instrument_label = tk.Label(window, text="Hangi enstrümanı tercih edersiniz?")
instrument_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

instrument_var = tk.StringVar()
instrument_options = ['piyano', 'keman', 'gitar', 'diğer']
instrument_var.set(instrument_options[0])

instrument_menu = tk.OptionMenu(window, instrument_var, *instrument_options)
instrument_menu.grid(row=0, column=1, padx=10, pady=10)

# Soru 2
color_label = tk.Label(window, text="En sevdiğiniz renk nedir?")
color_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

color_var = tk.StringVar()
color_options = ['mavi', 'kırmızı', 'sarı', 'diğer']
color_var.set(color_options[0])

color_menu = tk.OptionMenu(window, color_var, *color_options)
color_menu.grid(row=1, column=

1, padx=10, pady=10)

# Soru 3
animal_label = tk.Label(window, text="En sevdiğiniz hayvan nedir?")
animal_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

animal_var = tk.StringVar()
animal_options = ['kedi', 'köpek', 'balık', 'diğer']
animal_var.set(animal_options[0])

animal_menu = tk.OptionMenu(window, animal_var, *animal_options)
animal_menu.grid(row=2, column=1, padx=10, pady=10)

suggest_button = tk.Button(window, text="Öneriyi Getir!!!", command=get_music_suggestion)
suggest_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(window, text="", wraplength=500)
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
